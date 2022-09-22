from django.db.migrations import serializer
from django.shortcuts import render
from rest_framework import permissions


from rest_framework.viewsets import ModelViewSet,ViewSet
# Create your views here.
from ekart.models import Category
from ekart.serializers import CategorySerializer


class CategoryView(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes=[permissions.IsAdminUser]
