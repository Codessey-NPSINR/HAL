import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()

server.login('codessyhps@gmail.com', 'bnwg ncsf sjrc dqsk')

server.sendmail('codessyhps@gmail.com', 'pritamghiremath9@gmail.com', 'test email')

print('sent')