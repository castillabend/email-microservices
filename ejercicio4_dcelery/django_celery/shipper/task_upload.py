from __future__ import absolute_import
from celery import current_app

from shipper.models import FileUploat

app = current_app


@app.task
def test_shipper():
    print('Hi im shipper')


@app.task
def import_file(id):
    f = FileUploat.objects.get(pk=id)
    print(f.name.name)