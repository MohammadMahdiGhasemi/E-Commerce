#!/bin/bash
set -x

python3 -m venv .venv


source .venv/bin/activate


pip install django


django-admin startproject core .


echo "Enter app name:"
read appname


python3 manage.py startapp $appname


echo "Configuring settings.py..."


sed -i "/INSTALLED_APPS = \[/a\ \ \ \ '$appname'," core/settings.py


echo "Configuring urls.py..."

sed -i "/from django.urls import path/a\from django.urls import include " core/urls.py

sed -i "/path('admin\/', admin.site.urls),/a\ \ \ \ path('$appname/', include('$appname.urls'))," core/urls.py


echo "Creating $appname/urls.py..."
echo "from django.urls import path , include" > $appname/urls.py
sed -i "/from django.urls import path/a\urlpatterns = [] " $appname/urls.py


echo "Django project setup completed!"
