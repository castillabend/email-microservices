# from django.shortcuts import render, redirect
#
# # Create your views here.
# from django.urls import reverse_lazy
# from django.views.generic import CreateView
#
# from shipper.forms import UploadForm
# from shipper.models import FileUpload
#
# #
from celery import chain
from django.shortcuts import render
from django.urls import reverse_lazy

from .tasks import create_excel, send_mail, clean_directory


def create_excel_view(request):
    if request.method == 'POST':
        (create_excel.s() | send_mail.s() | clean_directory.s())()

    return render(request, 'upload.html')
#
#
# class FileUploadView(CreateView):
#     model = FileUpload
#     template_name = 'upload.html'
#     form_class = UploadForm
#     success_url = reverse_lazy('shipper:upload')
#
#     # def form_valid(self, form):
#     #     form.save()
#     #     return redirect('shipper:uploat')
#
#
#
#
