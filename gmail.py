import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


from email.mime.image import MIMEImage
import os.path

def maill():
		
	email= 'hirdeshj3005@gmail.com' #'sj2000sonam@gmail.com'
	password= '@hash12183061' #Enter your password
	sendto=	 'aarchij12001@gmail.com'  #input('enter email=')
	message= 'Dear sir  this is last person. Who try to acess your laptop' #input('enter message=')
	sub= 'Urjent Check' #input('enter subject=')

	file_location= 'mail1.py'

	msg=MIMEMultipart()
	msg['from']=email
	msg['to']=sendto
	msg['subject']=sub
	msg.attach(MIMEText(message,'plain'))


	fleiname=os.path.basename(file_location)
	fp =open('new.jpg','rb')
	image = MIMEImage(fp.read())
	msg.attach(image)
	fp.close()

	server=smtplib.SMTP('smtp.gmail.com',587)
	server.starttls()
	server.login(email,password)
	txt=msg.as_string()
	server.sendmail(email,sendto,txt)
	server.quit()
	print('mail send')

#maill()
