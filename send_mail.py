# -*- coding: utf-8 -*-
from app import app, mail
from flask_mail import Message


class MailSend:
    """Mail"""

    def __init__(self):
        self.sender = app.config['MAIL_SENDER']
        self.recipients = app.config['MAIL_RECIPIENTS']
        self.boss_email = app.config['BOSS_EMAIL']
        self.title_feedback = app.config['MAIL_FEEDBACK_TITLE']
        self.body_feedback = app.config['MAIL_FEEDBACK_BODY']
        self.title_service_query = app.config['MAIL_SERVICE_QUERY_TITLE']
        self.body_service_query = app.config['MAIL_SERVICE_QUERY_BODY']
        print(self.recipients)

    def send_feedback(self, url_from, name, email=None, phone=None, body=None):
        msg = Message(
            self.title_feedback % name,
            sender=self.sender,
            recipients=self.recipients)
        msg.html = self.body_feedback % (name, url_from, email, phone, body) + '\r\n.'
        mail.send(msg)

    def send_service_query(self, equipment, name, email=None,
                           phone=None, body=None, comment=None):
        msg = Message(
            self.title_service_query % name,
            sender=self.sender,
            recipients=self.recipients)
        msg.html = self.body_service_query % (equipment, name, email,
                                              phone, body, comment) + '\r\n.'
        mail.send(msg)
