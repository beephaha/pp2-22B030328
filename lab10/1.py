import csv
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="beepcoder",
    user="postgres",
    password="beep"
)

cursor = conn.cursor()

'''with open('phonebook.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader) # skip the header row
    for row in reader:
        cursor.execute(
            "INSERT INTO phonebook (first_name, last_name, phone_number) VALUES (%s, %s, %s,)",
            row
        )
'''


first_name = input("Enter the first name of the contact: ")
last_name = input("Enter the last name of the contact (optional): ")
phone_number = input("Enter the phone number of the contact: ")

cursor.execute(
    "INSERT INTO phonebook (first_name, last_name, phone_number) VALUES (%s, %s, %s)",
    (first_name, last_name, phone_number)
)

cursor.execute("UPDATE phonebook SET phone_number = %s WHERE first_name = %s", ("123456789", "beep"))

conn.commit()
cursor.close()
conn.close()