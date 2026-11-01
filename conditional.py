# Check whether a number is even or odd.
'''num=int(input("enter num:"))
if num%2==0:
    print("even")
else:
    print("odd")'''
    
# Find the largest of two numbers
'''num1 = int(input("enter num"))
num2 = int(input("enter num"))
if num1<num2:
    print(num2)
else:
    print(num1)'''
    
#Find the largest of three numbers.
'''num1 = int(input("enter num"))
num2 = int(input("enter num"))
num3 = int(input("enter num"))
if num1>num2:
    if num1<num3:
        print(num3)
    else:
        print(num1)
elif num2>num1:
    if num2<num3:
        print(num3)
    else:
        print(num2) 
else:
    print("equal")       
'''

'''voter= int(input("enter no:"))
if voter>18:
    print("eligable")
else:
    print("not eligable")'''
    
'''student=int(input("enter num:"))
if student<=100 and student>=90:
    print("A")
elif student>=80:
    print("B")
elif student>=70:
    print("C")
elif student>=60:
    print("D")
else:
    print("Fail")'''
    
'''year = int(input("Enter a year: "))

if year % 400 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("Not a leap year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")'''
    
#create simple calculator
'''num1=int(input("enter num:"))
num2=int(input("enter num:"))
print("choose, * = multiply, + = plus , / = divide , - = minus")
opration = input("enter opration = ")
if opration == "+":
    print(num1 + num2)
elif opration == "-":
    print(num1 - num2)
elif opration == "*":
    print(num1 * num2)
elif opration == "/":
    if num2==0:
        print("zero is not divisable")
    else:
        print(num1/num2)
else:
    print("error")'''
    

#short hand if statement
'''a= int(input("enter no:"))'''
'''if a>87: print("you are an excellent student")'''

'''print("you're an excellent student") if a>90 else print("avg")'''#(if,else)

# print no. from 1 to 10
'''a=1
while a<=10:
    print(a)
    a=a+1'''
    
# print even no. to 50
'''a=1
while a<=50:
    if a%2==0:
        print(a)
    a=a+1'''
    
# print multiplication table for any no.
'''num = int(input("enter no:"))
a=1
while a<=10:
    print(a*num)
    a=a+1'''
    
#check vowel
'''letter = input("enter letter:")

if letter in "aeiou":
    print("it is a vowel")
else:
    print("not an vowel")'''
    
#check wheater a no. is single or multi digit no.

#num= int(input ("enter num:"))

'''if num>0 and num<9:
    print("one digit")    
elif num>=10 and num<99:
    print("two digit")
elif num>=100 and num<999:
    print("three digit")
elif num>=1000 and num<9999:
    print("four digit") '''   
    
    
#print table    
'''num= int(input ("enter num:"))    
for i in range (1,10):
    print(i,"*",num,"=",num*i)'''
    
#while loop

#table print
'''a=int(input("enter num:"))
n=1
while n<=10:
    print(n,"*",a,"=",a*n)
    n=n+1'''
    
    
#while true
'''while True:
    num1=int(input("enter num:"))
    num2=int(input("enter num:"))
    print(num1+num2)
    a=(input("do you want to end this program give me ans in yes or no:"))
    if a=="yes":
        break'''
        
        
#nested loop
'''for i in range(1,5):
    for n in range(1,3):
        name= input("enter name:")
        print(name)
    print("class",i)'''
    
    
