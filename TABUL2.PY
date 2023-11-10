
# This program will calculate the final tab between 2 people, deciding who owes who how much. For it to work, the user must have individual item debt amounts for each party.

#version 2
# for this version, I want to create an indefinite array which the user will fill 
import time

print("This program will determine how much one brother owes the other.")
time.sleep(2)
print("First the program will calculate how much Kyle owes Alex.")
time.sleep(1)
sum=0
kyle=[]
fill=True
for i in range(33):
    while fill == True:
        kyle=(input("Enter item value or 'x' to finish: "))
        if kyle == "x":
            kyle=0
            fill=False
            sum+=kyle
        else:
            kyle = int(kyle)
            sum+=kyle
time.sleep(1)
print("Total Kyle owes is $" + str(sum))
time.sleep(2)
print("Now the program will calculate how much Alex owes Kyle.")
time.sleep(1)
sum1=0
alex=[]
fill=True
for i in range(33):
    while fill == True:
        alex=(input("Enter item value or 'x' to finish: "))
        if alex == "x":
            alex=0
            fill=False
            sum1+=alex
        else:
            alex = int(alex)
            sum1+=alex
time.sleep(1)
print("Total Alex owes is $" + str(sum1))
time.sleep(1)
print("Calculating....")
time.sleep(2.5)
if sum1>sum:
    final=sum1-sum
    print("Alex owes Kyle $" + str(final))
elif sum>sum1:
    final=sum-sum1
    print("Kyle owes Alex $" + str(final))
else:
    print("Kyle and Alex are even.")

