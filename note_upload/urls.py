
from django.urls import path, include
from . import views
urlpatterns = [
    
    path('', include('registration.urls')),
    path('notes/', views.home, name='home'),
    path('upload/', views.upload_note, name='upload_note'),
]
