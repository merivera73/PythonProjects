import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path 

html = Template(Path('index.html').read_text()
email = EmailMessage()
email['From'] = 'Me'
email['To'] = 'mertest73@yahoo.com'
email['Subject'] = 'You won the Lottery'

email.set_content('I am a Python Dev!!!!')

with smtplib.SMTP(host='smtp.yahoo.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('mertest73@yahoo.com', 'Devingappsin#2026')
    smtp.send_message(email)
    print('all good boss!')




# import smtplib
# from email.message import EmailMessage
# from string import Template
# from pathlib import Path 

# html = Template(Path('index.html').read_text())
# email = EmailMessage()
# email['from'] = 'Andrei Neagoie'
# email['to'] = '<to email address>
# email['subject'] = 'You won 1,000,000 dollars!'

# email.set_content(html.substitute({'name': 'TinTin'}), 'html')

# with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
#   smtp.ehlo()
#   smtp.starttls()
#   smtp.login('<your email address>', '<your password>')
#   smtp.send_message(email)
#   print('all good boss!')