from django.shortcuts import render

import requests
import json
url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "111988be39msh8282b8a0887d7d5p1039dajsnc9415f239aa1",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()

# Create your views here.
def helloview(request):
    noofresults=int(response['results'])
    covidlist=[]
    for i in range(0,noofresults):
        country=response['response'][i]['country']
        covidlist.append(country)
    if request.method=="POST":
        selectedcountry=request.POST['selectedcountry']
        for x in range(0,noofresults):
            if(selectedcountry==response['response'][x]['country']):
                new=response['response'][x]['cases']['new']
                active=response['response'][x]['cases']['active']
                critical=response['response'][x]['cases']['critical']
                recovered=response['response'][x]['cases']['recovered']
                total=response['response'][x]['cases']['total']
                deaths=int(total)-int(active)-int(recovered)
        context={'covidlist':covidlist,'new':new,'active':active,'critical':critical,'recovered':recovered,'total':total,'deaths':deaths,'selectedcountry':selectedcountry}
        return render(request,'index.html',context)
    context={'covidlist':covidlist}
    return render(request,'index.html',context)
