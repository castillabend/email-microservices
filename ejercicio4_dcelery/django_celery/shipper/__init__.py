#se coloca lo siguiente en el __init__ para que celery reconosca las task creadas dentro de la app
    #o se puede configurar en la propia task :  (from __future__ import absolute_import from celery import current_app app = current_app)


# from .celery import app as celery_app
#
# __all__ = ['celery_app']