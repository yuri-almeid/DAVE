import smtplib
        
def Send_Note(text):
    try:
        frommail = 'yuri.v.assistant@gmail.com'
        psw = 'V08012018'
        tomail = 'yuri.v.assistant@gmail.com'
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(frommail,psw)
        server.sendmail(frommail,tomail,text)
        server.quit()
        return 'Note taken sucefully at your email.'
    except:
        return "I couldn't sent your note."

def Send_Mail(text, tomail):
    try:
        frommail = 'yuri.v.assistant@gmail.com'
        psw = 'V08012018'

        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(frommail,psw)
        server.sendmail(frommail,tomail,text)
        server.quit()
        return 'Message sent sucefully.'
    except:
        return "I couldn't sent the email."


