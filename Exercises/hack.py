import csv
import json

#read and compile compromised users& passwords from passwords.csv
compromised_users = []

with open('passwords.csv', 'r') as password_file:
    passwords_csv = csv.DictReader(password_file)

    for line in passwords_csv:
        password_row = line
        print(password_row['Username'])
password_file.close()

with open('compromised_users.txt','w') as compromised_user_file:
     for user in compromised_users:
        compromised_user_file = user
compromised_user_file.close()

#notify 'the boss'
with open('boss_message', 'w') as boss_message:
    boss_message_dict = {"recipient": "The Boss", "message": "Mission Success"}
    json.dump(boss_message_dict, boss_message)
boss_message.close()

with open("new_passwords.csv", 'w') as new_passwords_obj:
    slash_null_sig = """
      _  _     ___   __  ____             
     / )( \   / __) /  \(_  _)            
     ) \/ (  ( (_ \(  O ) )(              
     \____/   \___/ \__/ (__)             
      _  _   __    ___  __ _  ____  ____  
     / )( \ / _\  / __)(  / )(  __)(    \ 
     ) __ (/    \( (__  )  (  ) _)  ) D ( 
     \_)(_/\_/\_/ \___)(__\_)(____)(____/ 
             ____  __     __   ____  _  _ 
      ___   / ___)(  )   / _\ / ___)/ )(  \
     (___)  \___ \/ (_/\/    \ \___ \) __ (
            (____/\____/\_/\_/(____/\_)(_/
      __ _  _  _  __    __                
     (  ( \/ )( \(  )  (  )               
     /    /) \/ (/ (_/\/ (_/\             
     \_)__)\____/\____/\____/
     """
    new_passwords_obj.write(slash_null_sig)
