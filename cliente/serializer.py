from rest_framework import serializers
from cliente.models import Cliente

class ClienteSerielizer(serializers.ModelSerializer):
    """ Exibindo todos os clientes """
    
    class Meta:
        model = Cliente
        fields = '__all__'
