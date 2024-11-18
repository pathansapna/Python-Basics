# print('Sapna Pathan')
#
# ##################
# #Arithmatic operations
# #  ** - power of the number, // - dividing operator and giving integer result ; / - dividing operator and giving float result
# print(1 + 3 * 2 - 4 ** 2 / 3)
#
# #############################
# #If else
# is_hot = True
# is_cold = False
# if is_hot:
#     print("Its very hot today")
# elif is_cold:
#     print("Its very cold today")
# else:
#     print("Pretty day")
# print("Enjoy day")
#
# ###########################
# name = "John Smith"
# is_new_Patient = True
# age = 20
# #########################
# #Input function
# Wname = input("What is your name?  ")
# favorite_color = input("WHat is your favorite color? ")
# print(Wname + ' Likes ' + favorite_color)

############################
# weight = input("WHat is your weight in pounds? ")
# weight_kilo = float(weight) * float(0.454)
# print("weight_kilo = ", + weight_kilo)

########################################

# wt = input("Weight? ")
# k = int(wt) * 0.454
# l = int(wt) / 0.454
# st = input("(L)bs or (K)gs = ")
# st.lower()
# if st == "k":
#
#     print(k)
# else:
#     print(l)
##############################################

#
# command = ""
# started = False
# while True:
#     command = input("> ").lower()
#     if command == "start":
#         if started:
#             print("Car is already started")
#         else:
#             started = True
#             print("Car is started, Ready to go!")
#     elif command == "stop":
#         if not started:
#             print("Car is already stopped")
#         else:
#             started = False
#             print("Car is stopped")
#     elif command == "help":
#         print('''
#         start - to start the car
#         stop - to stop the car
#         quit - to exit
#         ''')
#     elif command == "quit":
#         break
#     else:
#         print("I don't understand that...")
#
####################################################33

# numbers = [2,2,2, 5]
# # for x_count in numbers:
# #     n = [x_count]
# #     for y_count in n:
# #         print("*" * y_count)
# for x_count in numbers:
#     output = ''
#     for y_count in range(x_count):
#         output += 'X'
#     print(output)

######################################################33
#Find largest number
# numbers = [2,1,10,7,9,4]
# largest = numbers[0]
# for x in numbers:
#     if largest <= x:
#         largest = x
# print(largest)

###################################################
#Remove duplicates in a list
# numbers = [2,4,5,5,7,8,8]
# orgin = []
# for x in numbers:
#     if x  not in orgin:
#         orgin.append(x)
# print(orgin)

#################################################3
#Print integers in to words
# x= input("Phone: ")
# dictionary = {
#     "1": "One",
#     "2" : "Two",
#     "3" : "Three",
#     "4" : "Four"
# }
# output =""
# for ch in x:
#     output += dictionary.get(ch, "!") + " "
#
# print(output)
#


########################################################

