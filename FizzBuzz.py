#Nicholas Rudolph
#Class: Capture The Flag
#Date: Jan 21, 2020

#takes name as input
name = input("Enter your name: ")

for i in name:
    print(i + "\t", end=" ")
print("")
for i in range(len(name)):
    char = name[i]
    print(str(ord(char))+ "\t", end=" ")
print("")
for x in name:
    if (ord(x) % 3  == 0 and ord(x) % 5 == 0): #fizzbuzz if divisible by 3 and 5
        print("fizzbuzz", end=" ")
    elif (ord(x) % 5 == 0): #buzz if divisible by 5
        print ("buzz\t", end =" ")
    elif (ord(x) % 3 == 0): #fizz if divisible by 3
        print("fizz\t", end=" ")
    else:
        print("\t", end=" ")
print("")       
