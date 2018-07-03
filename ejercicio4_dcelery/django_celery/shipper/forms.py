from django import forms
from shipper.models import FileUpload
from shipper.tasks import import_file, read_excel


class UploatForm(forms.ModelForm):
    class Meta:
        model = FileUpload
        fields = ['name']

    def save(self, commit=True):
        file = super(UploatForm, self).save()
        import_file.delay(file.id)
        read_excel.delay(file.id)
        return file