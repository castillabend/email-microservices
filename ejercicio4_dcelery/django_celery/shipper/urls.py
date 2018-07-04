from django.conf.urls import url

from shipper.views import FileUploadView

app_name = "shipper"
urlpatterns = [
    url(r'upload/$', FileUploadView.as_view(), name="upload"),

]