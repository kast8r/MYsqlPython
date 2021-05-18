import time
from re import A
import mysql.connector
from mysql.connector.constants import MAX_MYSQL_TABLE_COLUMNS
import sys
import os
import json

from mysql.connector.errors import InterfaceError




print("\n",
"███╗   ███╗██╗   ██╗███████╗ ██████╗ ██╗\n",     
"████╗ ████║╚██╗ ██╔╝██╔════╝██╔═══██╗██║\n",     
"██╔████╔██║ ╚████╔╝ ███████╗██║   ██║██║\n",     
"██║╚██╔╝██║  ╚██╔╝  ╚════██║██║▄▄ ██║██║\n",     
"██║ ╚═╝ ██║   ██║   ███████║╚██████╔╝███████╗\n",
"╚═╝     ╚═╝   ╚═╝   ╚══════╝ ╚══▀▀═╝ ╚══════╝\n"
"Script made by kastor",
"\n")



def setConnection():
  

  
  if os.path.getsize("database.txt") == 0 :
    file = open("database.txt","w")
    hostIp = input("Give a server ip: ")
    file.write(hostIp + "\n")

    user = input("Username: ")
    file.write(user + "\n")

    password = input("Password: ")
    file.write(password + "\n")

    database = input("Give a database name: ")
    file.write(database + "\n")
    file.close()
  else:
    connectServer()
    
    

def connectServer(): 
 while True: 
  try: 
    file = open("database.txt","r")
    fileContent = file.readlines()
    passwordstr = str(fileContent[2])
    
    if len(passwordstr) < 2:
      passwordstr = ("")

    mydb = mysql.connector.connect(
    host=fileContent[0],
    user=fileContent[1],
    password= passwordstr,
    database=fileContent[3])
    
    mycursor = mydb.cursor()
    print("Connection successfull")
    
    break
  except InterfaceError:
    print("Couldn't connect to the server trying again...")
    

def createTables():
  table_name = input("Enter a table name: ")
  if table_name != "":
      while True:
        try:
            query =  "CREATE TABLE " + table_name + """(name VARCHAR(255), address VARCHAR(255))"""
            mycursor.execute(query)
            print("table created")
        except:
              print ("Table name already exists")
            
  else:
      print("Please enter a corret name for the table")

def createDabatase():
  print("Creating")
def listTables():
  print("listing")
def exitScript():
  print("exiting...")
  time.sleep(1)
  print("Have a nice day :)")
  time.sleep(1)
  exit()



def mainMenu():
  print(" 1. To connect to a MYsql server\n",
        "2. To create new databases\n",
        "3. To create new tables\n",
        "4. To list all tables\n",
        "5. Exit\n")
  option = int(input("Chose an option between (1-5): "))


  if option == 1:
    setConnection()
  elif option == 2:
    createDabatase()
  elif option == 3:
    createTables()
  elif option == 4:
    listTables()
  elif option == 5:
    exitScript()
  

mainMenu()