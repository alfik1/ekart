from django.urls import path
from rest_framework.routers import DefaultRouter
from ekart import views

router=DefaultRouter()
router.register("categories",views.CategoryView,basename="categories")

urlpatterns = [
    ]+router.urls