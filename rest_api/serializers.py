from rest_framework.serializers import ModelSerializer
from reservando.models import Reserva

class AgendamenetoModelSerializers(ModelSerializer):
# Atribuimos o modelo Reserva ao serializers através da classe Meta Semelhante ao que 
# fazemos no ModelForm
    class Meta:
        model = Reserva
        fields = "__all__"
        