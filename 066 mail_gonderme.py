import  smtplib

content ="Merhaba Kullanici"


mail = smtplib.SMTP("smtp.gmail.com",587)

mail.ehlo()

mail.starttls()

mail.login("gonderen@gmail.com","şifre")
#mail.sendmail("kimden","kime","içerik")
mail.sendmail("gonderen@gmail.com","alici@gmail.com",content)