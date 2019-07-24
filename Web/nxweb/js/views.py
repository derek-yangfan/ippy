from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from .models import Client, City
from .forms import ClientForm
from django.http import JsonResponse


# Create your views here.！



class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'client_form.html'


class ClientDetailView(DetailView):
    model = Client

def ajax_load_cities(request):
    if request.method == 'GET':
        country_id = request.GET.get('country_id', None)
        if country_id:
            data = list(City.objects.filter(country_id=country_id).values("id", "name"))
            return JsonResponse(data, safe=False)
