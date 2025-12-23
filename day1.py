n=10
print(type(n))
print(id(n));
print(n)
n=20.0
print(type(n))
print(id(n));
print(n)
a,b,c=10,20.0,"KPIT"
print(a,b,c,sep='-')

print('Hello', end='*')
print("world")
print(n)

s='IlovePython'
print(s[1:5])
print(s[0:6:2])
print(s[1:])
print(s[0:5])
print(s[0:6:1])
print(s[0:7:2])
print(s[:])
print(s[-1])
print(s[-4:-1])

#sum of digits of number

n=123
sumDigit=0;
while n!=0:
    digit=n%10
    sumDigit+=digit
    n/=10
print("sum of digits of number is ",sumDigit)

#revere of number
num=561
rev=0
while n!=0:
    digit=n%10
    rev=rev*10+digit
    n/=10
print("reverse of number is ",rev)

str1="I love python"
words=str1.split()
print(words)
x=[[w.upper(),w.lower(),len(w)] for w in words]
print(x)


# print(10+20)
# print("Manish"+"Manish")
# print(10.5+20.5)
# print(True+True)
# print(10+"Radha")
# #TypeError : for +: ' int ' and str
# print(10+True)
# print(10.5+False)
# print(10+10.5)

# print(
# int ( OutPut 123
# print(
# int ( OutPut 1
# print(
# int ( OutPut 0
# print(float(False))
# OutPut 0.0
# print(
# str ( OutPut False
# a
# , b = 10, 20
# print(
# str ( str ( OutPut 1020
# print(
# int (" OutPut 10
# print(float("10"))
# OutPut 10.0
# print(
# int ("10.6")) ValueError : invalid literal for int ()
# with base 10: '10.6’


# s.find(t)

# index of first instance of string ‘t’ inside ‘s’ (-1 if not found)

# print(s.find(“l”))

# s.rfind(t)

# index of last instance of string ‘t’ inside ‘s’ (-1 if not found)

# print(s.rfind(“l”))

# s.index(t)

# like s.find(t) except it raises ValueError if not found

# print(s.index(“o”))

# s.rindex(t)

# like s.rfind(t) except it raises ValueError if not found

# print(s.rindex(“o”))

# s.strip()

# a copy of s without leading or trailing whitespace

# print(s.strip())

# s.split(t)

# split ‘s’ into a list wherever a ‘t’ is found (whitespace by default)

# print(s.split(“l”))
 
# s.splitlines()

# split ‘s’ into a list of strings, one per line

# print(s.splitlines())

# s.lower()

# a lowercased version of the string ‘s’

# print(s.lower())

# s.upper()

# an uppercased version of the string ‘s’

# print(s.upper())

# text.join(s)

# combine the words of the text into a string using ‘s’ as the glue

# print(“*”.join(s))

# s.title()

# a title cased version of the string ‘s’

# print(s.title())

# s.replace(t, u)

# replace instances of ‘t’ with ‘u’ inside s

# print(s.replace(“Python”, “Java”))
#  s.capitalize()

# converts first character of a ‘s’ to uppercase letter and lowercases all other characters

# print(s.capitalize())

# s.startswith()

# returns True if a string starts with the specified prefix(string). If not, it returns False

# print(s.startswith(“Welcome”))

# print(s.startswith(“come”,3,10))

# s.endswith()

# returns True if a string ends with the specified suffix. If not, it returns False

# print (s.endswith(“Session"))

# print (s.endswith("to",2,16))

# s.swapcase()

# converts all uppercase characters to lowercase and all lowercase characters to uppercase characters

# print(s. swapcase() )
 
# yes
 
# yes ma'am
 
# s.isalnum()

# returns True if all characters in the string are alphanumeric (either alphabets or numbers). If not, it returns False

# print(s.isalnum())

# s1=“Python310”

# print(s1.isalnum())

# s.isalpha()

# returns True if all characters in the string are alphabets. If not, it returns False

# print(s.isalpha())

# s2="HelloPython"

# print (s2.isalpha())

# s.isdigit()

# returns True if all characters in a string are digits. If not, it returns False

# print (s.isdigit())

# s2="98564738"

# print (s2.isdigit())
 

#  s.islower()
# returns True if all alphabets in a string are lowercase alphabets. If the string contains at least one uppercase alphabet, it returns False.
# print(s.islower())
# s1=“python”
# print(s1.islower())
# s.isupper()
# returns whether or not all characters in a string are uppercased or not
# print(s.alpha())
# s2="HelloPython"
# print (s2.isalpha())
# s.isspace()
# returns True if there are only whitespace characters in the string. If not, it return False.
# print (s.isspace())
# s2=“ "
# print (s2.isspace())

# numbers=[1,2,3,4,5]
# squared_numbers={num:num**2 for num in numbers}
# print(squared_numbers)

# print("reverse number")
# num=int(input("Enter a number: "))
# rev=0
# while num>0:
#     digit=num%10
#     rev=rev*10+digit
#     num//=10
# print("reverse of number is ",rev)
# #------------------------------------------------------------------
# print("pallindrome number")
# n=int(input("Enter a number: "))
# rev=0
# originalNum=n
# while n>0:
#     digit=n%10
#     rev=rev*10+digit
#     n//=10
# if originalNum==rev:
#     print("number is pallindrome")
# else:
#     print("number is not pallindrome")

# #-------------------------------------------------------------------
# print("sum of digits of number")

# number=int(input("Enter number "))
# sumNumberDigit=0
# while number>0:
#     digit=number%10
#     sumNumberDigit+=digit
#     number//=10
# print("sum of digits is ",sumNumberDigit)

# a=int(input("enter number to calculate factorial"))
# fact=1
# for i in range(1,a+1):
#     fact*=i
# print("factorial of number ",a,"is ",fact)

#----------------------------------------------------------------

# n=int(input("enter number till what you want fibonnaci series "))
# a,b=0,1

# if n<0:
#     print("number should be positive")
# elif n==1:
#     print(a)
# else:
#     print(a ,end=" ")
#     for i in range(1,n):
#         print(b,end=" ")
#         a,b=b,a+b
# print("\n")
# #------------------------------------------------------------------------
# print("sum of first 5 even numbers")
# sum=0
# cnt=0
# for i in range(1,11):
#     if i%2==0:
#         sum+=i
#         cnt+=1
#     if cnt>5:
#         break
# print("sum of first 5 even numbers: ",sum)
# #-------------------------------------------------------------------------
# print("sum of first 5 odd numbers")
# sum=0
# cnt=0
# for i in range(1,11):
#     if i%2!=0:
#         sum+=i
#         cnt+=1
#     if cnt>5:
#         break
# print("sum of first 5 odd numbers: ",sum) 


# print("first  10 prime numbers ")
# for i in range(1,30):
#     cnt=0
#     if i<=2:
#         continue
#     for j in range(2,int(i**0.5)+1):
#         if i%j==0:
#             cnt+=1
#     if cnt<1:
#         print(i)
        

# print("frequency of digits in number ")
# num=int(input("Enter the number: "))
# freq={}
# for digit in str(num):
#     if digit in freq:
#         freq[digit]+=1
#     else:
#         freq[digit]=1
# print("print frequency ")
# for digit,count in freq.items():
#     print(f"{digit}->{count}")


print("reversing list")
list1=[1,2,3,4]
list1.reverse()
print(list1)


