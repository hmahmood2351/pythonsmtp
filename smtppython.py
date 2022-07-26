import smtplib, ssl 

sender = 'ic3squid@gmail.com'
password = 'APP PASSWORD GOES HERE'
receiver = 'hmahmood2351@gmail.com'

body_msg = '''Subject: test
I've sent an e-mail with Python'''

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
    server.login(sender, password)
    server.sendmail(sender, receiver, body_msg)
    
#references: 
#https://www.youtube.com/watch?v=Dg8L5t3kdAU, 
