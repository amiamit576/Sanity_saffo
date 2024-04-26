import time
from appium.webdriver.common.appiumby import  AppiumBy
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from datetime import datetime


class Short_call :


    #ac_id=acessbility_id,xp=xpath
    phn_Ac_id='Phone'
    recent_xp='//android.view.View[@resource-id="com.google.android.dialer:id/navigation_bar_item_active_indicator_view"]'
    keypad_xp='//android.widget.ImageButton[@content-desc="key pad"]'
    phn_no_enter_xp='//android.widget.EditText[@resource-id="com.google.android.dialer:id/digits"]'


    # after iteration
    callbtn_xp = '//android.widget.Button[@content-desc="dial"]'
    calltimer_Xp='//android.widget.Chronometer[@resource-id="com.google.android.dialer:id/contactgrid_bottom_timer"]'
    num_callbtn_xp='//android.widget.ImageView[@resource-id="com.google.android.dialer:id/call_button"]'
    end_call_xp='//android.widget.Button[@content-desc="End call"]'







    def __init__(self,driver):
        self.driver=driver






    def make_call(self,num):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID,self.phn_Ac_id).click()
        self.driver.find_element(AppiumBy.XPATH,self.recent_xp).click()
        self.driver.find_element(AppiumBy.XPATH,self.keypad_xp).click()
        self.driver.find_element(AppiumBy.XPATH,self.phn_no_enter_xp).send_keys(num)


    def sucess_call(self,n):
        WAIT_CALL=WebDriverWait(self.driver,30)
        call_drop=0
        call_sucess=0
        # Generate timestamp


        for  i in range(n):
            timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

            try:
                self.driver.find_element(AppiumBy.XPATH,self.num_callbtn_xp).click()
            except:
                self.driver.find_element(AppiumBy.XPATH,self.callbtn_xp).click()
            try:
                WAIT_CALL.until(Ec.visibility_of_element_located((AppiumBy.XPATH,self.calltimer_Xp)))
                try:
                    WAIT_CALL.until(Ec.visibility_of_element_located((AppiumBy.XPATH,self.recent_xp)))
                    call_drop +=1
                    print("Call Drop--->",call_drop,timestamp)

                    self.driver.get_screenshot_as_file(f'.\\ScreenShot\\drop_{timestamp}.png')
                    time.sleep(2)
                    continue
                except:
                    pass

                self.driver.find_element(AppiumBy.XPATH,self.end_call_xp).click()
                call_sucess +=1
                print("call sucess -->",call_sucess)
            except:
                print("Call Block or not reccived by recciver")
                continue

        print("Call Drop  total count--->", call_drop)
        self.driver.back()
        print("call sucess  total count-->", call_sucess)


















    
