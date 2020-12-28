from selenium import webdriver
import win32api, win32con, time
import unittest
import type_text as keyboard
 
 
# Facebook user's language must be set to English (US)
 
def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    time.sleep(3)
 
 
facebook_page = 'https://www.facebook.com/II-Cita-de-Presidentes-Salinas-2018-393653087809501'
facebook = 'https://www.facebook.com/'
 
emails = ['lima.paguay.lenin@cenecuador.edu.ec']
passwords = ['Interoc2022']
 
 
class GetAttributeTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get('https://facebook.com/')
 
    def test_GetAttribute(self):
        for index in range(0, len(emails)):
            driver = self.driver
 
            print('User enters email "%s", password "%s" and clicks on "Login" button' % (emails[index], passwords[index]))
            email = driver.find_element_by_id('email')
            email.send_keys('%s' % emails[index])
            password = driver.find_element_by_id('pass')
            password.send_keys('%s' % passwords[index])
            driver.find_element_by_id('loginbutton').click()
            time.sleep(3)
 
            print('User clicks on "Allow" button (allow facebook to show notifications)')
            click(275, 160)
            time.sleep(3)
            print('User goes to facebook page (%s)' % facebook_page)
            driver.get(facebook_page)
            time.sleep(4)
            print('User clicks on "Invite friends to like this Page" text')
            driver.find_element_by_link_text('Invite friends to like this Page').click()
            time.sleep(7)
            print('User clicks in the middle of "Invite your friends to like ..." window')
            click(1000, 540)
            time.sleep(3)
            times = 1200
            print('User presses down button for %s times to get to the bottom of friends list' % times)
            for l in range(0, times):
                keyboard.Press('DOWN')
            try:
                print('User clicks on all "Invite" buttons')
                for button_index in range(0, 1200):
                    if driver.find_elements_by_css_selector('span.uiButtonText'):
                        driver.find_elements_by_css_selector('span.uiButtonText')[button_index].click()
                        time.sleep(.7)
                    else:
                        pass
            except:
                pass
            print('User goes facebook main page')
            driver.get(facebook)
            time.sleep(3)
            print('User clicks on triangle next to settings so that drop down menu is displayed')
            driver.find_element_by_id('pageLoginAnchor').click()
            time.sleep(3)
            print('User clicks on "Log Out" text')
            driver.find_element_by_link_text('Log Out').click()
            time.sleep(3)
            print('Actions completed with: %s' % emails[index])
 
    if __name__ == '__main__':
        unittest.main()
      