import random
import time
import os
from selenium.webdriver.common.by import By
import WebDriver


def Login(driver,login_url,login_email,login_pass):
    driver.get(login_url)

    email_field = driver.find_element(By.NAME, "email")
    email_field.send_keys(login_email)

    pass_field = driver.find_element(By.NAME, "psw")
    pass_field.send_keys(login_pass)

    login_btn = driver.find_element(By.CSS_SELECTOR, ".loginForm-authSubmit")
    login_btn.click()

    time.sleep(2)

    # check login
    try:
        profile_field = driver.find_element(By.CSS_SELECTOR, ".userPage-title")
        print("loggedin !!")
    except:
        print("can't login !!")
        exit()



def Send_messages(driver,chat_url,min_userid,max_userid,msg_counter,msg_count,sended_file,message_content):

    sended_file.writelines("\n============= NEW JOB =============\n")
    while msg_counter < msg_count:
        userid = random.randrange(min_userid, max_userid)
        driver.get(chat_url + str(userid))

        # check if user exit
        try:
            error_field = driver.find_element(By.CSS_SELECTOR, ".iconStyle-img")
            print("user not found !!")
            continue

        except:
            print("messaging user: " + str(userid))

            message_field = driver.find_element(By.CSS_SELECTOR, ".chatWin-inputTextarea")
            message_field.send_keys(message_content)

            send_btn = driver.find_element(By.CSS_SELECTOR, ".chatWin-inputSubmit")
            send_btn.click()

            
            
            msg_counter += 1
            sended_file.writelines(str(userid) + "\n")
            print("messages sended: "+str(msg_counter)+" ("+str((msg_counter / msg_count)*100)+"%)")

            if msg_counter%10==0:
                cls()
            pass

    sended_file.write("============= JOB DONE =============\n")
    print("============= JOB DONE =============")


def Start(login_url,login_email,login_pass,chat_url,min_userid,max_userid,msg_counter,msg_count,sended_file,message_file,message_content):
    # START HERE
    driver_options = WebDriver.SetupWebDriverOptions(True)
    driver = WebDriver.SetupWebDriver(driver_options, "windows")

    Login(driver, login_url, login_email, login_pass)
    Send_messages(driver,chat_url,min_userid,max_userid,msg_counter,msg_count,sended_file,message_content)

def cls():
    os.system('cls' if os.name=='nt' else 'clear')