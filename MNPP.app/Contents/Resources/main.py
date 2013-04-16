#
#  main.py
#  MNPP
#
#  Created by Jair Gaxiola on 02/04/11.
#  Copyright __MyCompanyName__ 2011. All rights reserved.
#

#import modules required by application
import objc
import Foundation
import AppKit
import sys
sys.path.append("/Applications/MNPP/Library")

from PyObjCTools import AppHelper

# import modules containing classes required to start application and load MainMenu.nib
import MNPPController
import PreferencesController
import GeneralViewController
import PhpViewController
import MNPPAppDelegate

# pass control to AppKit
AppHelper.runEventLoop()

