# django_steps

**With Anaconda already install follow these steps:**

**on terminal:**

>*$ conda create --name venvname*

>*$ source activate venvname*

>*$ django-admin startproject projectname*

>*$ cd projectname*

>*$ python manage.py startapp AppName*

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
from AppName import views

urlpatterns = [

        path(r'^$', views.index, name = 'index'),
]


```
**go to projectname/urls.py and add:**

```python

from django.contrib import admin
from django.urls import path, include, re_path
from AppName import views


urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path(r'^$', views.index, name='index'),
    re_path(r'^AppName/', include("AppName.urls"))

]

```

**Now go to projectname/projectname and a new folder**
**name this folder "templates"**

**inside of the new folder "templates" add another folder with the same name as your app "AppName"**

**inside of projectname/projectname/templates create a file "index.html"**

**in the index.html add:**

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>HEllo</title>
  </head>
  <body>

    <h1>Hello this is a test page!</h1>
    <h2>{{ insert_content}}</h2>

  </body>
</html>

```

**now go to *projectname/projectname/settings.py* to let our project know how we want him to work**

add the following code to **settings.py**

After
```python
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

```

add:

```python
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
```
