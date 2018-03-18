# django_steps

baby steps to launch a webapp made in Django 2.0

**With Anaconda already install follow these steps:**

**on terminal:**
```sh
$ conda create --name venvname

$ source activate venvname

$ django-admin startproject projectDjango

$ cd projectDjango

$ python manage.py startapp firstApp

```

 **in firstApp/Views.py file add:**


 ```python


 from django.shortcuts import render

 # Create your views here.

 def index(request):
     my_dict = {'insert_content': "Hello! I'm from first app"}
     return render (request, 'firstApp/index.html', context= my_dict)

```

**add a new file at "firstApp/" and call it urls.py**

**in this new file (urls.py) write:**

```python

from django.urls import  re_path
from firstApp import views

urlpatterns = [

        re_path(r'^$', views.index, name = 'index'),
]


```
**go to projectDjango/urls.py and add:**

```python

from django.contrib import admin
from django.urls import  include, re_path
from firstApp import views


urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path(r'^$', views.index, name='index'),
    re_path(r'^firstApp/', include("firstApp.urls"))

]

```

**In the same directory as projectDjango and firstApp add 2 new folders**
**name the folders "templates" and "statics"**

**inside of the new folder "templates" add another folder with the same name as your app "firstApp"**

**inside of templates create a file "index.html"**

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

**now go to *projectDjango/projectDjango/settings.py* to let our project know how we want him to work**

add the following code to **settings.py**

After
```python
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

```

add:

```python
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'statics')
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
