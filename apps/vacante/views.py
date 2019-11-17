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
        diccionario = {
            'habilidades_requeridas':[3,5,0,0], 
            'experiencia':[3,2,0,0], 
            'prestaciones' : [1,2,0,0], 
            'sueldos' : [1,1,0,0], 
            'habilidades_deseadas':[1,5,0,0], 
            'tareas_a_ejecutar' : [1,5,0,0]}
                
        if request.method == "POST":
            form = VacanteDetailForm(request.POST)
            if form.is_valid():
                descripcion = form.cleaned_data['descripcion']
                descripcion = descripcion.strip()
                if len(descripcion) > 100:
                    data = ibm_ner.call_watson(self, texto = descripcion)
                    data_load = json.loads(data)
                    probabilidades = []
                    promedio = 0; 

                    for x in data_load['entities']:
                        probabilidad = ModelFind(x['type'],x['text'],x['count'],x['confidence'])
                        probabilidades.append(probabilidad)
                        diccionario[probabilidad.type][2] += 1
                    
                    for x in diccionario:
                        prob = diccionario.get(x)
                        diccionario.get(x)[3]= (prob[2] / (prob[1] if prob[2] < prob[1] else prob[2])) * prob[0]
                        promedio += diccionario.get(x)[3]

                    return render(request, self.template_name, {'form' : form, 'data' : data, 'probabilidades' : probabilidades, 'diccionario' : diccionario, 'promedio' : promedio})
                else:
                    return render(request, self.template_name, {'form' : form})
            else:
                return render(request, self.template_name, {'form' : form})
# Create your views here.
