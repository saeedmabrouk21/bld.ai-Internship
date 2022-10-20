from django.http import HttpResponse
from django.http import JsonResponse
import json

from django.shortcuts import render
# Create your views here.
listObj = []

with open("mainMenu/data.json") as fp:
    listObj = json.load(fp)


def index(request):
    if request.method == "GET":
        return JsonResponse(listObj,safe=False)
    elif request.method == "POST":
        listObj.append(json.loads(request.body))
        with open("mainMenu/data.json", 'w') as json_file:
            json.dump(listObj, json_file, indent=4, separators=(',', ': '))
        return JsonResponse(json.loads(request.body))


def updateDelete(request, id):
    if (request.method == "PUT"):
        for i in range (0,len(listObj)):
            if(listObj[i]['id']==id):
                listObj[i]= json.loads(request.body);
                break
        with open("mainMenu/data.json", 'w') as json_file:
            json.dump(listObj, json_file, indent=4, separators=(',', ': '))
        return JsonResponse(json.loads(request.body))




    elif (request.method =='DELETE'):
        index = -1
        for i in range (0,len(listObj)):
            if(listObj[i]['id']==id):
                del listObj[i]
                break
        with open("mainMenu/data.json", 'w') as json_file:
            json.dump(listObj, json_file, indent=4, separators=(',', ': '))
        return JsonResponse({"message" : "deleted"})
