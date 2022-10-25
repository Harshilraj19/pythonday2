# CONDITIONAL LOOPS  value set

# loops =0
# while loops <5:
#     print('this is a loop')
#     loops +=1
# print ('end of loop')


#


#  # VALIDATING
# x = "in"
# while x == "in":
#     userin=input("enter a number")
#     if userin.isnumeric():
#         print('that is a number')
#         x = "out"
#     else:
#         print("try again")
#         x = "in"
# print("thank you")

# loops= 10
# while loops < 20:
#     print(f" this is loop {loops}")
#     loops += 1


# times tables
# i = 1
# userin = int(input("enter a number"))
# while i <=12:
#     print(f"{userin} * {i} is {userin * i}")
#     i += 1

#('[@_!#$%^&*()<>?/\|}{~:]')


# x= "in"
#
# while x == "in" :
#     userIn= input("enter a number")
#     if userIn.isnumeric():
#         value= int(userIn)
#         if value < 10:
#             print("number is less than 10")
#             x = "in"
#         else:
#             print("you got it")
#             x = "out"
#
#     else:
#         print("not a number ")
#         x = "in"

# x = "in"
# while x == "in":
#      userin=input("enter password")
#      for char in userin:
#          if char.isalpha:
#             print("is a letter")
#          else:
#             print ('not a letter')


#




# special_symbols = ['$', '@', '#', '%']
#
# x = "in"
# while x == "in":
#     userin=input('enter password')
#
#     if len(userin) < 6:
#         print('Password must have at least 6 characters.')
#
#         continue
#
#     if len(userin) > 10:
#         print('Password cannot have more than 10 characters.')
#
#         continue
#
#     if not any(characters.isnumeric() for characters in userin):
#         print('Password must have at least one numeric character.')
#
#         continue
#
#     if not any(characters.isupper() for characters in userin):
#         print('Password must have at least one uppercase character')
#
#         continue
#
#     if not any(characters.islower() for characters in userin):
#         print('Password must have at least one lowercase character')
#
#         continue
#
#     if not any(characters in special_symbols for characters in userin):
#         print('Password should have at least one of the symbols $@#%')
#
#         continue
#
#     else:
#         print("Password is Valid.")
#         x = "out"




# # list of passowrds
# list_of_passwords = ['Abc@123', 'abc@123', 'ABC@123',
#                      'Abc@xyz', 'abc123', '12@#$%Abc',
#                      'Ab@1', "AAAAAbbbbbcccccc@#$%123456789"]
#
# # Validate each passowrd in the list
# for i in list_of_passwords:
#     print(i, ":"), validate_password(i)



def password ():
    special_symbols = ['$', '@', '#', '%']

x = "in"
while x == "in":
    userin=input('enter password')

    if len(userin) < 6:
        print('Password must have at least 6 characters.')

        continue

    if len(userin) > 10:
        print('Password cannot have more than 10 characters.')

        continue

    if not any(characters.isnumeric() for characters in userin):
        print('Password must have at least one numeric character.')

        continue

    if not any(characters.isupper() for characters in userin):
        print('Password must have at least one uppercase character')

        continue

    if not any(characters.islower() for characters in userin):
        print('Password must have at least one lowercase character')

        continue

    if not any(characters in special_symbols for characters in userin):
        print('Password should have at least one of the symbols $@#%')

        continue

    else:
        print("Password is Valid.")
        x = "out"

password()




































