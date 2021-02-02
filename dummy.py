import sys
import json
 
#if len(sys.argv) != 2:
 #   raise ValueError('Please provide email-id to send the email.')
 
#print(f'Script Name is {sys.argv[0]}')
 
#email = sys.argv[1]
 
#print(f'Sending test email to {email}')

# some JSON:
x =  '{"NUMBER": "2021020101",    "NAME": "AccountFeb0101",    "LAB": "LABFeb0101",    "TYPE": "CORPORATE"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["NUMBER"])

def Subtract (a, b): 
    return (a-b) 
  
print( Subtract(10, 12) ) # prints -2 
  
print( Subtract(15, 6) ) # prints 9 