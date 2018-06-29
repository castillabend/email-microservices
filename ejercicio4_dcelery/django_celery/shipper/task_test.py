from __future__ import absolute_import
from celery import current_app
app = current_app


@app.task
def test_shipper():
    print('Hi im shipper')