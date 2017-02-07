# -*- coding: utf-8 -*-

SECRET_KEY = ''
########################
# Mail Server Settings #
########################
MAIL_SERVER = 'smtp.mail.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = 'robot@mail.com'
MAIL_PASSWORD = 'password'
MAIL_SENDER = 'robot@mail.com'
MAIL_RECIPIENTS = ['robot@mail.com']
BOSS_EMAIL = ["robot@mail.com"]

# TODO What with cirillic symbols. Didn't work.

MAIL_FEEDBACK_TITLE = u''
MAIL_SERVICE_QUERY_TITLE = u''
MAIL_FEEDBACK_BODY = u""""""
MAIL_SERVICE_QUERY_BODY = u""""""
ANSWER_1 = "Message send."
ANSWER_2 = "Message send."
ANSWER_3 = "Message send."

RECAPTCHA_ENABLED = True
RECAPTCHA_SITE_KEY = ""
RECAPTCHA_SECRET_KEY = ""
# RECAPTCHA_THEME = "dark"
RECAPTCHA_TYPE = "image"
# RECAPTCHA_SIZE = "compact"
RECAPTCHA_RTABINDEX = 10

# MAIL_SUPPRESS_SEND = False
# MAIL_DEBUG = True
# TESTING = False
