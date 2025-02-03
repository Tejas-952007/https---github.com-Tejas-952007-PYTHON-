print("******Guess Name******")
# print the title game to attract people the focus on title intrest 
# * astrisk use as for design or inattractive interface or words 

n=int(input("set the range:"))
# get input for range make difficult or easy game
# 
# it is used for genrate random number in range
import random
num=random.randint(1,n)

# use while condition
while True:
  
  usernum=int(input("Enter the your Guess number:"))
#   get input of guess the number

# attempt to how many time to guess
  attempts=+1

  if(usernum==num):
    print("You won game!!!")
    print("congrtulation..")
    break
  elif(usernum>num):
   print("higher number guess")
   print("Try again...")
  else:
    print("lower number guess")
    print("try again")
print("atempts in won",attempts)