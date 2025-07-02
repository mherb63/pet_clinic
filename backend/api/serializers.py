from rest_framework import serializers
from .models import Owners, Pets, Vets, Vaccines, PetVaccines

class OwnersSerializer(serializers.ModelSerializer):
    pet_ids = serializers.PrimaryKeyRelatedField(many=True, read_only=True, source='pets')
    
    class Meta:
        model = Owners
        fields = '__all__'  

class PetsSerializer(serializers.ModelSerializer):
    owner = OwnersSerializer(read_only=True)  

    class Meta:
        model = Pets
        fields = '__all__'  

class VetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vets
        fields = '__all__'  

class VaccinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaccines
        fields = '__all__'  


class PetVaccinesSerializer(serializers.ModelSerializer):
    pet = PetsSerializer(read_only=True)
    pet_id = serializers.PrimaryKeyRelatedField(
        queryset=Pets.objects.all(), source='pet', write_only=True
    )

    vaccine = VaccinesSerializer(read_only=True)
    vaccine_id = serializers.PrimaryKeyRelatedField(
        queryset=Vaccines.objects.all(), source='vaccine', write_only=True
    )


    class Meta:
        model = PetVaccines
        fields = '__all__'  

