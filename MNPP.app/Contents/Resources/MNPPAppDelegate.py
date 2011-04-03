#
#  MNPPAppDelegate.py
#  MNPP
#
#  Created by Jair Gaxiola on 02/04/11.
#  Copyright __MyCompanyName__ 2011. All rights reserved.
#

from Foundation import *
from AppKit import *
from MNPPController import MNPPController

class MNPPAppDelegate(NSObject):
    def applicationDidFinishLaunching_(self, sender):
        NSLog("Application did finish launching.")
		
        self.mnppController = MNPPController.alloc().init()
        self.mnppController.showWindow_(self)
        self.mnppController.checkSettings()