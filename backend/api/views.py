from django.http import Http404, JsonResponse
from rest_framework import generics
from .models import Owners, Pets, Vets, Vaccines, PetVaccines
from .serializers import OwnersSerializer, PetsSerializer, VetsSerializer, VaccinesSerializer, PetVaccinesSerializer
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class OwnersListCreate(generics.ListCreateAPIView):
    queryset = Owners.objects.all()
    serializer_class = OwnersSerializer
    permission_classes = [IsAuthenticated]

class OwnerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Owners.objects.all()
    serializer_class = OwnersSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]

class OwnerWithPetsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        try:
            owner = Owners.objects.get(id=id)
        except Owners.DoesNotExist:
            raise NotFound("Owner not found")

        owner_serializer = OwnersSerializer(owner)
        pets = Pets.objects.filter(owner=owner)
        pets_serializer = PetsSerializer(pets, many=True)

        return Response({
            'owner': owner_serializer.data,
            'pets': pets_serializer.data
        })

class PetsListCreate(generics.ListCreateAPIView):
    queryset = Pets.objects.all()
    serializer_class = PetsSerializer
    permission_classes = [IsAuthenticated]

class PetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pets.objects.all()
    serializer_class = PetsSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]

class VetsListCreate(generics.ListCreateAPIView):
    queryset = Vets.objects.all()
    serializer_class = VetsSerializer
    permission_classes = [IsAuthenticated]

class VetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vets.objects.all()
    serializer_class = VetsSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]

class VaccinesListCreate(generics.ListCreateAPIView):
    queryset = Vaccines.objects.all()
    serializer_class = VaccinesSerializer
    permission_classes = [IsAuthenticated]

class VaccineDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vaccines.objects.all()
    serializer_class = VaccinesSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]

class PetVaccinesListCreate(generics.ListCreateAPIView):
    queryset = PetVaccines.objects.all()
    serializer_class = PetVaccinesSerializer
    permission_classes = [IsAuthenticated]

class PetVaccineDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PetVaccines.objects.all()
    serializer_class = PetVaccinesSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]

