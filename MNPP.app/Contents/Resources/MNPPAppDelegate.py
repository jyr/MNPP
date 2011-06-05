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
    statusMenu = objc.IBOutlet()
    startButton = objc.IBOutlet()
    stopButton = objc.IBOutlet()
    startNginx = objc.IBOutlet()
    stopNginx = objc.IBOutlet()
    startMySQL = objc.IBOutlet()
    stopMySQL = objc.IBOutlet()
    startPHP = objc.IBOutlet()
    stopPHP = objc.IBOutlet()
    preferences = objc.IBOutlet()
    step = objc.IBOutlet()

	
    def applicationDidFinishLaunching_(self, sender):
        NSLog("Application did finish launching.")

        print self.statusMenu.indexOfItemWithTitle_("Start nginx")
        self.mnppController = MNPPController.alloc().init()
        self.mnppController.showWindow_(self)
        self.mnppController.checkSettings()

    #def awakeFromNib(self):		
        statusItem = NSStatusBar.systemStatusBar().statusItemWithLength_(NSVariableStatusItemLength).retain()
        statusItem.setMenu_(self.statusMenu)
        statusItem.setTitle_("MNPP")
        statusItem.setHighlightMode_(YES)

    @objc.IBAction
    def showPreferencesWindow_(self, sender):
		self.mnppController.showPreferencesWindow_(self)
		
    @objc.IBAction
    def startServers_(self,sender):
		self.changeStatusStartMenuALL()
		self.startNginx.setHidden_(YES)
		self.stopNginx.setHidden_(NO)
		self.startMySQL.setHidden_(YES)
		self.stopMySQL.setHidden_(NO)
		self.startPHP.setHidden_(YES)
		self.stopPHP.setHidden_(NO)
		
		self.mnppController.startServers_(self)

    @objc.IBAction
    def stopServers_(self,sender):
		self.changeStatusStopMenuALL()
		self.startNginx.setHidden_(NO)
		self.stopNginx.setHidden_(YES)
		self.startMySQL.setHidden_(NO)
		self.stopMySQL.setHidden_(YES)
		self.startPHP.setHidden_(NO)
		self.stopPHP.setHidden_(YES)

		self.mnppController.stopServers_(self)

    @objc.IBAction
    def startNginx_(self,sender):
		self.changeStatusStartMenuALL()
		self.startNginx.setHidden_(YES)
		self.stopNginx.setHidden_(NO)
		self.mnppController.startNginx_(self)

    @objc.IBAction
    def stopNginx_(self, sender):
		self.changeStatusStopMenuALL()
		self.stopNginx.setHidden_(YES)
		self.startNginx.setHidden_(NO)
		self.mnppController.stopNginx_(self)
		
    @objc.IBAction
    def startMySQL_(self, sender):
		self.changeStatusStartMenuALL()
		self.startMySQL.setHidden_(YES)
		self.stopMySQL.setHidden_(NO)
		self.mnppController.startMySQL_(self)

    @objc.IBAction
    def stopMySQL_(self, sender):
		self.changeStatusStopMenuALL()
		self.startMySQL.setHidden_(YES)
		self.stopMySQL.setHidden_(NO)
		self.mnppController.stopMySQL_(self)

    @objc.IBAction
    def startPHP_(self, sender):
		self.changeStatusStartMenuALL()
		self.startPHP.setHidden_(YES)
		self.stopPHP.setHidden_(NO)
		self.mnppController.startPHP_(self)

    @objc.IBAction
    def stopPHP_(self, sender):
		self.changeStatusStopMenuALL()
		self.stopPHP.setHidden_(YES)
		self.startPHP.setHidden_(NO)
		self.mnppController.stopPHP_(self)

    @objc.IBAction
    def exit_(self, sender):
		self.mnppController.exit_(self)

    def changeStatusStartMenuALL(self):
		self.startButton.setHidden_(YES)
		self.stopButton.setHidden_(NO)
		print "start menuall"
	
    def changeStatusStopMenuALL(self):
		self.startButton.setHidden_(NO)
		self.stopButton.setHidden_(YES)
		print "stop menuall"