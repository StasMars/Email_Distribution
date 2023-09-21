import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def send_ya_mail(recipients_emails: list, msg_text: str):
    login = 'Ваша почта'
    password = os.getenv('Ваш пароль')

    msg = MIMEText(f'{msg_text}', 'plain', 'uft-8')
    msg['Subject'] = Header('Текст темы письма', 'uft-8')
    msg['From'] = login
    msg['To'] = ', '.join(recipients_emails)

    s = smtplib.SMTP('smtp.yandex.ru', 587, timeout=10)

    try:
        s.starttls()
        s.login(login, password)
        s.sendmail(msg['From'], recipients_emails, msg.as_string())
    except Exception as ex:
        print(ex)
    finally:
        s.quit()


def main():
    send_ya_mail(recipients_emails=['Почта №1', 'Почта №2', 'и т.д.'], msg_text='Текст сообщения')   #Вписываем почты вех, кому хотите отправить и текст самого сообщения


if __name__ == '__main__':
    main()