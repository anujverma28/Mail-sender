import smtplib
import getpass

# connection with email server

con = smtplib.SMTP("smtp.gmail.com",587)

# tl-587 is thee transport layer security

#ssl 425 second socket layer

#enable tls security
con.starttls()

# login to server
sender = input("Enter sender's email :")

print("Enter your password")

pwd = getpass.getpass()

receiver = input("Enter receiver's email :")

con.login(sender,pwd)

msg = "You have been hacked :)"

con.sendmail(sender,receiver,msg)

print("message sent")

con.quit()
