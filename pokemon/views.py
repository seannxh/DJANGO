from rest_framework.viewsets import ModelViewSet
from .models import Pokemon
from .serializers import PokemonSerializer

class PokemonViewSet(ModelViewSet):
    queryset = Pokemon.objects.all()  # Ensures data is fetched from the database
    serializer_class = PokemonSerializer  # Specifies the serializer
