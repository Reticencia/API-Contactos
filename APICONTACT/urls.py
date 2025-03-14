from django.urls import path
from .views import CreateAndGet, SearchAndPut

urlpatterns = [
    path('Contactos/', CreateAndGet.as_view()),
    path('Contactos/<str:name>', SearchAndPut.as_view()),
]