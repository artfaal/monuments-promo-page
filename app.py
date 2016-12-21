# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, flash, url_for
from forms import FeedbackForm, ServiceRequest
from flask_mail import Mail

app = Flask(__name__)
app.config.from_object('config')
app.config.from_pyfile("config.py")
mail = Mail(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<name_page>')
def pages(name_page):
    form = FeedbackForm(request.form)
    service_form = ServiceRequest(request.form)
    if request.method == 'POST' and request.form['feedback'] == 'Default_Send' and form.validate():
        mail.send_feedback(request.base_url, form.name.data,
                           form.email.data, form.phone.data,
                           form.body.data)
        flash(app.config['ANSWER_1'])
        return redirect(url_for('pages', name_page=name_page))

    elif request.method == 'POST' and request.form['feedback'] == 'Service_Send' and form.validate():
        mail.send_service_query(
            service_form.equipment.data, service_form.name.data,
            service_form.email.data, service_form.phone.data,
            service_form.body.data, service_form.comment.data)
        flash(app.config['ANSWER_2'])
        return redirect(url_for('pages', name_page=name_page))
    else:
        return render_template(name_page)


if __name__ == '__main__':
    app.run(debug=True)
