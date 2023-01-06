#!/usr/bin/env python3
"""
CArcos | christopher.arcos@tlgcohort.com | Challenge 31
"""

wordbank = ["indentation", "spaces"]

tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']

#add int 4 to end of the list 
wordbank.append(4)

# conver the user input (1-20) to int
num = int(input("Enter a number betweeen 0-20\n"))

# based on user input grab that item from the list
student_name = tlgstudents[num]

print(f"{student_name} always uses {wordbank[2]} {wordbank[1]} to indent")

