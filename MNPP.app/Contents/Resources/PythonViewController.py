#
#   PythonViewController.py
#
#   Created by Jair Gaxiola on 09/06/11.
#   Copyright 2011 __MyCompanyName__. All rights reserved.
#

from Foundation import *
from AppKit import *
import objc
class PythonViewController (NSViewController):
	uwsgi = objc.IBOutlet()

	@objc.IBAction
	def savePreferences_(self, sender):
		settings = NSUserDefaults.standardUserDefaults()
		
		if self.uwsgi.state():
			settings.setObject_forKey_(1, 'uwsgi')
		else:
			settings.setObject_forKey_(0, 'uwsgi')
		print "python preferences"

