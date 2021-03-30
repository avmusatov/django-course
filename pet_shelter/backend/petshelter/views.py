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
        serializer = PetSerializer(pets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        pet = get_object_or_404(Pet, id=id)
        serializer = PetSerializer(pet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        pet = get_object_or_404(Pet, id=id)
        pet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DonationView(APIView):
    def get(self, request):
        donations = Donation.objects.all()
        serializer = DonationSerializer(donations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DonationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        donation = get_object_or_404(Donation, id=id)
        serializer = DonationSerializer(donation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        donation = get_object_or_404(Donation, id=id)
        donation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class LeaderView(APIView):
    def get(self, request):
        leaders = Leadership.objects.all()
        serializer = LeadershipSerializer(leaders, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LeadershipSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        leader = get_object_or_404(Leadership, id=id)
        serializer = LeadershipSerializer(leader, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        leader = get_object_or_404(Leadership, id=id)
        leader.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)