from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello_world(request):
    
    if request.method == "POST":
        
        temp = request.POST.get('hello_world_input')
        
        
        return render(request, 'accountapp/hello_world.html', context={"text":temp})
    else:
        return render(request, 'accountapp/hello_world.html', context={"text":"GET METHOD"})
