#
#   PreferencesController.py
#
#   Created by Jair Gaxiola on 15/01/11.
#   Copyright 2011 __MyCompanyName__. All rights reserved.
#

from Foundation import *
from AppKit import *
from Authorization import Authorization
from GeneralViewController import GeneralViewController
from PhpViewController import PhpViewController

import objc

class PreferencesController (NSWindowController):
	preferencesView = objc.IBOutlet()
	
	def show(self):
		try:
			if self.PreferencesController:
				self.PreferencesController.close()
		except:
			pass

		self.PreferencesController = NSWindowController.alloc().initWithWindowNibName_("Preferences")
		self.PreferencesController.showWindow_(self)
		self.PreferencesController.retain()
		self.PreferencesController.window().center()
		self.preferencesView = self.PreferencesController.window().contentView()
		
		self.GeneralController = GeneralViewController.alloc().initWithNibName_bundle_("General", None)
		self.generalView = self.GeneralController.view()
		self.preferencesView.addSubview_(self.generalView)
		
		self.PhpController = PhpViewController.alloc().initWithNibName_bundle_("Php", None)

		self.setSettings(self)
		print dir(self.PreferencesController)
		
	show = classmethod(show)	
	
	def setSettings(self):		
		settings = NSUserDefaults.standardUserDefaults()

		startMNPP = settings.boolForKey_("start")

		if startMNPP:
			self.GeneralController.start.setState_(NSOnState)
		else:
			self.GeneralController.start.setState_(NSOffState)

		stopMNPP = settings.boolForKey_("stop")

		if stopMNPP:
			self.GeneralController.stop.setState_(NSOnState)
		else:
			self.GeneralController.stop.setState_(NSOffState)
			
		openMNPP = settings.boolForKey_("open")

		if openMNPP:
			self.GeneralController.open.setState_(NSOnState)
		else:
			self.GeneralController.open.setState_(NSOffState)
		
		php53 = settings.boolForKey_("php53")
		
		if php53:
			try:
				self.PhpController.php53.setState_(NSOnState)
				self.PhpController.php52.setState_(NSOffState)
			except:
				pass

		php52 = settings.boolForKey_("php52")

		if php52:
			try:
				self.PhpController.php52.setState_(NSOnState)
				self.PhpController.php53.setState_(NSOffState)
			except:
				pass
		
		"""
		nginxPort = settings.stringForKey_("nginxPort")

		if nginxPort:
			self.GeneralController.nginxPort.setStringValue_(nginxPort)

		mysqlPort = settings.stringForKey_("mysqlPort")

		if mysqlPort:
			self.GeneralController.mysqlPort.setStringValue_(mysqlPort)
		
		phpPort = settings.stringForKey_("phpPort")

		if phpPort:
			self.GeneralController.phpPort.setStringValue_(phpPort)
		"""
	
	def resetSubviews(self):
		for i in range(1, len(self.preferencesView.subviews())):
			self.preferencesView.subviews().removeObjectAtIndex_(i)
	
	@objc.IBAction
	def general_(self, sender):
		self.resetSubviews()
		self.generalView = self.GeneralController.view()
		self.preferencesView.addSubview_(self.generalView)
		
		self.setSettings()
	
	@objc.IBAction
	def php_(self, sender):
		self.resetSubviews()
		self.phpView = self.PhpController.view()
		self.preferencesView.addSubview_(self.phpView)
		
		self.setSettings()