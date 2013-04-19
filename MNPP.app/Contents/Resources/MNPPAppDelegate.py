#
#  MNPPAppDelegate.py
#  MNPP
#
#  Created by Jair Gaxiola on 02/04/11.
#  Copyright __MyCompanyName__ 2011. All rights reserved.
#

from time import sleep
from Foundation import *
from AppKit import *
from MNPPController import MNPPController

class MNPPAppDelegate(NSObject):
    statusMenu = objc.IBOutlet()
    preferences = objc.IBOutlet()
    step = objc.IBOutlet()

	
    def applicationDidFinishLaunching_(self, sender):
        NSLog("Application did finish launching.")

        self.mnppController = MNPPController.alloc().init()
        self.mnppController.checkSettings()

        statusItem = NSStatusBar.systemStatusBar().statusItemWithLength_(NSVariableStatusItemLength).retain()
        statusItem.setMenu_(self.statusMenu)
        statusItem.setHighlightMode_(YES)
        statusItem.setToolTip_("MNPP: Mac + Nginx + Percona + PHP/Python")
        font = NSFontManager.sharedFontManager().convertFont_toHaveTrait_(NSFont.menuBarFontOfSize_(11), NSBoldFontMask)
        #first row has a high line height to keep the icon vertical centered
        parStyleFirstRow = NSParagraphStyle.defaultParagraphStyle().mutableCopy()
        parStyleFirstRow.setAlignment_(NSCenterTextAlignment)
        parStyleFirstRow.setMinimumLineHeight_(15)
        #second row has low line height to keep the icon compact
        parStyleSecondRow = NSParagraphStyle.defaultParagraphStyle().mutableCopy()
        parStyleSecondRow.setParagraphStyle_(parStyleFirstRow)
        parStyleSecondRow.setMaximumLineHeight_(10)
        #the char \u2009 is a thin space
        title = NSMutableAttributedString.alloc().initWithString_attributes_(u"MN\nP\u2009P", {NSFontAttributeName: font})
        title.addAttribute_value_range_(NSParagraphStyleAttributeName, parStyleFirstRow, NSMakeRange(0,3))
        title.addAttribute_value_range_(NSParagraphStyleAttributeName, parStyleSecondRow, NSMakeRange(3,3))
        statusItem.setAttributedTitle_(title) 
        self.startServers_(self)

    @objc.IBAction
    def showPreferencesWindow_(self, sender):
		self.mnppController.showPreferencesWindow_(self)
		
    @objc.IBAction
    def startServers_(self,sender):
		self.mnppController.startServers_(self)

    @objc.IBAction
    def stopServers_(self,sender):
        self.mnppController.stopServers_(self)

    @objc.IBAction
    def restartServers_(self, sender):
        self.mnppController.restartServers_(self)
            

    @objc.IBAction
    def exit_(self, sender):
		self.mnppController.exit_(self)
