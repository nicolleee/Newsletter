import smtplib

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()


    smtp.login('EMAIL_HOST_USER', 'EMAIL_HOST_PASSWORD')


    subject = 'mail?'
    body = 'mail!'

    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail('EMAIL_HOST_USER', 'EMAIL_HOST_USER', msg)
