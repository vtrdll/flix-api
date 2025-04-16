from rest_framework import generics
from genres.models import Genre
from genres.serializers import GenreSerializers


class GenreCreateListView (generics.ListCreateAPIView):

    queryset = Genre.objects.all()
    serializer_class = GenreSerializers


class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Genre.objects.all()
    serializer_class = GenreSerializers
