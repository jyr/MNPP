<?php

/**
 * hook_drush_init()
 *
 */
function mnpp_drush_init(){
	$MNPP_PATH = '/Applications/MNPP/';
	
	if (file_exists($MNPP_PATH) && is_dir($MNPP_PATH)){
		define('MNPP_PATH', $MNPP_PATH);
		define('MNPP_INIT_SCRIPTS', MNPP_PATH . 'init/');
		define('MNPP_BIN', MNPP_PATH . 'init/mnpp');
	}
}

/**
 * Implementation of hook_drush_command()
 *
 */

function mnpp_drush_command(){
	$items = array();
	
	$items['mnpp'] = array(
		'description' => 'Quickly management to MNPP',
		'arguments' => array(
			'start' => 'Start MNPP services',
			'stop' => 'Stop MNPP services',
		),
		
		'options' => array(
			'nginx' => '',
			'percona' => '',
			'php-fpm' => '',
		),
		
		'examples' => array(
			'drush mnpp start' => 'Start all services',
			'drush mnpp stop' => 'Stop all services',
			'drush mnpp restart' => 'Restart all services',
			'drush mnpp --nginx=start|stop' => 'Start or Stop nginx',
			'drush mnpp --percona=start|stop' => 'Start or Stop percona',
			'drush mnpp --php-fpm=start|stop' => 'Start or Stop php-fpm',
		),
		'bootstrap' => DRUSH_BOOTSTRAP_DRUSH,
	);
	
	return $items;
}

/**
 * drush_COMMANDNAME()
 *
 */
function drush_mnpp(){
	$args = drush_get_arguments();

	if(in_array($args[1], array('restart', 'start', 'stop'))){
		mnpp_service_manage('', $args[1]);
		return;
	}
	else{
		$service_commands = array();
		$services = array('nginx', 'percona', 'php-fpm');
		foreach($services as $service){
			$service_command = drush_get_option($service);
			if($service_command){
				$service_commands[$service] = $service_command;
			}
		}
		
		foreach($service_commands as $service => $command){
			mnpp_service_manage($service, $command);
		}
	}
}

/**
 * drush_COMMANDNAME_validate()
 *
 */
function drush_mnpp_validate(){
	
	if(getenv('safe_mode')){
		return drush_set_error('MNPP_ERROR_PHP_SAFE_MODE', dt('PHP Safe mode is enabled, this option is deprecated from php 5.3.0'));
	}
	
	if(!defined('MNPP_PATH')){
		return drush_set_error('MNPP_ERROR_INSTALL', dt('You don´t have installed MNPP.'));
	}
}

/**
 * Manage a MNPP service
 *
 */

function mnpp_service_manage($service, $command){

	if ($command == "restart"){
		mnpp_service_manage($service, 'stop');
		mnpp_service_manage($service, 'start');
		
		return;
	}

	$script = mnpp_service_init_script($service, $command);
	mnpp_service_init_script_rc($service, $command, $script);
}

/**
 * Return init script for a service 
 * @param String $service
 * @param String $command
 */
function mnpp_service_init_script($service, $command){

	if(empty($service)){
		$script = 'mnpp --php53  --' . $command;
	}
	else{
		$service = mnpp_php_version($service);
		($service == 'php') ? $version = '53': $version = '';
		$script = 'mnpp --' . $command  . ' ' . $service . $version;
	}

	return MNPP_INIT_SCRIPTS . $script;
}

/**
 * Run command of script service
 * @param String $service
 * @param String $command
 * @param String $script
 */
function mnpp_service_init_script_rc($service, $command, $script){
	$script = "sudo " . $script . " > /Users/jyr/log.txt";
	$filename = mnpp_php_version($service, $command);	
	$rc = MNPP_INIT_SCRIPTS . $filename . ".sh";

	if(file_exists(MNPP_BIN) && file_exists($rc)){
		if(drush_shell_exec($script)){
			drush_log(dt('MNPP !service !command', array(
				'!service' => $service,
				'!command' => $command,
			)),
			'success'
		);
		}
		else{
			drush_set_error('MNPP_ERROR_RC', dt('Failed to !command !service. Make sure MNPP is running.', array(
				'!command' => $command,
				'!service' => $service
			)));
		}
	}
}

function mnpp_php_version($service, $command = ''){
	
	if ($service == 'php-fpm'){
		$service = 'php';
	}else if(empty($service)){
		$service = $command;
	}
	
	return $service;
}