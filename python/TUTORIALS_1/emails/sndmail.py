def sndmail(frome, toe, content):
    import smtplib as sml
    try:
        s = sml.SMTP('smtp.gmail.com', 587)
        s.ehlo()
        s.starttls()
        s.login(frome, passwd)
        s.sendmail(toe, content)
        s.close()
    except Exception as e:
        print(e)


frome  = 'ksc11197@gmail.com'
passwd = 'uydckbkhjxckfseg'
toe = 'sprabhas905@gmail.com'
content = 'JAI SHREE RAM FROM SMTP SERVER'
sndmail(frome, toe, content)