from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from .views import *

urlpatterns = [
    path('owners/', OwnersListCreate.as_view(), name='owners-list-create'),
    path('owners/<int:id>/', OwnerDetail.as_view(), name='owner-detail'),
    path('owners/<int:id>/pets/', OwnerWithPetsView.as_view(), name='owner-with-pets'),

    path('pets/', PetsListCreate.as_view(), name='pets-list-create'),
    path('pets/<int:id>/', PetDetail.as_view(), name='pet-detail'),

    path('vets/', VetsListCreate.as_view(), name='vets-list-create'),
    path('vets/<int:id>/', VetDetail.as_view(), name='vet-detail'),

    path('vaccines/', VaccinesListCreate.as_view(), name='vaccines-list-create'),
    path('vaccines/<int:id>/', VaccineDetail.as_view(), name='vaccine-detail'),

    path('pet-vaccines/', PetVaccinesListCreate.as_view(), name='pet-vaccines-list-create'),
    path('pet-vaccines/<int:id>/', PetVaccineDetail.as_view(), name='pet-vaccine-detail'),
]
