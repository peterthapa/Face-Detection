
# # Program to display the Fibonacci sequence up to n-th term
# nterms = int(input("How many terms? "))
# # first two terms
# n1, n2 = 0, 1
# count = 0
# # check if the number of terms is valid
# if nterms<=0:
#    print("Please enter a positive integer")
# # if there is only one term, return n1
# elif nterms == 1:
#    print("Fibonacci sequence upto",nterms)
#    print(n1)
# # generate fibonacci sequence
# else:
#    print("Fibonacci sequence:")
#    while count < nterms:
#        print(n1)
#        nth = n1 + n2
#        # update values
#        n1 = n2
#        n2 = nth
#        count += 1


# number = int(input ("Enter the number of which the user wants to print the multiplication table: "))      
# # We are using "for loop" to iterate the multiplication 10 times       
# print ("The Multiplication Table of: ", number)    
# for count in range(1, 11):      
#    print (number, 'x', count, '=', number * count)    

 
# english = float(input(" Please enter English Marks: "))
# math = float(input(" Please enter Math score: "))
# computers = float(input(" Please enter Computer Marks: "))
# physics = float(input(" Please enter Physics Marks: "))
# chemistry = float(input(" Please enter Chemistry Marks: "))

# total = english + math + computers + physics + chemistry
# percentage = (total / 500) * 100

# print("Total Marks = %2f"  %total)
# print("Marks Percentage = %2f"  %percentage)

# if(percentage >= 90):
#     print("S Grade")
# elif(percentage >= 80):
#     print("A Grade")
# elif(percentage >= 70):
#     print("B Grade")
# elif(percentage >= 60):
#     print("CGrade")
# elif(percentage >= 50):
#     print("D Grade")
# elif(percentage >=40):
#     print("E Grade")
# else:
#     print("Fail")



# Python3 program for intersection() function
# 


# import pandas as pd
# import numpy as np
# exam_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
#         'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
#         'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
#         'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
# labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# df = pd.DataFrame(exam_data , index=labels)
# print("Orginal rows:")
# print(df)
# df.sort_values(by=['name', 'score'], ascending=[False, True])
# print("Sort the data frame first by ‘name’ in descending order, then by ‘score’ in ascending order:")
# print(df)


# import tkinter as tk
# from tkinter import messagebox as m
# def show():
#     str=t1.get()
# m.showinfo("password",str)

# w1=tk.Tk()
# w1.title("First")
# l1=tk.Label(w1,text="Password")
# l1.grid(column=0,row=0)
# t1=tk.Entry(w1,width=10,show="*")
# t1.grid(column=1,row=0)
# b1=tk.Button(w1,text="Show",command=show)
# b1.grid(column=1,row=1)
# w1.mainloop()

# number = int(input("Please Enter any Number: "))
# reverse = 0
# temp = number
# while(temp > 0):
#     Reminder = temp % 10
#     reverse = (reverse * 10) + Reminder
#     temp = temp //10
 
# print("Reverse of a Given number is = %d" %reverse)

# if(number == reverse):
#     print("%d is a Palindrome Number" %number)
# else:
#     print("%d is not a Palindrome Number" %number)

# Print Pascal's Triangle in Python
# from math import factorial
# # input n
# n = int(input("Enter how many rows:"))
# for i in range(n):
#   for j in range(n-i+1):
#     # for left spacing
#     print(end=" ")
#   for j in range(i+1):
#     # nCr = n!/((n-r)!*r!)
#     print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
#     # for new line
#   print()

# x=int(input("Enter row number="))
# for i in range(x):
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print("")

# def great(a,b,c):
#       if a>b and a>c:
#          print("A is greatest")
#       elif b>c:
#             print("B is greatest")
#       else:
#             print("C is greatest")

# a=input("Enter first no")
# b=input("Enter 2nd no")
# c=input("Enter 3rd no")
# great(a,b,c)

# import numpy as np

# x = np.ones((10, 10))
# x[1:-1, 1:-1] = 0
# print(x)

# def Sieve of Eratosthenes(n):
#     print(prime)
#     p=2
#     while(p*p<=n)
#     if (prime[p]==true):
#         for i in range(p&2,n+1,p):
#             prime[i]=False
#             print(i,prime[i])
#             p+=1
#             prime[0]=False
#             prime[1]=False
#             for p in range (n+1):
#                 if prime[p]:
#                     print(p)



def allset(a,n,v,total):
    if total == 0:
        for value in v :
            print(value,end=" ")
        print()
        return
    if n == 0:
        return
    allset(a,n-1,v,total)
    v1 = []+v
    v1.append(a[n-1])
    allset(a,n-1,v1,total-a[n-1])
    
def printarray(a,n,total):
    v= []
    print("The solutions are : ")
    allset(a,n,v,total)
    
a = []
n = int(input("Enter the length of set : "))
total = int(input("Enter the sum value : "))
print("Enter the elements of the set : ")
for i in range(n):
    x = int(input())
    a.append(x)
printarray(a,n,total)


