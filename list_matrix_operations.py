# -*- coding: ut(f-8 -*-
"""
Created on Sun Dec  3 22:05:10 2023

@author: Feyza
"""

my_name = "Ayse Feyza Birer"
my_id = "220102002033"
my_email = "a.birer2022@gtu.edu.tr"

def problem1(a,b):
  if b >= len(a) or b < 0:
      return None
  else:
      return a[b]
    
  
def problem2(a,b):
    if b > len(a) or b < 0:
        return a 
    else:
        c = a[b]
        a.remove(c)
        return a
    
def problem3(a,b):
    if b == True:
        a.sort()
        return a
    else:
        a.sort()
        a.reverse()
        return a
    
def problem4(a,b):
    sum_ab = 0
    sum_b = 0
    
    for i in range(len(a)):
        sum_ab += a[i] * b[i]
        sum_b += b[i]
    return float(sum_ab) / float(sum_b)

def problem5(a,b):
    new_a = []
    for i in a:
        if a.count(i) > 1 and i not in new_a:
            new_a.append(i)    
        elif a.count(i) == 1 and i not in new_a:
            new_a.append(i)
        

    new_b = []
    for i in b:
        if b.count(i) > 1 and i not in new_b:
            new_b.append(i)
        elif b.count(i) == 1 and i not in new_b:
            new_b.append(i)
        
  
    count = 0
    for i in new_a:
        if i in new_b:
            count += 1
    return count

def problem6(a):
    if len(a) == 2:
        b = a[0]
        c = a[1]
        if len(b) == len(c):
            if len(b) == 1:
                determinant = b[0] - c[0]
            elif len(b) == 2:
                determinant = (b[0] * c[1]) - (c[0] * b[1])
            elif len(b) == 3:
                determinant = ((b[0] * c[1]) + (b[1] * c[2])) - ((c[0] * b[1]) + (c[1] * b[2]))
            elif len(b) == 4:
                determinant = ((b[0] * c[1]) + (b[1] * c[2]) + (b[2] * c[3])) - (
                        (c[0] * b[1]) + (c[1] * b[2]) + (c[2] * b[3]))
        else:
            return None

    elif len(a) == 3:
        b = a[0]
        c = a[1]
        d = a[2]
        if len(b) == len(c) == len(d):
            if len(b) == 1:
                determinant = b[0] - c[0] - d[0]
            elif len(b) == 2:
                determinant = ((b[0] * c[1]) + (c[0] * d[1])) - ((c[0] * b[1]) + (d[0] * c[1]))
            elif len(b) == 3:
                determinant = ((b[0] * c[1] * d[2]) + (c[0] * d[1])) - ((c[0] * b[1]) + (d[0] * c[1] * b[2]))
            elif len(b) == 4:
                determinant = ((b[0] * c[1] * d[2]) + (c[0] * d[1]) + (b[1] * c[2])) - (
                        (c[0] * b[1]) + (d[0] * c[1] * d[2]) + (d[1] * c[2]))

        else:
            return None

    elif len(a) == 4:
        b = a[0]
        c = a[1]
        d = a[2]
        e = a[3]
        if len(b) == len(c) == len(d) == len(e):
            if len(b) == 1:
                determinant = b[0] - c[0] - d[0] - e[0]
            elif len(b) == 2:
                determinant = (((c[0] * b[1]) + (d[0] * c[1]) + (e[0] * d[1])) - (
                        (b[0] * c[1]) + (c[0] * d[1]) + (d[0] * e[1])))
            elif len(b) == 3:
                determinant = (((c[0] * b[1]) + (d[0] * c[1] * b[2]) + (e[0] * d[1]) * c[2]) - (
                        (b[0] * c[1] * d[2]) + (c[0] * d[1] * e[2]) + (d[0] * e[1]) + (b[1] * c[2])))
            elif len(b) == 4:
                determinant = ((b[0] * c[1] * d[2] * e[3]) + (c[0] * d[1] * e[2]) + (d[0] * e[1]) + (
                        b[1] * c[2]) + (b[2] * c[3])) - (
                                       (c[0] * b[1]) + (d[0] * c[1] * b[2]) + (e[0] * d[1] * c[2] * b[3]) + (
                                       e[1] * d[2] * c[3]) + (e[2] * d[3]))

        else:
            return None

    elif len(a) == 1:
        b = a[0]
        return float(b[0])

    return determinant

def problem7(accounts=" ", source=" ", lira=" ", kurus=" "):
    source = int(source)
    if source < 0  or source >= len(accounts):
        return accounts
    elif float(accounts[source]) < (float(lira) + float(kurus*1/100)):
        return accounts
    else:
      accounts[source] = str(abs(round(float(accounts[source]) - float(lira) - float((kurus*1/100)), 2)))
        
    return accounts
      
def problem8(a):
    students = list(range(1, a + 1))
    index = 0

    while len(students) > 1:
        index = (index + 8) % len(students)
        eliminated_student = students.pop(index)
    return students[0]

def problem9(a):
    for element in a:
        if a.count(element) > 1:
            return element
    return None




    
        
    
















