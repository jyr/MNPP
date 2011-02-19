#
#  MEPPAppDelegate.py
#  MEPP
#
#  Created by Jair Gaxiola on 16/02/11.
#  Copyright __MyCompanyName__ 2011. All rights reserved.
#

from Foundation import *
from AppKit import *
from MEPPController import MEPPController

class MEPPAppDelegate(NSObject):
    def applicationDidFinishLaunching_(self, sender):
        NSLog("Application did finish launching.")

        self.meppController = MEPPController.alloc().init()
        self.meppController.showWindow_(self)
        self.meppController.checkSettings()
