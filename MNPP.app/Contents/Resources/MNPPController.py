#
#   MNPPController.py
#
#   Created by Jair Gaxiola on 06/01/11.
#   Copyright 2011 __MyCompanyName__. All rights reserved.
#

from Foundation import *
from AppKit import *
from Authorization import Authorization, kAuthorizationFlagDestroyRights
from PreferencesController import PreferencesController

import objc
import os


class MNPPController (NSWindowController):
    statusMenu = objc.IBOutlet()
    startButton = objc.IBOutlet()
    stopButton = objc.IBOutlet()
    startNginx = objc.IBOutlet()
    stopNginx = objc.IBOutlet()
    startMySQL = objc.IBOutlet()
    stopMySQL = objc.IBOutlet()
    startPHP = objc.IBOutlet()
    stopPHP = objc.IBOutlet()
    preferences = objc.IBOutlet()
    window = objc.IBOutlet()
	
    def init(self):
		self = super(MNPPController, self).initWithWindowNibName_("MainMenu")
		self.phpVersion = ""
		if self:
			self.path = "/Applications/MNPP/init/"
			self.auth = Authorization(destroyflags=(kAuthorizationFlagDestroyRights,))

		self.appDelegate = NSApp.delegate()
		return self
		
    @objc.IBAction
    def startServers_(self, sender):
		try:
			self.checkPhpVersion()
			startScript = self.path + "start" + self.phpVersion
			
			self.auth.executeWithPrivileges(startScript)
			self.enableUwsgi()
			self.changeStatusStartButtonALL()

			self.startNginx.setHidden_(YES)
			self.stopNginx.setHidden_(NO)
			self.startMySQL.setHidden_(YES)
			self.stopMySQL.setHidden_(NO)
			self.startPHP.setHidden_(YES)
			self.stopPHP.setHidden_(NO)
			
			self.appDelegate.changeStatusStartMenuALL()
			
			self.appDelegate.startNginx.setHidden_(YES)
			self.appDelegate.stopNginx.setHidden_(NO)
			self.appDelegate.startMySQL.setHidden_(YES)
			self.appDelegate.stopMySQL.setHidden_(NO)
			self.appDelegate.startPHP.setHidden_(YES)
			self.appDelegate.stopPHP.setHidden_(NO)

		except:
			pass
		
    @objc.IBAction
    def stopServers_(self, sender):
		try:
			self.checkPhpVersion()
			stopScript = self.path + "stop" + self.phpVersion
			self.disableUwsgi()
			self.auth.executeWithPrivileges(stopScript)

			self.changeStatusStopButtonALL()			
			self.startNginx.setHidden_(NO)
			self.stopNginx.setHidden_(YES)
			self.startMySQL.setHidden_(NO)
			self.stopMySQL.setHidden_(YES)
			self.startPHP.setHidden_(NO)
			self.stopPHP.setHidden_(YES)

			self.appDelegate.changeStatusStopMenuALL()
			self.appDelegate.stopNginx.setHidden_(YES)
			self.appDelegate.startNginx.setHidden_(NO)
			self.appDelegate.stopMySQL.setHidden_(YES)
			self.appDelegate.startMySQL.setHidden_(NO)	
			self.appDelegate.stopPHP.setHidden_(YES)
			self.appDelegate.startPHP.setHidden_(NO)	
			
		except:
			pass
	
    @objc.IBAction
    def openPage_(self, sender):
		urlMNPP = NSURL.URLWithString_("http://mnpp.local")
		workspace = NSWorkspace.sharedWorkspace().openURL_(urlMNPP)
	
    @objc.IBAction
    def startNginx_(self, sender):
		try:
			startNginx = self.path + "startNginx"
			self.auth.executeWithPrivileges(startNginx)
			self.enableUwsgi()
			
			self.changeStatusStartButtonALL()
			self.startNginx.setHidden_(YES)
			self.stopNginx.setHidden_(NO)
			
			"""
			Menu status bar options
			"""
			self.appDelegate.changeStatusStartMenuALL()
			#self.appDelegate.startNginx_(self)
			self.appDelegate.startNginx.setHidden_(YES)
			self.appDelegate.stopNginx.setHidden_(NO)
			
		except:
			pass
	
    @objc.IBAction
    def stopNginx_(self, sender):
		try:		
			stopNginx = self.path + "stopNginx"
			self.auth.executeWithPrivileges(stopNginx)
			self.disableUwsgi()
			
			self.changeStatusStopButtonALL()
			self.startNginx.setHidden_(NO)
			self.stopNginx.setHidden_(YES)

			"""
			Menu status bar options
			"""
			self.appDelegate.changeStatusStopMenuALL()
			self.appDelegate.stopNginx.setHidden_(YES)
			self.appDelegate.startNginx.setHidden_(NO)

		except:
			pass

    @objc.IBAction
    def startMySQL_(self, sender):
		try:
			startMySQL = self.path + "startMySQL"
			self.auth.executeWithPrivileges(startMySQL)
			self.changeStatusStartButtonALL()
			self.startMySQL.setHidden_(YES)
			self.stopMySQL.setHidden_(NO)
			
			"""
			Menu options
			"""
			self.appDelegate.changeStatusStartMenuALL()
			self.appDelegate.startMySQL.setHidden_(YES)
			self.appDelegate.stopMySQL.setHidden_(NO)


		except:
			pass
	
    @objc.IBAction
    def stopMySQL_(self, sender):
		try:
			stopMySQL = self.path + "stopMySQL"
			self.auth.executeWithPrivileges(stopMySQL)
			self.changeStatusStopButtonALL()
			self.startMySQL.setHidden_(NO)
			self.stopMySQL.setHidden_(YES)
			
			"""
			Menu options
			"""
			self.appDelegate.changeStatusStopMenuALL()
			self.appDelegate.stopMySQL.setHidden_(YES)
			self.appDelegate.startMySQL.setHidden_(NO)			
		except:
			pass

			
    @objc.IBAction
    def startPHP_(self, sender):
		try:
			self.checkPhpVersion()
			startPHP = self.path + "startPHP" + self.phpVersion

			self.auth.executeWithPrivileges(startPHP)
			self.changeStatusStartButtonALL()
			self.startPHP.setHidden_(YES)
			self.stopPHP.setHidden_(NO)
			
			"""
			Menu options
			"""
			self.appDelegate.changeStatusStartMenuALL()
			self.appDelegate.startPHP.setHidden_(YES)
			self.appDelegate.stopPHP.setHidden_(NO)

			
		except:
			pass
	
    @objc.IBAction
    def stopPHP_(self, sender):
		try:
			stopPHP = self.path + "stopPHP" + self.phpVersion
			self.auth.executeWithPrivileges(stopPHP)
			self.changeStatusStopButtonALL()
			self.startPHP.setHidden_(NO)
			self.stopPHP.setHidden_(YES)

			"""
			Menu options
			"""
			self.appDelegate.changeStatusStopMenuALL()
			self.appDelegate.stopPHP.setHidden_(YES)
			self.appDelegate.startPHP.setHidden_(NO)			
		except:
			pass

    @objc.IBAction
    def preferences_(self, sender):
		PreferencesController.show()
	
    @objc.IBAction
    def showPreferencesWindow_(self, sender):
		PreferencesController.show()
		#self.preferencesController = PreferencesController.alloc().init()
		#self.preferencesController.showWindow_(self)

    @objc.IBAction
    def exit_(self, sender):
		settings = NSUserDefaults.standardUserDefaults()
		stopMNPP = settings.boolForKey_("stop")
		
		if stopMNPP:
			self.stopServers_(self)

		NSApp().terminate_(self)

    def checkSettings(self):
		settings = NSUserDefaults.standardUserDefaults()
		php53 = settings.boolForKey_("php53")
		php52 = settings.boolForKey_("php52")
        
		if not php53 and not php52:
			settings.setObject_forKey_("1", 'php53')
			settings.setObject_forKey_("0", 'php52')
                
		startMNPP = settings.boolForKey_("start")
		if startMNPP:
			self.startServers_(self)
		
		openMNPP = settings.boolForKey_("open")
		if openMNPP:
			self.startServers_(self)
            

    def checkPhpVersion(self):
		settings = NSUserDefaults.standardUserDefaults()
		php53 = settings.boolForKey_("php53")
		php52 = settings.boolForKey_("php52")

		if php53:
			self.phpVersion = "53"
		else:
			self.phpVersion = "52"

    def changeStatusStartButtonALL(self):
		self.startButton.setHidden_(YES)
		self.stopButton.setHidden_(NO)

    def changeStatusStopButtonALL(self):
		self.startButton.setHidden_(NO)
		self.stopButton.setHidden_(YES)
		
    def enableUwsgi(self):
		settings = NSUserDefaults.standardUserDefaults()
		uwsgi = settings.boolForKey_("uwsgi")
		
		if uwsgi:
			enableUwsgi = self.path + "enableUwsgi"
			self.auth.executeWithPrivileges(enableUwsgi)

    def disableUwsgi(self):
		settings = NSUserDefaults.standardUserDefaults()
		uwsgi = settings.boolForKey_("uwsgi")
		
		disableUwsgi = self.path + "disableUwsgi"
		self.auth.executeWithPrivileges(disableUwsgi)
