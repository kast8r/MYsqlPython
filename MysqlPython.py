import time
from re import A
import mysql.connector
from mysql.connector.constants import MAX_MYSQL_TABLE_COLUMNS
import sys
import os
from playsound import playsound
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
#playsound("intro.wav")


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
  playsound('bird.wav')
  time.sleep(9)
  mainMenu()

def mainConnect():
    file = open("database.txt","r")
    fileContent = file.readlines()
    passwordstr = str(fileContent[2])
    
    if len(passwordstr) == 1:
      passwordstr = ("")

    mainConnect.mydb = mysql.connector.connect(
    host=fileContent[0],
    user=fileContent[1],
    password= passwordstr,
    database=fileContent[3])
    
    mainConnect.mycursor = mainConnect.mydb.cursor()
def returnToMainMenu():
  answer = print("¿Do you want to return to main menu? y/n: ")
  if answer == "y":
    mainMenu()
  elif answer == "n":
    exitScript()
  elif  answer == "" or answer != "y" or answer != "n":
    print("Please enter a valid answer, y or n\n")
    time.sleep(1)
    returnToMainMenu()

    
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
  credentials = input("Do you want to change the credentials y/n?: ")
  if credentials == "y" :
    changeCredentials()
  elif credentials == "n" :
    exitToMenut() 
  elif credentials == "" or credentials != "y" or credentials != "n":
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
    time.sleep(1)
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
            

            query =  ("CREATE TABLE " + table_name + "(id int NOT NULL AUTO_INCREMENT, PRIMARY KEY (id));""") 
            
            try:
              numberOfColumns = int(input("¿How many columns do you want?: "))
            except ValueError:
              print("You have to enter a valid number")
              createTables()
            mycursor.execute(query)

            while numberOfColumns > 0:
              columnName = str(input("Name for the column number " + str(numberOfColumns) + ": "))
              query2 = ("""ALTER TABLE """ + table_name + """ ADD COLUMN """ + columnName + """ VARCHAR(255);""")

              mycursor.execute(query2)
              
              numberOfColumns= numberOfColumns-1
              if numberOfColumns == 0:
                print("\nThe table and columns were successfully created\n \nReturning to main menu...\n")
                time.sleep(2)
                mainMenu()
                break 
            
            
        except ProgrammingError: 
            print ("Something went wrong, trying again...")
            createTables()
            
  else:
      print("Please enter a corret name for the table")

def createDabatase():
  print("Creating")
def listTables():
  mainConnect()
  query = ("SHOW TABLES;")
  mainConnect.mycursor.execute(query)
  
  def listTablesOptions():
    choose = input("¿Do you want to see the tables slowly(1) or in a shot(2)? 1/2: ")
    if choose == "1":
      print("listing...\n")
      time.sleep(2)
      for x in mainConnect.mycursor:
          time.sleep(.50)
          print(x)
        #TODO solve the for
      returnToMainMenu()
    elif choose == "2":
      print("listing...\n")
      time.sleep(2)

      for x in mainConnect.mycursor:
        print(x) 
      returnToMainMenu() 
    elif choose == "" or choose != "1" or choose != "2":   
      print("Please give a valid answer 1 or 2")
      listTablesOptions()

  listTablesOptions()

def exitScript():
  print("exiting...")
  time.sleep(1)
  print("Have a nice day :)")
  time.sleep(1)
  exit()
def exitToMenut():
  print("Exiting to menu...\n")
  time.sleep(1)
  mainMenu()



def mainMenu():
  print(" 1. To connect to a MYsql server\n",
  
        "2. To create new databases\n",
        "3. To create new tables\n",
        "4. To list all tables\n",
        "5. To change credentials\n",
        "6. Exit\n")
  option = int(input("Chose an option between (1-6): "))


  if option == 1:
    playsound('click.wav')
    setConnection()
  elif option == 2:
    playsound('click.wav')
    createDabatase()
  elif option == 3:
    playsound('click.wav')
    createTables()
  elif option == 4:
    playsound('click.wav')
    listTables()
  elif option == 5:
    playsound('click.wav')
    checkCredentials()
  elif option == 6:
    playsound('click.wav')
    exitScript()
  elif option == 666:
    playsound('click.wav')
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