from rest_framework import viewsets
from cliente.serializer import ClienteSerielizer
from cliente.models import Cliente

class ClientesViewSet(viewsets.ModelViewSet):
    """ Listando todos os clientes """
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerielizer