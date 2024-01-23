
from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('about/',about,name='about'),
    path('registration/',registration,name='registration'),
    path('login/',login,name='login'),
    path('Savedata/',Savedata,name='Savedata'),  
    path('dash/',dash,name='dash'),
    path('LoginPage/',LoginPage,name='LoginPage'),
    path('delete/',delete,name='delete')
]
