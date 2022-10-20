from django.urls import path
from .views import index
from .views import updateDelete


urlpatterns = [
    path('', index),
    path('<int:id>', updateDelete)
]
