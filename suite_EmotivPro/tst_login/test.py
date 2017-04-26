# -*- coding: utf-8 -*-

def main():
    startApplication("emotivpro")
    # login
    mouseClick(waitForObject(":textField_TextField"), 71, 15, Qt.LeftButton)
    mouseClick(waitForObject(":textField_TextField"), 51, 20, Qt.LeftButton)
    type(waitForObject(":textField_TextField"), "chimcu")
    type(waitForObject(":textField_TextField"), "<Tab>")
    type(waitForObject(":textField_TextField_2"), "Thuyvy123")
    mouseClick(waitForObject(":background_Rectangle"), 116, 14, 33554432, Qt.LeftButton)
    snooze(10)
    
    #enter license
    setWindowState(waitForObject(":_QQuickApplicationWindow"), WindowState.Maximize)
    mouseClick(waitForObject(":textField_TextField"), 68, 19, 33554432, Qt.LeftButton)
    type(waitForObject(":textField_TextField"), "1d678e0e-f879-4837-97b7-52dd9f0582e6")
    mouseClick(waitForObject(":background_Rectangle"), 116, 14, 33554432, Qt.LeftButton)
    snooze(15)
    
    #click next for the fit headset screen
    mouseClick(waitForObject(":background_Rectangle_2"), 24, 16, 100663296, Qt.LeftButton)
    doubleClick(waitForObject(":background_Rectangle_2"), 24, 13, 100663296, Qt.LeftButton)
    mouseClick(waitForObject(":background_Rectangle_3"), 143, 26, 100663296, Qt.LeftButton)
    snooze(15)
    
