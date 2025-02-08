from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('reader', views.ReaderViewSet)
router.register('book', views.BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]