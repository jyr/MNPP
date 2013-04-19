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
		except:
			pass
		
    @objc.IBAction
    def stopServers_(self, sender):
		try:
			self.checkPhpVersion()
			stopScript = self.path + "stop" + self.phpVersion

			self.disableUwsgi()
			self.auth.executeWithPrivileges(stopScript)
		except:
			pass

    @objc.IBAction
    def restartServers_(self, sender):
        try:
            self.checkPhpVersion()
            restartScript = self.path + "restart" + self.phpVersion
        
            self.disableUwsgi()
            self.auth.executeWithPrivileges(restartScript)
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
		except:
			pass
	
    @objc.IBAction
    def stopNginx_(self, sender):
		try:		
			stopNginx = self.path + "stopNginx"
			self.auth.executeWithPrivileges(stopNginx)
			self.disableUwsgi()
		except:
			pass

    @objc.IBAction
    def startMySQL_(self, sender):
		try:
			startMySQL = self.path + "startMySQL"
			self.auth.executeWithPrivileges(startMySQL)
		except:
			pass
	
    @objc.IBAction
    def stopMySQL_(self, sender):
		try:
			stopMySQL = self.path + "stopMySQL"
			self.auth.executeWithPrivileges(stopMySQL)
		except:
			pass

			
    @objc.IBAction
    def startPHP_(self, sender):
		try:
			self.checkPhpVersion()
			startPHP = self.path + "startPHP" + self.phpVersion

			self.auth.executeWithPrivileges(startPHP)
			self.changeStatusStartButtonALL()
		except:
			pass
	
    @objc.IBAction
    def stopPHP_(self, sender):
		try:
			stopPHP = self.path + "stopPHP" + self.phpVersion
			self.auth.executeWithPrivileges(stopPHP)
		except:
			pass

    @objc.IBAction
    def preferences_(self, sender):
		PreferencesController.show()
	
    @objc.IBAction
    def showPreferencesWindow_(self, sender):
		PreferencesController.show()

    @objc.IBAction
    def exit_(self, sender):
		settings = NSUserDefaults.standardUserDefaults()
		stopMNPP = settings.boolForKey_("stop")
		
		if stopMNPP:
			self.stopServers_(self)

		NSApp().terminate_(self)

    def checkSettings(self):
		settings = NSUserDefaults.standardUserDefaults()
		php54 = settings.boolForKey_("php54")
		php53 = settings.boolForKey_("php53")
		php52 = settings.boolForKey_("php52")
        
		if not php54 and not php53 and not php52:
			settings.setObject_forKey_("1", 'php54')
			settings.setObject_forKey_("0", 'php53')
			settings.setObject_forKey_("0", 'php52')
                
		startMNPP = settings.boolForKey_("start")
		if startMNPP:
			self.startServers_(self)
		
		openMNPP = settings.boolForKey_("open")
		if openMNPP:
			self.startServers_(self)
            

    def checkPhpVersion(self):
		settings = NSUserDefaults.standardUserDefaults()
		php54 = settings.boolForKey_("php54")
		php53 = settings.boolForKey_("php53")
		php52 = settings.boolForKey_("php52")

		if php54:
			self.phpVersion = "54"
		elif php53:
			self.phpVersion = "53"
		else:
			self.phpVersion = "52"

		
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
