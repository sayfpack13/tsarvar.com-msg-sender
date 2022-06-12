import Tools
import WebDriver


login_email="yagexo7394@game4hr.com"
login_pass="1917b5f2"
min_userid=0
max_userid=52886

login_url="https://tsarvar.com/en/login"
chat_url="https://tsarvar.com/en/pm/id"
message_file=open("message.txt","r",encoding="utf8")
message_content=message_file.read().strip()
sended_file=open("sended_users.txt","a")




option=0

while True:
    while option<1 or option>2:
        print("1) send messages")
        print("2) Exit")

        option=int(input("Select option: "))

        if option==2:
            exit()

    msg_count = int(input("How many messages: "))

    # START HERE
    driver_options = WebDriver.SetupWebDriverOptions(False)
    driver = WebDriver.SetupWebDriver(driver_options, "windows")

    Tools.Login(driver, login_url, login_email, login_pass)
    Tools.Send_messages(driver,chat_url,min_userid,max_userid,msg_count,sended_file,message_file,message_content)

    option=0




