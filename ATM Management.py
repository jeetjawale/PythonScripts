import getpass
import string
import os

# creating a lists of users, their PINs and bank statements
users = ['riddhesh', 'sam', 'rick']
pins = ['1258', '1986', '4500']
amounts = [10000, 5990, 2980]
count = 0
# while loop checks existance of the enterd username
while True:
    user = input('\nENTER USER NAME: ')
    print(user)
    user = user.lower()
    if user in users:
        if user == users[0]:
            n = 0
        elif user == users[1]:
            n = 1
        else:
            n = 2
        break
    else:
        print('****************')
        print('INVALID USERNAME')
        print('****************')

# comparing pin
while count < 3:
    
    print('******************')
    pin = str(input('PLEASE ENTER PIN: '))
    print('******************')
   
    if pin.isdigit():
        if user == users[0]:
            if pin == pins[0]:
                break
            else:
                count += 1
                
                print('***********')
                print('INVALID PIN')
                print('***********')
                
                print()

        if user == users[1]:
            if pin == pins[1]:
                break
            else:
                count += 1
              
                print('***********')
                print('INVALID PIN')
                print('***********')
               
                print()
                
        if user == users[2]:
            if pin == pins[2]:
                break
            else:
                count += 1
             
                print('***********')
                print('INVALID PIN')
                print('***********')
            
                print()
    else:
        
        print('************************')
        print('PIN CONSISTS OF 4 DIGITS')
        print('************************')
        
        count += 1
    
# in case of a valid pin- continuing, or exiting
if count == 3:

    print('***********************************')
    print('3 UNSUCCESFUL PIN ATTEMPTS, EXITING')
    print('!!!!!YOUR CARD HAS BEEN LOCKED!!!!!')
    print('***********************************')

    exit()


print('*************************')
print('LOGIN SUCCESFUL, CONTINUE')
print('*************************')

print()

print('**************************')    
print(str.capitalize(users[n]), 'Welcome to ATM Management')
print('**************************')

# Main menu
while True:
    #os.system('clear')

    print('*******************************')
    response = input('SELECT ONE OF THE FOLLOWING: \nBalance____(B) \nWithdraw___(W) \nDeposit____(D)  \nChange Pin_(P)  \nQuit_______(Q) \n: ').lower()
    print('*******************************')
  
    valid_responses = ['b', 'w', 'd', 'p', 'q']
    response = response.lower()
    if response == 'b':
   
        print('*********************************************')
        print(str.capitalize(users[n]), 'YOU HAVE ', amounts[n],'RUPEES ON YOUR ACCOUNT.')
        print('*********************************************')
     
        
    elif response == 'w':
      
        print('*********************************************')
        cash_out = int(input('ENTER AMOUNT YOU WOULD LIKE TO WITHDRAW: '))
        print('*********************************************')
  
        if cash_out%10 != 0:
     
            print('******************************************************')
            print('AMOUNT YOU WANT TO WITHDRAW MUST TO MATCH 10 RUPEES NOTES')
            print('******************************************************')
           
        elif cash_out > amounts[n]:
       
            print('*****************************')
            print('YOU HAVE INSUFFICIENT BALANCE')
            print('*****************************')
           
        else:
            amounts[n] = amounts[n] - cash_out
       
            print('***********************************')
            print('YOUR NEW BALANCE IS: ', amounts[n], 'RUPEES')
            print('***********************************')
     
            
    elif response == 'd':
        print()
     
        print('*********************************************')
        cash_in = int(input('ENTER AMOUNT YOU WANT TO DEPOSIT: '))
        print('*********************************************')
   
        print()
        if cash_in%10 != 0:
           
            print('****************************************************')
            print('AMOUNT YOU WANT TO DEPOSIT MUST TO MATCH 10 RUPEES NOTES')
            print('****************************************************')
          
        else:
            amounts[n] = amounts[n] + cash_in
           
            print('****************************************')
            print('YOUR NEW BALANCE IS: ', amounts[n], 'RUPEES')
            print('****************************************')
          
    elif response == 'p':
    
        print('*****************************')
        new_pin = str(input('ENTER A NEW PIN: '))
        print('*****************************')
       
        if new_pin.isdigit() and new_pin != pins[n] and len(new_pin) == 4:
           
            print('******************')
            new_ppin = str(input('CONFIRM NEW PIN: '))
            print('*******************')
          
            if new_ppin != new_pin:
               
                print('************')
                print('PIN MISMATCH')
                print('************')
        
            else:
                pins[n] = new_pin
                print('NEW PIN SAVED')
        else:
        
            print('*************************************')
            print('   NEW PIN MUST CONSIST OF 4 DIGITS \nAND MUST BE DIFFERENT TO PREVIOUS PIN')
            print('*************************************')
        
    elif response == 'q':
        exit()
    else:
        
        print('******************')
        print('RESPONSE NOT VALID')
        print('******************')
        
