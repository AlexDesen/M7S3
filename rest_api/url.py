from django.urls import path
from rest_api.views import hello_wolrd
# from rest_api.views import categoria, adicionar_categoria
from rest_api.views import CategoriaViewSet


from rest_framework.routers import DefaultRouter,SimpleRouter
from rest_api.views import AgendamentoModelViewSet
from rest_api.views import EventoModelViewSet


   # A função processada na views retorna uma página html já na app retorna um json

# O router é um gerenciador de rotas
router = DefaultRouter()# O "trailing_slash=False"- é para não usarmos a barra no finl da url.
#categoria é passada como prefixo na função register()
router.register('categoria',CategoriaViewSet,basename='categoria')
router.register('agendamento', AgendamentoModelViewSet)
router.register('eventos',EventoModelViewSet, basename='eventos')


app_name = 'rest_api'
urlpatterns = [
    path('hello_world', hello_wolrd, name='hello_world_app'),
    # path('categoria/',categoria, name = 'categoria'),
    # path('criar_categoria/',adicionar_categoria, name ='criar_categoria'),
    # path('eventos/',eventos, name ='eventos'),
]

# agora urlpatterns gurdará também as urls do router
urlpatterns = urlpatterns + router.urls


