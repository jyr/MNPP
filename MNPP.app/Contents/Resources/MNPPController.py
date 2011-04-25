#
#   MNPPController.py
#
#   Created by Jair Gaxiola on 06/01/11.
#   Copyright 2011 __MyCompanyName__. All rights reserved.
#

from Foundation import *
from AppKit import *
from Authorization import Authorization
from PreferencesController import PreferencesController

import objc
import os


class MNPPController (NSWindowController):
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
		if self:
			self.path = "/Applications/MNPP/init/"
			self.auth = Authorization()

		return self
		
    @objc.IBAction
    def startServers_(self, sender):
		try:
			settings = NSUserDefaults.standardUserDefaults()
			php53 = settings.boolForKey_("php53")
			php52 = settings.boolForKey_("php52")
			print "php53"
			print php53
			print "php52"
			print php52

			if php53:
				phpVersion = "53"
			else:
				phpVersion = "52"
			
			startScript = self.path + "start " + phpVersion
			print startScript
			self.auth.executeWithPrivileges(startScript)
			self.startButton.setHidden_(YES)
			self.stopButton.setHidden_(NO)
			self.startNginx.setHidden_(YES)
			self.stopNginx.setHidden_(NO)
			self.startMySQL.setHidden_(YES)
			self.stopMySQL.setHidden_(NO)
			self.startPHP.setHidden_(YES)
			self.stopPHP.setHidden_(NO)
		except:
			pass
		
    @objc.IBAction
    def stopServers_(self, sender):
		try:
			settings = NSUserDefaults.standardUserDefaults()
			php53 = settings.boolForKey_("php53")
			php52 = settings.boolForKey_("php52")
			print "php53"
			print php53
			print "php52"
			print php52

			if php53:
				phpVersion = "53"
			else:
				phpVersion = "52"
				
			stopScript = self.path + "stop " + phpVersion
			self.auth.executeWithPrivileges(stopScript)
			self.startButton.setHidden_(NO)
			self.stopButton.setHidden_(YES)
			self.startNginx.setHidden_(NO)
			self.stopNginx.setHidden_(YES)
			self.startMySQL.setHidden_(NO)
			self.stopMySQL.setHidden_(YES)
			self.startPHP.setHidden_(NO)
			self.stopPHP.setHidden_(YES)
		except:
			pass
	
    @objc.IBAction
    def openPage_(self, sender):
		urlMNPP = NSURL.URLWithString_("http://mnpp.astrata.local")
		workspace = NSWorkspace.sharedWorkspace().openURL_(urlMNPP)
	
    @objc.IBAction
    def startNginx_(self, sender):
		try:
			startNginx = self.path + "startNginx"
			self.auth.executeWithPrivileges(startNginx)
			self.startNginx.setHidden_(YES)
			self.stopNginx.setHidden_(NO)
		except:
			pass
	
    @objc.IBAction
    def stopNginx_(self, sender):
		try:		
			stopNginx = self.path + "stopNginx"
			self.auth.executeWithPrivileges(stopNginx)
			self.startNginx.setHidden_(NO)
			self.stopNginx.setHidden_(YES)
		except:
			pass

    @objc.IBAction
    def startMySQL_(self, sender):
		try:
			startMySQL = self.path + "startMySQL 53"
			self.auth.executeWithPrivileges(startMySQL)
			self.startMySQL.setHidden_(YES)
			self.stopMySQL.setHidden_(NO)
		except:
			pass
	
    @objc.IBAction
    def stopMySQL_(self, sender):
		try:
			stopMySQL = self.path + "stopMySQL"
			self.auth.executeWithPrivileges(stopMySQL)
			self.startMySQL.setHidden_(NO)
			self.stopMySQL.setHidden_(YES)
		except:
			pass

			
    @objc.IBAction
    def startPHP_(self, sender):
		try:		
			startPHP = self.path + "startPHP"
			self.auth.executeWithPrivileges(startPHP)
			self.startPHP.setHidden_(YES)
			self.stopPHP.setHidden_(NO)
		except:
			pass
	
    @objc.IBAction
    def stopPHP_(self, sender):
		try:
			stopPHP = self.path + "stopPHP"
			self.auth.executeWithPrivileges(stopPHP)
			self.startPHP.setHidden_(NO)
			self.stopPHP.setHidden_(YES)
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

		startMNPP = settings.boolForKey_("start")
		if startMNPP:
			self.startServers_(self)
		
		openMNPP = settings.boolForKey_("open")
		if openMNPP:
			self.startServers_(self)