from __future__ import absolute_import
from celery import current_app
from shipper.models import FileUpload
from .models import FileUpload
import pandas as re

#import numpy as np
from django.contrib.auth.models import User


app = current_app


@app.task
def test_shipper():
    print('Hi im shipper')


@app.task
def import_file(_id):
    f = FileUpload.objects.get(id=_id)
    return f.name.name
#import pandas as re
@app.task
def read_excel(val_id):
    file = FileUpload.objects.get(id=val_id)
    val = re.read_excel(file.name.path)
    # print(archivo_excel.columns)
    # values = archivo_excel['id'].values
    # print(values)
    # columnas = ['id', 'last_login', 'is_superuser', 'username', 'first_name',
    #             'last_name', 'email', 'is_staff', 'is_active', 'date_joined']
    # df_seleccionados = archivo_excel[columnas]
    # print(df_seleccionados)


    for index, row in val.iterrows():
    #for index, row in range(len(val)):
        user = User.objects.create_user(id=row['id'], last_login =row['last_login'], is_superuser =row['is_superuser'],
                                        username=row['username'], first_name=row['first_name'], last_name=row['last_name'],
                                        email=row['email'], is_staff=row['is_staff'], is_active=row['is_active'], date_joined=row['date_joined']
                                        )


    # user=User.objects.create_user(‘foo’, password=’bar’) #   creamos el usuario y clave
    # user.is_superuser=True   #permisos de superusuario
    # user.is_staff=True #definimos si es parte del staff
    user.save() #guardamos los datos.