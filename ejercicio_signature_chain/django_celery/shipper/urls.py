from django.conf.urls import url

from . import views

app_name = "shipper"
urlpatterns = [
    url(r'^create_excel/$', views.create_excel_view, name="create_excel"),

]