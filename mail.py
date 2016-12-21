# -*- coding: utf-8 -*-
from app import app, mail


class MailSend:
    """Mail"""

    def __init__(self):
        self.sender = app.config['MAIL_SENDER']
        self.recepients = app.config['MAIL_RECEPIENTS']
        self.boss_email = app.config['BOSS_EMAIL']
        self.title_feedback = app.config['MAIL_FEEDBACK_TITLE']
        self.body_feedback = app.config['MAIL_FEEDBACK_BODY']
        self.title_service_query = app.config['MAIL_SERVICE_QUERY_TITLE']
        self.body_service_query = app.config['MAIL_SERVICE_QUERY_BODY']

    def send_feedback(self, url_from, name, email=None, phone=None, body=None):
        msg = mail.Message(
            self.title_feedback % name,
            sender=self.sender,
            recipients=self.recepients)
        msg.html = self.body_feedback % (name, url_from, email, phone, body)
        mail.send(msg)

    def send_service_query(self, equipment, name, email=None,
                           phone=None, body=None, comment=None):
        msg = mail.Message(
            self.title_service_query % name,
            sender=self.sender,
            recipients=self.recepients)
        msg.html = self.body_service_query % (equipment, name, email,
                                              phone, body, comment)
        mail.send(msg)
