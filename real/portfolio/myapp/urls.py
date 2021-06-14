from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import first, home, information

urlpatterns = [
    # path('', first, name='first'),
    path('', home, name='home'),
    path('information', information, name='information')
]