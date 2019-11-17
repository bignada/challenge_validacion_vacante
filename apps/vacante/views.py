from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render
from .forms import VacanteDetailForm
from .ibm_api import ibm_ner
from .model_ibm import ModelFind
import json

class ValidarView(TemplateView):
    template_name = 'vacante/validar.html'

    def get(self, request):
        form = VacanteDetailForm()
        return render(request, self.template_name, {'form' : form})

    def post(self, request):
        if request.method == "POST":
            form = VacanteDetailForm(request.POST)
            if form.is_valid():
                data = ibm_ner.call_watson(self, texto = form.cleaned_data['descripcion'])
                data_load = json.loads(data)
                probabilidades = []

                for x in data_load['entities']:
                    probabilidades.append(ModelFind(x['type'],x['text'],x['count'],x['confidence']))


                return render(request, self.template_name, {'form' : form, 'data' : data, 'probabilidades' : probabilidades})
# Create your views here.
