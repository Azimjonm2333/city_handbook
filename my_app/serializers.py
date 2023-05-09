from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from my_app.models import Category, Contact, School, Town


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ("phone", "additionalPhone", "working_mode", "email")
    
    def get_custom_field(self, instance):
        return instance.place.title


class CategoryFullSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"
    
    def to_representation(self, instance, *args, **kwargs):
        data = super(CategoryFullSerializer, self).to_representation(instance)
        return data["title"]


class TownSerializer(serializers.ModelSerializer):

    class Meta:
        model = Town
        fields = "__all__"

    def to_representation(self, instance, *args, **kwargs):
        data = super(TownSerializer, self).to_representation(instance)
        return data["name"]


class SchoolSerializer(serializers.ModelSerializer):

    email = serializers.CharField(source="contact.email")
    phone = serializers.CharField(source="contact.phone")
    additionalPhone = serializers.CharField(source="contact.additionalPhone")
    working_mode = serializers.CharField(source="contact.working_mode")
    image = serializers.CharField(source="contact.image")

    contact = ContactSerializer()
    categories = CategoryFullSerializer()
    town = TownSerializer()
    
    class Meta:
        model = School
        fields = "__all__"


class SchoolCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = School
        fields = "__all__"

    def create(self, validated_data):
        return super().create(validated_data)