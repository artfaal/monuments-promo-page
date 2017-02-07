# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, flash, url_for, send_from_directory
from forms import FeedbackForm, ServiceRequest
from flask_mail import Mail
import send_mail
from flask_recaptcha import ReCaptcha

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
    mail1 = send_mail.MailSend()
    service_form = ServiceRequest(request.form)
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


if __name__ == '__main__':
    app.run(debug=True)
