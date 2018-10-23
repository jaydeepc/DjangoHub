import csv
import MySQLdb

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='',
    db='openhub')
cursor = mydb.cursor()

with open('data.csv', newline='') as datafile:
    reader = csv.DictReader(datafile)
    for row in reader:

        list = [row['First name'], row['Last name'], row['Github username (If the project is on Git)'], "India", row['Your home office']]

        cursor.execute("INSERT INTO openhub_contributors(user_firstname, user_lastname, git_username, country, office ) VALUES(%s, %s, %s, %s, %s) WHERE NOT EXISTS (SELECT name FROM table_listnames WHERE name = '{0}'".format(row['First name']),
            list)

    mydb.commit()
    cursor.close()
    print("Done")