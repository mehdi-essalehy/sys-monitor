# sys-monitor
monitors cpu, memory and disk usage and sends email if there is a spike

to run any of these files you need to [install the psutil module](https://github.com/giampaolo/psutil/blob/master/INSTALL.rst),
and [allow access to less secure apps on your gmail account](https://myaccount.google.com/lesssecureapps)

put the email adderess and password of your gmail account in the mail_config.py file
you can change the thresholds beyond which the email gets sent in the config.py file

you can either run the main.py file and then push it to the background;
in this case you can change the time between checks by changing the variable t in the main.py file,
or run alert.py as a cron job 

you can also run the get_data.py file to get (cpu, memory, disk) usage 
