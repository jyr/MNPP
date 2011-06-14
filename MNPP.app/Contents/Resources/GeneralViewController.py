#
#   GeneralViewController.py
#
#   Created by Jair Gaxiola on 23/04/11.
#   Copyright 2011 __MyCompanyName__. All rights reserved.
#

from Foundation import *
from AppKit import *
import objc

class GeneralViewController (NSViewController):
	start = objc.IBOutlet()
	stop = objc.IBOutlet()
	open = objc.IBOutlet()
	nginxPort = objc.IBOutlet()
	mysqlPort = objc.IBOutlet()
	phpPort = objc.IBOutlet()
	
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

		"""
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
		"""
		settings.synchronize()
	



