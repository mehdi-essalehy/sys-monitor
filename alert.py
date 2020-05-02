from get_data  import get_data
from send_mail import send_mail
from config    import *

def alert(cpu_threshold=cpu_threshold, ram_threshold=ram_threshold, disk_threshold=disk_threshold):
	"""sends an email when cpu, memory or disk usage above threshold"""

	cpu, ram, disk = get_data()

	if cpu > cpu_threshold or ram > ram_threshold or disk > disk_threshold:
		subject = 'ALERT'
		message = "Abnormal usage of resources.\n\ncpu: {}\nram: {}\ndisk: {}".format(cpu, ram, disk)
		send_mail(subject, message)

alert()