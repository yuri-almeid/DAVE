import smtplib
server = smtplib.SMTP('localhost')
server.sendmail('yurilima95@gmail.com','yurilima95@gmail.com',""" teste """)
server.quit()
