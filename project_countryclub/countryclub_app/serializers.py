from rest_framework import serializers
from django_countries.fields import CountryField

from .models import Club, ClubMembers


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        # fields = ['city', 'address', 'country']
        fields = '__all__'


class ClubMembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubMembers

        fields = '__all__'
