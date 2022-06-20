from . import mail, create_app
from flask_mail import Message
from flask import render_template

app = create_app()

def send_mail(to, subject, template, **kwargs):
  msg = Message(app.config['ONESPACEPIRATE_MAIL_SUBJECT_PREFIX'] + subject, sender=app.config['MAIL_USERNAME'], recipients=[to])
  msg.body = render_template(template + '.txt', **kwargs)
  msg.html = render_template(template + '.html', **kwargs)
  mail.send(msg)



