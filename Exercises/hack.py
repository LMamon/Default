import csv

compromised_users = []

with open('passwords.csv', 'r') as password_file:
    passwords_csv = csv.DirectReader(password_file)

    for line in password_csv:
        password_row = line
        print(password_row['Username'])