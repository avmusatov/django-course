from rest_framework import serializers
from .models import Pet, Donation, Leadership


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ('id',
                  'name',
                  'kind',
                  'age',
                  'description',
                  'sex',
                  'sterilization',
                  'toilet',
                  'image_path')


class LeadershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leadership
        fields = ('id',
                  'name',
                  'position',
                  'description',
                  'image_path')


class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = ('id',
                  'amount',
                  'message',
                  'date',
                  'email',
                  'contact_name')
