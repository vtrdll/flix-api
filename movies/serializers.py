from rest_framework import serializers
from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):


    class Meta:
        model = Movie
        fields = '__all__'

    def validate_relase_date(self, value):
        if value < 1900:
            raise serializers.ValidationError('A data de lançamento precisa ser menor que 1900.')
        return value 
    
    