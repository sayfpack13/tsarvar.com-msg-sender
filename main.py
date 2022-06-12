from multiprocessing import Process
import Tools



login_email="yagexo7394@game4hr.com"
login_pass="1917b5f2"
min_userid=0
max_userid=52886

login_url="https://tsarvar.com/en/login"
chat_url="https://tsarvar.com/en/pm/id"
message_file=open("message.txt","r",encoding="utf8")
message_content=message_file.read().strip()
sended_file=open("sended_users.txt","a")
msg_counter=0
option=0



while True:
    while option<1 or option>2:
        print("1) send messages")
        print("2) Exit")

        option=int(input("Select option: "))

    if option==2:
        break


    msg_count = int(input("How many messages :"))

    Tools.Start(login_url, login_email, login_pass, chat_url, min_userid, max_userid, msg_counter, msg_count,
                sended_file, message_file, message_content)



    option=0



sended_file.close()
message_file.close()



