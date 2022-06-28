from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.

def http_response(request):
    if request.method == "GET":
        return HttpResponse("Hello World!")

def json_response(request):
    if request.method == "GET":

        data = {
            'name' : 'minseo',
            'school' : 'CAU'
        }

        return JsonResponse(data=data)

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name') # <input type="text" !!name="name"!! value="이름을 적어주세요">
        
        data = {
            'name' : name
        }

        return render(request, 'index.html', context=data)

    else:
        return render(request, 'index.html')
