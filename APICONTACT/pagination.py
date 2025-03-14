from rest_framework import pagination
#Esto es una importacion de DRF que es la paginacion, esto se puede realizar de 
#dos formas: Desde settings para la paginazion de manera global aplicabe a todas las views
#y esta tambien existe la forma de aplicarlo de manera individual, de que creando una clase en 
#un script nuevo e importando pagination 

class ContactPagination(pagination.PageNumberPagination):
    page_size = 1
    page_size_query_param = 'size'
    max_page_size = 1000

#page_size: este indica cuando se llama a un get el numero sera la cantidad de resultados que apareceran
#page_size_query_param: este es el string que el usuario utlizara para cambiar el page_size a un numero que el quiera
#si el usuario quiere que en lugar de 1 elemento le aparescan 10 nomas pone ?size=10 y con eso la paginacion se vuelve de 10
#max_page_size: este es el numero maximo de paginas que puede aver 