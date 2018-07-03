from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from shipper.forms import UploadForm
from shipper.models import FileUpload

#
# def uploat (request):
#     form = UploatForm(request.POST or None)
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             # return redirect('shipper:listar')
#     contexto = {'form': form}
#     return render(request, 'upload.html', contexto)


class FileUploadView(CreateView):
    model = FileUpload
    template_name = 'upload.html'
    form_class = UploadForm
    success_url = reverse_lazy('shipper:upload')

    # def form_valid(self, form):
    #     form.save()
    #     return redirect('shipper:uploat')




