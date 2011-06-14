#
#   MenuStatusBar.py
#
#   Created by Jair Gaxiola on 18/05/11.
#   Copyright 2011 __MyCompanyName__. All rights reserved.
#

from Foundation import *
from AppKit import *
import objc
class MenuStatusBar (NSObject):
    @objc.IBAction
	def MenuStart(self, sender):
	    print "funciona"

