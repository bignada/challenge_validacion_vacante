from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render
from .forms import VacanteDetailForm

class ValidarView(TemplateView):
    template_name = 'vacante/validar.html'

    def get(self, request):
        form = VacanteDetailForm()
        return render(self.template_name, {'form' : form})

    def post(self, request):
        if request.method == "POST":
            form = VacanteDetailForm(request.POST)
            if form.is_valid():
                return render(self)
# Create your views here.
