from django.shortcuts import render
from django.http import HttpResponse
import ipam.functions as func
import ipam.assign_ip as aa
import json
#import socket, struct
# Create your views here.

from ipam.models import Audit, Host, Net, Locations, CustomNetColumnEntries, CustomNetColumns, Line, Site



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
    
    if 'red_num' in request.GET:
        sn = Net.objects.get(red_num = request.GET['red_num'])
        subnet = func.ip_to_long(sn.red)
        broadcast = subnet +255
    elif 'sn' in request.GET:
        sn = request.GET['sn']
        subnet = func.ip_to_long(sn)
        broadcast = subnet +255
    else:
        subnet = func.ip_to_long('172.22.200.1')
        broadcast = func.ip_to_long('172.22.200.255')

    ips = Host.objects.filter(ip__gt = subnet).filter(ip__lt =broadcast)

    for ip in ips:
        ip.ip = func.long_to_ip(int(ip.ip))

    context = {
        'id' : '0-5',
        'hosts' : ips,
    }

    return render(request, 'ip_entry.html', context)
    

def subnets(request):
    
    """
    if 'plant' in request.GET:
        subnets = Net.objects.filter(loc = request.GET['plant'])
    else:
        subnets = Net.objects.all()
    
    context = {
        'subnets' : subnets,
        
    }
    """
    db = func.db_connect()
    cursor = db.cursor()

    subnets = func.list_subnets(cursor)

    context = {
        'subnets' : subnets,
        
    }


    return render(request, 'subnets.html', context)
    
    #return HttpResponse(request.GET['plant'])

def ip_request(request):
    db = func.db_connect()
    cursor = db.cursor()

    subnets = func.list_site(cursor)

    context = {
        'subnets' : subnets,
        
    }


    return render(request, 'ip_request.html', context)
    
    """
    
    plants = Locations.objects.all()
    lines = CustomNetColumnEntries.objects.filter(cc_id=2)
    cells = CustomNetColumnEntries.objects.filter(cc_id=3)

    subnets = Net.objects.all()
    context = {
        'id' : '0-5',
        'subnets' : subnets,
        'plants': plants,
        'lines':lines,
        'cells':cells,
    }

    return render(request, 'ip_request.html', context)
    """

def assign(request):
   #http://127.0.0.1:8000/ipam/assign/?plant=plant 51&line=vss&cell=fa&count=3
    if 'plant' in request.GET:
        i_site = str(request.GET['plant'])
        i_line = request.GET['line']
        i_cell = request.GET['cell']
        count = int(request.GET['count'])
        #count = 6
       
        rlts = aa.assign_ip(i_site, i_line,i_cell,count)
        context = {
            'rlts':rlts,
        }
        return render(request, 'assign.html', context)

    else:
        return HttpResponse("Please request information first!!")
    """
    rlts = aa.assign_ip('plant 51','vss','fa',4)
    context = {
        'rlts':rlts,
    }
    return render(request, 'assign.html', context)
    """

def Map(request):
    return render(request,"map.html")
    #return HttpResponse("Hello!")
     
Place_dict = {
        "GuangDong":{
                        "GuangZhou":["PanYu","HuangPu","TianHe"],
                        "QingYuan":["QingCheng","YingDe","LianShan"],
                        "FoShan":["NanHai","ShunDe","SanShui"]
                        },
        "ShanDong":{
                        "JiNan":["LiXia","ShiZhong","TianQiao"],
                        "QingDao":["ShiNan","HuangDao","JiaoZhou"]
                        },
        "HuNan":{
                        "ChangSha":["KaiFu","YuHua","WangCheng"],
                        "ChenZhou":["BeiHu","SuXian","YongXian"]
                    }
    }

def Return_City_Data(request):
    province = request.GET['Province']
    
    City_list = []
    for city in Place_dict[province]:
        City_list.append(city)
    return HttpResponse(json.dumps(City_list))    
     
def Return_Country_Data(request):
    province,city = request.GET['Province'],request.GET['City']
    
    Country_list = Place_dict[province][city]
    return HttpResponse(json.dumps(Country_list))

##get the stationery list via stat_type_id from select list
def load_site(request):
    if request.method == 'GET':
        site_id = request.GET.get('site_id', None)
        print('get site_id from ajax "%s"'%(site_id))
        if site_id:
            data = list(Line.objects.filter(site_id=site_id).values("id", "name"))
            result=json.dumps(data)
            print(result)
    return HttpResponse(result, "json.html")
