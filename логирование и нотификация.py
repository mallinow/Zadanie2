import logging
import requests
import smtplib
from email.mime.text import MIMEText

# настройка логирования
logging.basicConfig(filename='app.log', level=logging.INFO)

# отправка сообщения в Slack
def send_slack_message(text, webhook_url):
    data = {'text': text}
    response = requests.post(webhook_url, json=data)
    if response.status_code != 200:
        logging.error(f'Ошибка отправки сообщения в Slack: {response.content}')

# отправка уведомления по электронной почте
def send_email_notification(text, from_addr, to_addr, smtp_server, smtp_port, smtp_username, smtp_password):
    msg = MIMEText(text)
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = 'Уведомление о завершении задачи'

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(from_addr, [to_addr], msg.as_string())

# выполнение задачи
def run_task():
    logging.info('Начало выполнения задачи')
    # здесь выполняется ваша задача
    logging.info('Задача выполнена успешно')

# отправка уведомлений
def send_notifications():
    # отправка сообщения в Slack
    slack_webhook_url = 'https://hooks.slack.com/services/XXXXXXXXX/XXXXXXXXX/XXXXXXXXXXXXXXXXXXXXXXXX'
    send_slack_message('Задача выполнена успешно', slack_webhook_url)

    # отправка уведомления по электронной почте
    from_addr = 'sender@example.com'
    to_addr = 'recipient@example.com'
    smtp_server = 'smtp.example.com'
    smtp_port = 587
    smtp_username = 'username'
    smtp_password = 'password'
    send_email_notification('Задача выполнена успешно', from_addr, to_addr, smtp_server, smtp_port, smtp_username, smtp_password)

# основной код
if __name__ == '__main__':
    try:
        run_task()
        send_notifications()
    except Exception as e:
        logging.error(f'Ошибка выполнения задачи: {str(e)}')
        send_slack_message(f'Ошибка выполнения задачи: {str(e)}', slack_webhook_url)
