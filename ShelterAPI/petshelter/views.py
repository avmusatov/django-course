from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from petshelter.models import Pet, Leadership, Donation
from petshelter.serializers import PetSerializer, LeadershipSerializer, DonationSerializer


class PetView(APIView):
    def get(self, request):
        pets = Pet.objects.all()
        pet_serializer = PetSerializer(pets, many=True)
        return Response(pet_serializer.data)

    def post(self, request):
        pet_serializer = PetSerializer(data=request.data)
        if pet_serializer.is_valid():
            pet_serializer.save()
            return Response(pet_serializer.data, status=status.HTTP_201_CREATED)
        return Response(pet_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        pet = get_object_or_404(Pet, id=id)
        pet_serializer = PetSerializer(pet, data=request.data)
        if pet_serializer.is_valid():
            pet_serializer.save()
            return Response(pet_serializer.data)
        return Response(pet_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        pet = get_object_or_404(Pet, id=id)
        pet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
