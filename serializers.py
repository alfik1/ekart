from rest_framework import serializers

from ekart.models import Category


class CategorySerializer(serializers.ModelSerializer):
    is_active=serializers.BooleanField(read_only=True)
    class Meta:
        model = Category
        fields =["category_name","is_active"]