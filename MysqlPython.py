import time
from re import A
import mysql.connector
from mysql.connector.constants import MAX_MYSQL_TABLE_COLUMNS
import sys
import os
import json

from mysql.connector.errors import InterfaceError, ProgrammingError



print("\n",
"\033[1;32;40m███╗   ███╗██╗   ██╗███████╗ ██████╗ ██╗\n",     
"\033[1;32;40m████╗ ████║╚██╗ ██╔╝██╔════╝██╔═══██╗██║\n",     
"\033[1;32;40m██╔████╔██║ ╚████╔╝ ███████╗██║   ██║██║\n",     
"\033[1;32;40m██║╚██╔╝██║  ╚██╔╝  ╚════██║██║▄▄ ██║██║\n",     
"\033[1;32;40m██║ ╚═╝ ██║   ██║   ███████║╚██████╔╝███████╗\n",
"\033[1;32;40m╚═╝     ╚═╝   ╚═╝   ╚══════╝ ╚══▀▀═╝ ╚══════╝\n"
"\033[1;31;40mScript made by kastor",
"\n")

def abelardoAsc():
  print("\n"               
  "      ___\n"
  "    .'``.``.\n"
  " __/ (o) `, `.\n"
  "'-=`,     ;   `.\n"
  "    \    :      `-.\n"
  "    /    ';        `.\n"
  "   /      .'         `.\n"
  "   |     (      `.     `-.._\n"
  "    \     \` ` `. \         `-.._\n"
  "     `.   ;`-.._ `-`._.-. `-._   `-._\n"
  "       `..'     `-.```.  `-._ `-.._.'\n"
  "         `--..__..-`--'      `-.,'\n"
  "            `._)`/\n"
  "             /--(\n"
  "          -./,--'`-,\n"
  "       ,^--(\n"                    
  "       ,--' `-,\n"
  "\n"
  "This is Abelardo\n")
  mainMenu()


def changeCredentials(): 
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

def setConnection():
  
  if os.path.getsize("database.txt") == 0 :
    changeCredentials()
  else:
    connectServer()
    
def checkCredentials():
  print("\nChecking credentials...")
  time.sleep(2)
  file = open("database.txt","r")
  fileContent = file.readlines()
  print("Server ip: " + fileContent[0] +"" + "Username: " + fileContent[1] +"" + "Password: " + fileContent[2] +"" + "Table: " + fileContent[3] +"")
  changeCredentials = input("Do you want to change the credentials? y/n")
  if changeCredentials == "y" :
    changeCredentials()
  elif changeCredentials == "n" :
    exitScript() 
  elif changeCredentials == "" or changeCredentials != "y" or changeCredentials != "n":
    print("Enter a valid answer")
    chooseAnOption()  
  file.close()   

def connectServer(): 
 Attempts = 10
 while Attempts > 0: 
  try: 
    file = open("database.txt","r")
    fileContent = file.readlines()
    passwordstr = str(fileContent[2])
    
    if len(passwordstr) == 1:
      passwordstr = ("")

    mydb = mysql.connector.connect(
    host=fileContent[0],
    user=fileContent[1],
    password= passwordstr,
    database=fileContent[3])
    
    mycursor = mydb.cursor()
    print("\nConnecting...")
    time.sleep(2)
    print("Connection successfull!!\n")
    time.sleep(1)
    mainMenu()
    break
  except InterfaceError:
    print("Couldn't connect to the server trying again... (" + str(Attempts) + " attemtps remaining)")
    Attempts = Attempts -1
    if Attempts == 0 :
      time.sleep(1)
      chooseAnOption()
      
        

def createTables():
  
  table_name = input("Enter a table name: ")
  if table_name != "":
   
    while True:
        try:
            file = open("database.txt","r")
            fileContent = file.readlines()
            passwordstr = str(fileContent[2])
            
            if len(passwordstr) == 1:
              passwordstr = ("")

            mydb = mysql.connector.connect(
            host=fileContent[0],
            user=fileContent[1],
            password= passwordstr,
            database=fileContent[3])
            
            mycursor = mydb.cursor()
            query =  "CREATE TABLE " + table_name + """(name VARCHAR(255), address VARCHAR(255))"""
            mycursor.execute(query)
            print("table created")
            break
        except ProgrammingError: 
            print ("Table name already exists, choose another one")
            createTables()
            
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
  elif option == 666:
    abelardoAsc()
    
def chooseAnOption():
  checkServerInfo = input("\n¿Do you want to check the server credentials y/n?: ")
  if checkServerInfo == "y" :
    checkCredentials()
  elif checkServerInfo == "n" :
    exitScript() 
  elif checkServerInfo == "" or checkServerInfo != "y" or checkServerInfo != "n":
    print("Enter a valid answer")
    chooseAnOption()  

mainMenu()