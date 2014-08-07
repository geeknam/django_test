import time 

from django import forms
from django.views.generic.edit import FormView
from django.contrib import messages

from importer import import_data



class UploadFileForm(forms.Form):
    data_file = forms.FileField()

    def import_data(self):
        data = self.cleaned_data['data_file']
        return import_data(data)

class DataImportView(FormView):
    template_name = 'index.html'
    form_class = UploadFileForm
    success_url = '/'

    def form_valid(self, form):
        start = time.time()
        lines_imported = form.import_data()
        processing = time.time() - start
        messages.add_message(self.request, messages.INFO, 'Time taken to import: %s seconds' % str(processing))
        messages.add_message(self.request, messages.INFO, 'Number of lines imported: %s' % str(lines_imported))
        return super(DataImportView, self).form_valid(form)