

# This program will calculate the final tab between 2 people, deciding who owes who how much. For it to work, the user must have individual item debt amounts for each party.
import time

print("This program will determine how much one brother owes the other.")
time.sleep(2)
n=input("For how much Kyle owes Alex, how many items will you be entering?: ")
sum=0
n=int(n)
kyle=[]
for i in range(n):
    kyle=int(input("Enter value: "))
    sum+=kyle
print("Total Kyle owes is " + str(sum))
time.sleep(2)
n1=input("For how much Alex owes Kyle, how many items will you be entering?: ")
sum1=0
n1=int(n1)
alex=[]
for i in range(n1):
    alex=int(input("Enter value: "))
    sum1+=alex
print("Total Alex owes is " + str(sum1))
print("Calculating....")
time.sleep(2.5)
if sum1>sum:
    final=sum1-sum
    print("Alex owes Kyle " + str(final))
elif sum>sum1:
    final=sum-sum1
    print("Kyle owes Alex " + str(final))
else:
    print("Kyle and Alex are even.")

    



