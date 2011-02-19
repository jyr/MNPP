#
#  main.py
#  MEPP
#
#  Created by Jair Gaxiola on 16/02/11.
#  Copyright __MyCompanyName__ 2011. All rights reserved.
#

#import modules required by application
import objc
import Foundation
import AppKit

from PyObjCTools import AppHelper

import sys
sys.path.append("/Applications/MEPP/Library")

# import modules containing classes required to start application and load MainMenu.nib
import MEPPController
import MEPPAppDelegate


# pass control to AppKit
AppHelper.runEventLoop()
