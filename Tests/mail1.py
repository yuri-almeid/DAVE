import smtplib

def Send_Mail(text):
    try:
        frommail = 'yuri.v.assistant@gmail.com'
        psw = 'V08012018'
        tomail = 'yuri.v.assistant@gmail.com'
        text = "Hello World"
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(frommail,psw)
        server.sendmail(frommail,tomail,msg)
        server.quit()
        return 'Message sent to your email.'
    except:
        return "I couldn't sent you an email."

while True:
    msg = input('msg: ')
    ss = Send_Mail(msg)
    print(ss)
        
