from django.conf import settings
from django.core.mail import EmailMessage
from celery import Celery

app = Celery('prueba_celery', backend= 'amqp://quest:quest@localhost', broker= 'amqp://localhost')

settings.configure(

    DEBUG=True,
    SECRET_KEY='thisisthesecretkey',
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=(

        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',

    ),
    EMAIL_USE_TLS=True,
    EMAIL_HOST='smtp.gmail.com',
    EMAIL_PORT=25,
    EMAIL_HOST_USER='castillabend@gmail.com',
    EMAIL_HOST_PASSWORD='reinandoenvida',
    EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend',
)


@app.task
def enviaremail(subject, to, fr_mail,  message):
    e = EmailMessage()
    e.subject = subject
    e.to = [to]
    e.from_email = fr_mail
    e.body = message
    e.send()


if __name__ == '__main__':
    subject = input('Insert subject: ')
    to = input('Insert destine: ')
    message = input('Insert body: ')
    enviaremail.delay(subject, to, 'castillabend@gmail.com', message)

## PUBLISHER Y WORKER EN UN MISMO ARCHVIVO CON CELERY, SE EJECUTA (celery worker -A prueba_celery -l info) Y EN OTRA TERMINAL SE EJECUTA (python prueba_celery.py)


