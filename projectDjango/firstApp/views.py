from django.shortcuts import render

# Create your views here.

def index(request):
    my_dict = {'insert_content': "Hello! I'm from first app"}
    return render (request, 'firstApp/index.html', context= my_dict)
