from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    try:
        context = {
            'title' : "BrainCache"
        }
        return render(request= request, context= context, template_name="home/index.html")
    except:
        return HttpResponse(content="Something is going on in this universe !!")