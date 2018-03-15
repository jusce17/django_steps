# django_steps

baby steps to launch a webapp made in Django 2.0

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

**Now go to projectname/projectname and add two (3) new folders**
**name this folder "templates" and "statics/images"**

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
STATIC_DIR = os.path.join(BASE_DIR, 'static')
```

After
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',        

```

Add:
```python

'DIRS': [TEMPLATE_DIR,],

```

Add this to the end of the file
```python
STATICFILES_DIRS = [
    STATIC_DIR,

]

```



In order to load the static files, edit the index.html file

```html
<!DOCTYPE html>
 {% load staticfiles %}

<!— to load images —>
<img src="{%static "images/image1.png" %}" alt="image not loaded" width="200" height="200"/>

```
