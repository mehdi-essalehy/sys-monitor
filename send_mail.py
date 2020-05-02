import smtplib
import mail_config 

def send_mail(sub, msg):
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.ehlo()
	server.starttls()
	server.login(mail_config.EMAIL_ADDRESS, mail_config.PASSWORD)
	message = 'Subject: {}\n\n{}'.format(sub, msg)
	server.sendmail(mail_config.EMAIL_ADDRESS, mail_config.EMAIL_ADDRESS, message)
	server.quit()
