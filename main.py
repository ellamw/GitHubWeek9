#                           NUMBER 1

import random
 
# given a list of integers, create a new list with the same number of elements
# each integer in the new list is the sum of its neighbors and itself in the original list
 
# create a random list
originalList = [random.randrange(1, 100) for i in range(random.randrange(0, 10))]
print("\nThe original list is", originalList)
print("The length of the original list is", len(originalList))
 
# create an empty new list
newList = []
 
# the base case is the first element in the new list is
# the first and second element added together from the original list
newList.append(originalList[0] + originalList[1])
 
# we will start at 1 since element 0 has been accounted for above
element = 1
 
# for each element starting at the second element and up to and not including the last element
# is the prev element, current element, and next element added together from the original list
while element < len(originalList) - 1:
    newList.append(originalList[element - 1] + originalList[element] + originalList[element + 1])
    element = element + 1
 
# the last element is just the prev element and the last element added together from the original list
newList.append(originalList[element - 1] + originalList[element])
 
print("\nThe new list is", newList)
print("The length of the new list is", len(newList), "\n")








#                           NUMBER 2

import matplotlib.pyplot as plt
 
# write a program that calculates the amount of money a person would earn over a period of time
# if his or her salary is one penny the first day, two pennies the second day, and continues to
# double each day. the program should ask the user for the number of days.
# Display a table showing what the salary was for each day, and then show the total pay at the end
# of the period. The output should be displayed in a dollar amount, not the number of pennies.
def salaryFunction(numberDays):
    salary = 0.01
    salaryList = []
    i = 1
    while i < numberDays + 1:
        salary *= 2
        print("You made $", salary, "today")
        i += 1
        salaryList.append(salary)
 
    print("The amount you will earn is $", salary)
    return salaryList
   
 
numberDays = int(input("How many days will you be working?: "))
 
plt.plot(salaryFunction(numberDays))
plt.xlabel("Number of Days Worked")
plt.ylabel("Amount Earned (in dollars)")
plt.title("Salary")
plt.show()








#                           NUMBER 3

# write 2 functions
# _encrypt takes plain text and assesses the indexed value of each letter in the string
# then adds 3 to the indexed value and produced encrypted text, based off of the plain text
# _decrypt reverses this
 
def _encrypt(PlainText):
 
    # Encrypted (aka Cipher) Text
    EncryptedText = ""
 
    # Encrypt = Transform PlainText into EncryptedText (aka Cipher)
    for i in PlainText:
        EncryptedText += chr(ord(i) + 3)
 
    print("\nThe Plain Text is:", PlainText)
    print("The Cipher Text is:", EncryptedText)
 
PlainText = input("\nEnter a sentence: ")
_encrypt(PlainText)
 
 
def _decrypt(EncryptedText):
 
    # Decypted Text
    DecryptedText = ""
 
    # Decrypt = Transform EncyptedText (aka Cipher) into PlainText
    for i in EncryptedText:
        DecryptedText += chr(ord(i) - 3)
 
    print("\nThe Cipher Text is:", EncryptedText)
    print("The Decrypted Text is:", DecryptedText)
 
EncryptedText = input("\nEnter the cipher text from above: ")
_decrypt(EncryptedText)








#                           NUMBER 4

#       PART 1
# write a program that prompts for an integer - let's call it x
# then finds the sum of x consecutive integers starting at 1
 
x = int(input("Enter a number: "))
sum = 0
for i in range(1, x + 1):
    sum += i
print(sum)


#       PART 2
# modify your program by enclosing your loop in another loop so that you can
# find consecutive sums. For example, if 5 is entered, you will find five sums
# of consecutive numbers
 
x = int(input("Enter a number: "))
for i in range(1, x + 1):
    sum = 0
    for j in range(1, i + 1):
        sum += j
    print(sum)








#                           NUMBER 5

#       PART 1
# write an if statement that assigns 20 to the variable y
# and assigns 40 to the variable z if the variable x is greater than 100
 
x = int(input("Enter a number: "))
 
if x > 100:
    z = 40
    y = 20
    print("z is", z)
    print("y is", y)
else:
    print("there is no z or y")


#       PART 2
# write an if statement that assigns 0 to the variable b
# and assigns 1 to the variable c if the variable a is less than 10
 
a = int(input("Enter a number: "))
 
if a < 10:
    b = 0
    c = 1
    print(b)
    print(c)


#       PART 3
# write an if-else statement that assigns 0 to the variable b
# if the variable a is less than 10. Otherwise it should assign 99 to the variable b
 
a = int(input("Enter a number: "))
 
if a < 10:
    b = 0
else:
    b = 99
 
print("b is", b)








#                           NUMBER 6

# write a function that takes as input an English sentence (a string) and prints the total number
# of vowels and the total number of consonants in the sentence. The function returns nothing.
# Note that the sentence could have special characters like dots, dashes, and so on.
 
def vowelConsonant(sentence):
    vowelCount = 0
    consonantCount = 0
    for i in sentence:
        if (i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "A" or i == "E" or i == "I" or i == "O" or i == "U"):
            vowelCount += 1
        elif (i == "b" or i == "c" or i == "d" or i == "f" or i == "g" or i == "h" or i == "j" or i == "k" or i == "l" or i == "m" or i == "n" or i == "p" or i == "q" or i == "r" or i == "s" or i == "t" or i == "v" or i == "w" or i == "x" or i == "y" or i == "z" or i == "B" or i == "C" or i == "D" or i == "F" or i == "G" or i == "H" or i == "J" or i == "K" or i == "L" or i == "M" or i == "N" or i == "P" or i == "Q" or i == "R" or i == "S" or i == "T" or i == "V" or i == "W" or i == "X" or i == "Y" or i == "Z"):
            consonantCount += 1
       
    print("The number of vowels is", vowelCount)
    print("The number of consonants is", consonantCount)
    return 0
 
sentence = input("Enter a sentence: ")
vowelConsonant(sentence)








#                           NUMBER 7

#       PART 1
# (a) Write a function to print the first N numbers of Fibonacci sequence.
 
def fibonacciList(n):
 
    list = [1, 1]
   
    for i in range(2, n):
        list.append(list[i - 1] + list[i - 2])
   
    print(list)
 
 
n = int(input("Enter how many numbers you want in the sequence: "))
 
fibonacciList(n)


#       PART 2
# (b) Write a function to print the Nth number of the sequence.
def fibonacciNum(n):
   
    list = [1, 1]
   
    for i in range(2, n):
        list.append(list[i - 1] + list[i - 2])
   
    print(list[n - 1])
 
   
n = int(input("Enter which number of the sequence you want to calculate: "))
 
fibonacciNum(n)