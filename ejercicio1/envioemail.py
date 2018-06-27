from django.conf import settings
from django.core.mail import EmailMessage

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
    EMAIL_HOST_PASSWORD='jfjhrejhrhrj',
    EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend',
)


def enviaremail(subject, to, fr_mail,  mensage): #cc_mail,
    e = EmailMessage()
    e.subject = subject
    e.to = [to]
    e.fr_mail = fr_mail
    #e.cc_mail = cc_mail
    e.body = mensage
    e.send()



