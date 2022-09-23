import sys

file = open( "temp.txt" , 'r')

string = ""
for line in file:
    string += line

lis = list(string.split( " " ))

print(lis[1])