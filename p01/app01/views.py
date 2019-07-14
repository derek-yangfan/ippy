from django.shortcuts import render
from django.http import HttpResponse
from app01.models import Audit, Host

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