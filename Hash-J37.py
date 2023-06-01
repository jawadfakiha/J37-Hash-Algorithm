#!/usr/bin/python3

import random
import string

Pepper = "TUWAIQACADEMY-J37"

def generateRandomSalt():
    
    saltLength = 8   
    
    saltCharacters = string.ascii_letters + string.digits
    Salt = ''.join(random.choice(saltCharacters) for i in range(saltLength))
    
    return Salt
    
# this function generate random 8 characters to make a random salt


    
def J37HashFunction(Password,Salt):
    
    hashValue = 456357
    
    pepperedPassword = Password + Pepper
    saltedPassword = pepperedPassword + Salt
    
    for char in saltedPassword :
    
        asciiValue = ord(char)
        hashValue ^= asciiValue
    
    return hashValue
    
# this is the simple hashing algorithm consists of generating a random initial value for the hash
# then will add the pepper to the password and after that we will add the random generated salt also
# after that for every character in the password we will get an integer representing that unicode character
# and then we will do a simple bitwise XOR operation between the random initial hash value and the integers
    
def userRegestration():

    Username = input("\nEnter a Username : ")
    Password = input("Enter a Password : ")
    
    try :
    
        with open("userRecords.txt","r") as file :
            checkUser = file.readlines()
    
            for userRecord in checkUser :
                usernameRecord, _ , _ = userRecord.strip().split(":")
                if usernameRecord == Username :
                    print("\n[*] Username Already Exists !\n")
                    return
                    
    except FileNotFoundError :
        
        Salt = generateRandomSalt()
        hashedPassword = J37HashFunction(Password,Salt)
        
        with open("userRecords.txt","a") as file :
            file.write(f"{Username}:{hashedPassword}:{Salt}\n")
            
        print("\n[*] Successfuly Registered !\n")
    
        return
    
    Salt = generateRandomSalt()
    hashedPassword = J37HashFunction(Password,Salt)
    
    with open("userRecords.txt","a") as file :
        file.write(f"{Username}:{hashedPassword}:{Salt}\n")
        
    print("\n[*] Successfuly Registered !\n")
    
# this is our user regestration function
    
def userAuthentication():

    Username = input("Enter a Username : ")
    Password = input("Enter a Password : ")
    
    try :
    
        with open( "userRecords.txt" , "r" ) as file :
            recordsAuthentication = file.readlines()
        
        for userRecord in recordsAuthentication :
    
            usernameRecord, hashedPasswordRecord, saltRecord = userRecord.strip().split(":")
        
            if usernameRecord == Username :
                hashedPassword = J37HashFunction(Password,saltRecord)
            
                if int(hashedPasswordRecord) == hashedPassword :
                    print("\n[*] Signed In Successfully !\n")
                    return
                
                else :
                
                    print("\n[*] Authentication Failed - Incorrect Password !\n")
                    return
                
           
        print("\n[*] Authentication Failed - User Not Found !\n")
    
    except FileNotFoundError :        
        print("\n[*] No User Records Found !\n")
        return
        
# this is our user authentication function
        
print("\n############################################################")
print("                 Hashing In Deep - Project                    ")
print("By Jawad Fakiha - Tuwaiq Academy ( Cybersecurity Bootcamp )   ")
print("############################################################\n")
            
while True :
    
    userChoice = input("Choose an Option : \n[1] Register \n[2] Sign-In \n\n[*] : ")

    if userChoice == "1" :
        userRegestration()
        break
    
    elif userChoice == "2" :
        userAuthentication()
        break
        
    else :
        print("\n****************************")
        print("Invalid Choice - Try Again !")
        print("****************************\n")            
        


    
    
