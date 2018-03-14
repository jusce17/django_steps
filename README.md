# django_steps

**With Anaconda already install follow these steps:**

_on terminal_

$ conda create --name venvname

$ source activate venvname

$ django-admin startproject projectname

$ cd projectname

$ python manage.py startapp AppName

 _in Views.py file add:_


 ```python


 from django.shortcuts import render

 # Create your views here.

 def index(request):
     my_dict = {'insert_content': "Hello! I'm from first app"}
     return render (request, 'index.html', context= my_dict)

```
