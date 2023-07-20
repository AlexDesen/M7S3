



from rest_framework.viewsets import  ModelViewSet
from rest_framework.permissions import IsAuthenticated
from reservando.models import Reserva
from rest_api.serializers import AgendamenetoModelSerializers



class AgendamentoModelViewSet(ModelViewSet):

    queryset = Reserva.objects.all()
    serializer_class = AgendamenetoModelSerializers
    permission_classes = [IsAuthenticated]
   
   


