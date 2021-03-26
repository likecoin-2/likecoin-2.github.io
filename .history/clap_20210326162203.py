from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time 


def clap_html():
    
    likecoin_login_url = "https://like.co/in/register?language=zh&redirect=https%3A%2F%2Flike.co%2Fin%2Foauth%3Flanguage%3Dzh%26client_id%3D8d494f5f203c8bec57f7%26redirect_uri%3Dhttps%253A%252F%252Fliker.land%252Foauth%252Fredirect%26scope%3Dprofile%2520email%2520read%253Alike%2520civic_liker%2520bookmarks%2520follow%2520preferences%26state%3D396024e16df05025%26register%3D1&register=1"
    username_list = ['championfsd@protonmail.com', 'gdsdggfsd@protonmail.com', 'bgfnggh@protonmail.com']
    password_list = ['yuig4796', 'yuig4796', 'yuig4796']

    for username, password in zip(username_list, password_list):
        driver = webdriver.Firefox()
        driver.get(likecoin_login_url)

        driver.switch_to.frame(0)
        time.sleep(10)
        driver.find_element_by_xpath("//a[@class='social-logo social-logo-facebook']").click()

        now_handle = driver.current_window_handle
        all_handles = driver.window_handles  
        #彈出兩個介面,跳轉到不是主窗體介面  
        for handle in all_handles:  
            if handle!=now_handle: 
                driver.switch_to.window(handle)  
                # 密碼輸入
                WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="email"]')))
                elem = driver.find_element_by_id("email")
                elem.send_keys(username)
                time.sleep(2)

                elem = driver.find_element_by_id("pass")
                elem.send_keys(password)
                time.sleep(2)
                elem.send_keys(Keys.RETURN)
                fb_handle = handle
                time.sleep(10)

        driver.switch_to.window(now_handle)      
        driver.switch_to.default_content()
        js = 'window.open("https://likecoin-2.github.io/total");'
        driver.execute_script(js)
        now_handle = driver.current_window_handle
        all_handles = driver.window_handles  
        for handle in all_handles:
            if handle != now_handle and handle != fb_handle:
                driver.switch_to.window(handle) 
        time.sleep(60)
        for i in range(84):
            iframe_id = 'likecoin{}'.format(i)
            driver.switch_to.frame(iframe_id)
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.TAG_NAME, 'button')))
            button_list = driver.find_elements_by_tag_name('button')
            try:
                button_list[2].click()
                button_list[2].click()
                button_list[2].click()
                button_list[2].click()
                button_list[2].click()
            except:
                pass
            driver.switch_to.default_content()

        driver.quit()

if __name__ == "__main__":
    time.sleep(300)
    clap_html()