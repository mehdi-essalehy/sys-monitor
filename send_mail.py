import smtplib
import mail_config 

def send_mail(sub, msg):
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.ehlo()
	server.starttls()
	server.login(config.EMAIL_ADDRESS, config.PASSWORD)
	message = 'Subject: {}\n\n{}'.format(sub, msg)
	server.sendmail(config.EMAIL_ADDRESS, config.EMAIL_ADDRESS, message)
	server.quit()
