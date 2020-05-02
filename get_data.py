import psutil

def get_data():
	cpu  = psutil.cpu_percent(interval=1) #percentage of cpu usage
	ram  = psutil.virtual_memory()[2] #percentage of mem usage
	disk = psutil.disk_usage('/')[3] #percentage of disk usage
	return cpu, ram, disk

get_data()