import sys
 
if len(sys.argv) != 2:
    raise ValueError('Please provide email-id to send the email.')
 
print(f'Script Name is {sys.argv[0]}')
 
email = sys.argv[1]
 
print(f'Sending test email to {email}')
