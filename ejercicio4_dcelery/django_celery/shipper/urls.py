from django.conf.urls import url

from shipper.views import FileUploatView

app_name = "shipper"
urlpatterns = [
    url(r'uploat/$', FileUploatView.as_view(), name="uploat"),

]