import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="localnav",
    passwd="",
    database="minorproject"
)
#creating a cursor object using the cursor() method
mycursor = mydb.cursor()

#storing table names in a list
mycursor.execute("SHOW TABLES")
table_names = [x[0] for x in mycursor]
print(table_names)

#assigning variables to the table final_minor
finally_minor = "`final_minor - sheet1`"

#select all the rows from the table final_minor
mycursor.execute("select * from `final_minor - sheet1`" )
myresult = mycursor.fetchall()



#taking a country name as input
country = input("Enter a country name: ")


#selecting the rows from the table final_minor where the country name is equal to the input
mycursor.execute("select * from `final_minor - sheet1` where country = %s", (country,))

#fetching the result
mycountryresult = mycursor.fetchall()

#displaying the result
print(mycountryresult)

