from django.shortcuts import render
from rest_framework import generics,status
from .models import Contacto
from .serializer import ContactoSerializer
from .pagination import ContactPagination
from rest_framework.views import APIView
from rest_framework.response import Response



# Create your views here.

'''
class CreateAndGet(generics.ListCreateAPIView):
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializer
    pagination_class = ContactPagination


class SearchAndPut(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializer
    lookup_field = 'name' 
    #Default Django use the pk, but in this case want to use a differents lookup_field
    #i need define a new lookup_field in the view   
'''
class CreateAndGet(APIView):

    def get(self, request):
        
        lol = Contacto.objects.all()

        paginacion = ContactPagination()

        page = paginacion.paginate_queryset(lol, request)

        serializer = ContactoSerializer(page, many=True)

        return paginacion.get_paginated_response(serializer.data)
    
    def post(self, request):

        serializer = ContactoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        
class SearchAndPut(APIView):

    def get(self, request, name):

        contacto = Contacto.objects.get(name=name)

        serializer = ContactoSerializer(contacto)

        return Response(serializer.data)


    def put(self, request, name):
        try:
            contacto = Contacto.objects.get(name=name)
        except:
            return Response({'Error':'Dato no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ContactoSerializer(contacto, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        
    def delete(self, request, name):

        contacto = Contacto.objects.get(name=name)

        contacto.delete()

        return Response({'Dato': 'Eliminado'}, status=status.HTTP_204_NO_CONTENT)
        
'''
Documentacion:
Explicacion con respecto a la paginacion, class CreateAndGet(APIView):, explicacion de las partes que nose:

lo segundo que hace es crear una instacia del paginador
para luego dividir los contactos en paginas segun el request 
para que el serializer solo serialize los contacots de la pagina actual

En la segunda View:

para cambiar el lookup_fields, solo en lugar de ponerle pk, puedes usar el campo que quieres para utlizarlo para buscar
'''
        
        

