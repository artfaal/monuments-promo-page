# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, flash, url_for, send_from_directory
from flask_mail import Mail, Message
from flask_recaptcha import ReCaptcha
from wtforms import Form
from wtforms.fields import StringField, TextAreaField
from wtforms.validators import DataRequired, Length, Email

app = Flask(__name__)
app.config.from_object('config')
app.config.from_pyfile("config.py")
mail = Mail(app)
recaptcha = ReCaptcha(app=app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<name_page>', methods=['GET', 'POST'])
def pages(name_page):
    form = FeedbackForm(request.form)
    service_form = ServiceRequest(request.form)
    mail1 = MailSend()
    if request.method == 'POST' and request.form[
        'feedback'] == 'Default_Send' and form.validate() and recaptcha.verify():
        mail1.send_feedback(request.base_url, form.name.data, form.email.data, form.phone.data, form.body.data)
        flash(app.config['ANSWER_1'])
        return redirect(url_for('pages', name_page=name_page, form=form, service_form=service_form))

    elif request.method == 'POST' and request.form[
        'feedback'] == 'Service_Send' and form.validate() and recaptcha.verify():
        mail1.send_service_query(
            service_form.equipment.data, service_form.name.data,
            service_form.email.data, service_form.phone.data,
            service_form.body.data, service_form.comment.data)
        flash(app.config['ANSWER_2'])
        return redirect(url_for('pages', name_page=name_page, service_form=service_form))
    else:
        return render_template(name_page, form=form, service_form=service_form)


@app.route('/robots.txt')
def robots_from_root():
    return send_from_directory(app.static_folder, request.path[1:])


@app.route('/sitemap.xml')
def sitemap_from_root():
    return send_from_directory(app.static_folder, request.path[1:])


class FeedbackForm(Form):
    name = StringField(u'Имя*:', validators=[DataRequired()])
    email = StringField(u'E-mail*:', validators=[Email()])
    phone = StringField(u'Телефон:')
    body = TextAreaField(u'Сообщение*:')


class ServiceRequest(Form):
    """
    Форма для страницы: "Он-лайн заявка на проведение Сервисного обслуживания"
    """
    equipment = StringField(u'Оборудование*:', validators=[DataRequired()])
    body = TextAreaField(u'Описание неисправности*:',
                         validators=[DataRequired(),
                                     Length(min=5, max=5000)])
    name = StringField(u'Имя*:', validators=[DataRequired()])
    phone = StringField(u'Телефон:')
    email = StringField(u'E-mail*:', validators=[Email()])
    comment = StringField(u'Комментарий:')


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

if __name__ == '__main__':
    app.run(debug=True)
