# django_steps

**With Anaconda already install follow these steps:**

**on terminal:**

$ conda create --name venvname

$ source activate venvname

$ django-admin startproject projectname

$ cd projectname

$ python manage.py startapp AppName

 **in AppName/Views.py file add:**


 ```python


 from django.shortcuts import render

 # Create your views here.

 def index(request):
     my_dict = {'insert_content': "Hello! I'm from first app"}
     return render (request, 'index.html', context= my_dict)

```

**add a new file at "AppName/" and call it urls.py**

**in this new file (urls.py) write:**

```python

from django.urls import  path
from firstApp import views

urlpatterns = [

        path(r'^$', views.index, name = 'index'),
]


```
**go to projectname/urls.py and add:**

```python

from django.contrib import admin
from django.urls import path, include, re_path
from firstApp import views


urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path(r'^$', views.index, name='index'),
    re_path(r'^firstApp/', include("firstApp.urls"))

]

```
