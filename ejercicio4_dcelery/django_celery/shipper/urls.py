from django.conf.urls import url

from shipper.views import FileUploatView

app_name = "shipper"
urlpatterns = [
    url(r'upload/$', FileUploatView.as_view(), name="upload"),

]