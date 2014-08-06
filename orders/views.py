from django import forms
from django.views.generic.edit import FormView
from importer import import_data


class UploadFileForm(forms.Form):
    data_file = forms.FileField()

    def import_data(self):
        data = self.cleaned_data['data_file']
        import_data(data)

class DataImportView(FormView):
    template_name = 'index.html'
    form_class = UploadFileForm
    success_url = '/'

    def form_valid(self, form):
        form.import_data()
        return super(DataImportView, self).form_valid(form)