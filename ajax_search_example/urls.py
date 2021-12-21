import rest_framework
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("app.urls")),
    # path("api-drf/",include("rest_frameworks.urls")),
]
