import smtplib

def Send_Mail(text, tomail):
    try:
        frommail = 'yuri.v.assistant@gmail.com'
        psw = 'V08012018'

        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(frommail,psw)
        server.sendmail(frommail,tomail,text)
        server.quit()
        return 'Message sent to your email.'
    except:
        return "I couldn't sent you an email."

while True:
    msg = input('msg: ')
    mail = input('mail: ')
    ss = Send_Mail(msg, mail)
    print(ss)
        
