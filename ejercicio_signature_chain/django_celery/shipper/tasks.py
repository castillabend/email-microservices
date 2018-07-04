from __future__ import unicode_literals, absolute_import

import delete as delete
import xlsxwriter
from django.contrib.auth.models import User
from django_celery import celery_app as app
from django.core.mail import EmailMessage
import os
from django.conf import settings


@app.task
def create_excel():
    # Some data we want to write to the worksheet.
    list_user = User.objects.filter(is_active=1)
    print("hola")
    # Create a workbook and add a worksheet.
    workbook = xlsxwriter.Workbook(
        'media/Report_user.xlsx',
        {'remove_timezone': True, 'default_date_format': 'dd/mm/yy'}
        )
    worksheet = workbook.add_worksheet()
    worksheet.write(0, 1, 'id')
    worksheet.write(0, 2, 'last_login')
    worksheet.write(0, 3, 'is_superuser')
    worksheet.write(0, 4, 'username')
    worksheet.write(0, 5, 'first_name')
    worksheet.write(0, 6, 'last_name')
    worksheet.write(0, 7, 'email')
    worksheet.write(0, 8, 'is_staff')
    worksheet.write(0, 9, 'is_active')
    worksheet.write(0, 10, 'date_joined')

    # row = 0
    # col = 0
    #
    # for item, cost in (list_user):
    #     worksheet.write(row, col, item)
    #     worksheet.write(row, col + 1, cost)
    #     row += 1

    i = 1
    for user in list_user:
        worksheet.write(i, 1, user.id)
        worksheet.write(i, 2, user.last_login)
        worksheet.write(i, 3, user.is_superuser)
        worksheet.write(i, 4, user.username)
        worksheet.write(i, 5, user.first_name)
        worksheet.write(i, 6, user.last_name)
        worksheet.write(i, 7, user.email)
        worksheet.write(i, 8, user.is_staff)
        worksheet.write(i, 9, user.is_active)
        worksheet.write(i, 10, user.date_joined)

        i += 1

    workbook.close()
    return 'media/Report_user.xlsx'


@app.task
def send_mail(ruta):
    e = EmailMessage()
    e.subject = settings.EMAIL_SUBJECT     # 'Reporte Usuarios Activos'
    e.to = settings.EMAIL_TO  #['castillabend@gmail.com',]
    e.from_email = settings.EMAIL_HOST_USER    #'castillabend@gmail.com'
    e.body = settings.EMAIL_BODY  #'PSI Adjunto Reporte Usuarios Activos'
    e.attach_file(ruta)
    e.send()
    return ruta

@app.task
def clean_directory(ruta):
    os.remove(ruta)


@app.task
def beat_crontab():
    (create_excel.s() | send_mail.s() | clean_directory.s())()


    # for index, row in val.iterrows():
    #     # for index, row in range(len(val)):
    #     user = User.objects.create_user(id=row['id'], last_login=row['last_login'], is_superuser=row['is_superuser'],
    #                                     username=row['username'], first_name=row['first_name'],
    #                                     last_name=row['last_name'],
    #                                     email=row['email'], is_staff=row['is_staff'], is_active=row['is_active'],
    #                                     date_joined=row['date_joined']
    # # expenses = (
    #     ['Rent', 1000],
    #     ['Gas', 100],
    #     ['Food', 300],
    #     ['Gym', 50],
    # )

    # Start from the first cell. Rows and columns are zero indexed.
    # row = 0
    # col = 0
    #
    # # Iterate over the data and write it out row by row.
    # for item, cost in (list_user):
    #     worksheet.write(row, col, item)
    #     worksheet.write(row, col + 1, cost)
    #     row += 1

    # Write a total using a formula.
    # worksheet.write(row, 0, 'Total')
    # worksheet.write(row, 1, '=SUM(B1:B4)')





