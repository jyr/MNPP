#
#   PreferencesController.py
#
#   Created by Jair Gaxiola on 15/01/11.
#   Copyright 2011 __MyCompanyName__. All rights reserved.
#

from Foundation import *
from AppKit import *
from Authorization import Authorization

import objc

class PreferencesController (NSWindowController):
	start = objc.IBOutlet()
	stop = objc.IBOutlet()
	open = objc.IBOutlet()
	nginxPort = objc.IBOutlet()
	mysqlPort = objc.IBOutlet()
	phpPort = objc.IBOutlet()

	def init(self):
		self.initWithWindowNibName_("Preferences")
		
		return self
	
	def windowDidLoad(self):
		self.setSettings()

	def show(self):
		self.preferencesController = PreferencesController.alloc().init()
		self.preferencesController.showWindow_(self)

	show = classmethod(show)
	
	def setSettings(self):
		settings = NSUserDefaults.standardUserDefaults()
		
		startMEMP = settings.boolForKey_("start")

		if startMEMP:
			self.start.setState_(NSOnState)
		else:
			self.start.setState_(NSOffState)

		stopMEMP = settings.boolForKey_("stop")

		if stopMEMP:
			self.stop.setState_(NSOnState)
		else:
			self.stop.setState_(NSOffState)
			
		openMEMP = settings.boolForKey_("open")

		if openMEMP:
			self.open.setState_(NSOnState)
		else:
			self.open.setState_(NSOffState)
		
		nginxPort = settings.stringForKey_("nginxPort")

		if nginxPort:
			self.nginxPort.setStringValue_(nginxPort)

		mysqlPort = settings.stringForKey_("mysqlPort")

		if mysqlPort:
			self.mysqlPort.setStringValue_(mysqlPort)
		
		phpPort = settings.stringForKey_("phpPort")

		if phpPort:
			self.phpPort.setStringValue_(phpPort)
			
	@objc.IBAction
	def savePreferences_(self, sender):
		settings = NSUserDefaults.standardUserDefaults()
		
		if self.start.state():
			settings.setObject_forKey_(1, 'start')
		else:
			settings.setObject_forKey_(0, 'start')
		
		if self.stop.state():
			settings.setObject_forKey_(1, 'stop')
		else:
			settings.setObject_forKey_(0, 'stop')
		
		if self.open.state():
			settings.setObject_forKey_(1, 'open')
		else:
			settings.setObject_forKey_(0, 'open')

		if self.nginxPort.stringValue():
			settings.setObject_forKey_(self.nginxPort.stringValue(), 'nginxPort')
		else:
			settings.setObject_forKey_("80", 'nginxPort')
		
		if self.mysqlPort.stringValue():
			settings.setObject_forKey_(self.mysqlPort.stringValue(), 'mysqlPort')
		else:
			settings.setObject_forKey_("3306", 'mysqlPort')
		
		if self.phpPort.stringValue():
			settings.setObject_forKey_(self.phpPort.stringValue(), 'phpPort')
		else:
			settings.setObject_forKey_("9000", 'phpPort')
		
		settings.synchronize()
		

