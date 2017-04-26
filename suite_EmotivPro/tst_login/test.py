# -*- coding: utf-8 -*-

def main():
    startApplication("emotivpro")
    test.compare(str(waitForObjectExists(":Login_Text").text), "Login")
    # login
    mouseClick(waitForObject(":textField_TextField"), 71, 15, Qt.LeftButton)
    
    test.compare(str(waitForObjectExists(":EmotivID_Text").text), "EmotivID")
    test.compare(str(waitForObjectExists(":Password_Text").text), "Password")
    name= "chimcu"
    type(waitForObject(":textField_TextField"), name)
    type(waitForObject(":textField_TextField"), "<Tab>")
    type(waitForObject(":textField_TextField_2"), "Thuyvy123")
    test.compare(str(waitForObjectExists(":Forgot password?_Text").text), "Forgot password?")
    test.compare(str(waitForObjectExists(":Create account_Text").text), "Create account")
    mouseClick(waitForObject(":background_Rectangle"), 116, 14, 33554432, Qt.LeftButton)
    snooze(10)
    
    #enter license
    setWindowState(waitForObject(":_QQuickApplicationWindow"), WindowState.Maximize)
    mouseClick(waitForObject(":textField_TextField"), 68, 19, 33554432, Qt.LeftButton)
    type(waitForObject(":textField_TextField"), "1d678e0e-f879-4837-97b7-52dd9f0582e6")
    mouseClick(waitForObject(":background_Rectangle"), 116, 14, 33554432, Qt.LeftButton)
    snooze(15)
    #check EmotivID on the right conner
    toolbar= ":mToolbar." + name+ "_Text"
    test.compare(str(waitForObjectExists(toolbar).text), name)
    
    test.compare(str(waitForObjectExists(":Fitting your headset correctly_Text").text), "Fitting your headset correctly")
    mouseClick(waitForObject(":NEXT_Text"))
    mouseClick(waitForObject(":NEXT_Text"))
    mouseClick(waitForObject(":NEXT_Text"))
    mouseClick(waitForObject(":DONE_Text"))
    
    
