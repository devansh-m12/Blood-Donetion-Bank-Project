print("****************************************************************************")
print("*                                                                          *")
print("*                   Welcome Blood Management System                     *")
print("*                                                  By:- Devansh $ Akash *")
print("****************************************************************************")
print("-----------------------------------------")
print("|Enter 1 for Admin mode			|\n|Enter 2 for user mode			|")#admin mode for blood bank manager
print("-----------------------------------------")
Admin_user_mode = input("Enter your mode : ")
if Admin_user_mode == "1":
    print("welcome to andmin mode")
    #print("enter your password")
    password=input("enter your password")
if password== "1234":##password for admin
    print("-----------------------------------------")
print("         Welcome to admin mode         ")
print("-----------------------------------------")

print("To add new Bank Enter 1	  	")
print("To Find Doner Enter 2	  	")
print("To URGENT REQUEST Enter 3		")
print("To Exit Enter 4    	")
print("-----------------------------------------")
y = input ("Enter your choice : ")
if y==1:
    add=input('Name of the hospital:')
    print(add+' has been added\n')
elif y==2:
    print(' Devansh Mahant (A-positive)\n Akash Chaurasia (O-negative)\n Vinnay Gaur (A-negative)\n Nilesh Choudhary (O-positive)\n Jack Marley (B-positive)\n')
elif y==3:
    print('URGENT REQUEST\nGrace Hospital Blood Bank is in URGENT NEED of Blood Donation of ALL TYPES\n')
while y!=4:
    print("-----------------------------------------")
print("         Welcome to admin mode         ")
print("-----------------------------------------")
print("To add new Bank Enter 1	  	")
print("To Find Doner Enter 2	  	")
print("To URGENT REQUEST Enter 3		")
print("To Exit Enter 4    	")
y = input ("Enter your choice : ")
if y==1:
      add=input('Name of the hospital:')
      print(add+' has been added\n')
elif y==2:
      print(' Devansh Mahant (A-positive)\n  Akash Chaurasia (O-negative)\n Vinnay Gaur (A-negative)\n Nilesh Choudhary (O-positive)\n Jack Marley (B-positive)\n')
elif y==3:
      print('URGENT REQUEST\nGrace Hospital Blood Bank is in URGENT NEED of Blood Donation of ALL TYPES\n')
elif x==2:
  print("-----------------------------------------")
print("         Welcome to user mode         ")
print("-----------------------------------------")

z=int(input('Content:\n 1. Send Blood Request\n 2. Donate Blood\n 3. Blood Requests\n 4. Exit\n'))
if z==1:
    request=input('Enter your blood group:')
    print('Your request for blood donation of '+request+' type has been sent\n')
elif z==2:
    donate=input('Enter your blood group:')
    print('Your blood type '+donate+' has beeen registered for blood donations\n')
elif z==3:
    a=int(input('URGENT REQUEST\nGrace Hospital Blood Bank is in URGENT NEED of Blood Donation of ALL TYPES\n 1.ACCEPT\n 2.IGNORE\n'))
if a==1:
        print(' You have ACCEPTED the blood donation request\n You will be contacted to schedule an appointment soon\n')
while z!=4:
    z=int(input('Content:\n 1. Send Blood Request\n 2. Donate Blood\n 3. Blood Requests\n 4. Exit\n'))
if z==1:
      request=input('Enter your blood group:')
      print('Your request for blood donation of '+request+' type has been sent\n')
elif z==2:
      donate=input('Enter your blood group:')
      print('Your blood type '+donate+' has beeen registered for blood donations\n')
elif z==3:
      a=int(input('URGENT REQUEST\nGrace Hospital Blood Bank is in URGENT NEED of Blood Donation of ALL TYPES\n 1.ACCEPT\n 2.IGNORE\n'))
      if a==1:
        print(' You have ACCEPTED the blood donation request\n You will be contacted to schedule an appointment soon\n')
else:
  print('Incorrect input')