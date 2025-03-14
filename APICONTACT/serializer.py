from rest_framework import serializers
from .models import Contacto
#Esto es una importacion de Python y sirve para validar patrones
import re

class ContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacto
        fields = '__all__'

    def validate_phone(self, value):
        #Esto es lo que se utliza para identificar el patron, 'r' es el prefijo de raw string 
        '''
        '^': Indicador de que inicia el string
        '\+?': este es que puede o no llevar +
        '\d{10,15}$' esto es que puede ser un string entre 10 a 15 y el $ es que termina y el \d es que solo admite numeros
        '''
        patron = r'^\+?\d{10,15}$'

        #Metodos comunes:
        '''
        re.match: verifica que el texto conincida con el patron desde el inicio
        re.seacrh: busca conicidencia entre el patron y el texto
        re.findall: encuentra todas las coincidencias en el texto
        '''
        if not re.match(patron, value):
            raise serializers.ValidationError('Numero erroneo')
        
        return value

