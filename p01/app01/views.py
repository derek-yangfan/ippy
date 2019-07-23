from django.shortcuts import render
from django.http import HttpResponse
from app01.models import Audit, Host, Net, Locations
from .forms import AddForm

# Create your views here.
def index(request):
    context = {}
    event2 = [1,3,5,6,7,9]
    list = Host.objects.order_by("id")[0:10]
    
    context = {'id': event2, 'hosts':list}
    #for ip in list:
       # event1['ip'] =ip.ip
        #event2.append(ip.hostname)

    #event1 = Host.objects.order_by("ip")[0:2]

    #return HttpResponse(list)
    return render(request, 'home.html', context)

def iplist(request):
    list = Host.objects.order_by("id")[0:20]

    context = {'hosts':list}
    return render(request, 'iplist.html', context)

def assign(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = int(a)+int(b)
            return render(request, 'assign.html', {'form': form, 'rlt':c})
    else:
        form = AddForm()
        return render(request, 'assign.html', {'form': form})

def subnets(request):
    subnets = Net.objects.all()
    
    context = {
        'subnets':subnets,
    }

    return render(request, 'subnets.html', context)

