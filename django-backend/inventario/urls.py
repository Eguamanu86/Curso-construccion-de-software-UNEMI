from django.urls import path
from .views import ProductoListView

urlpatterns = [
    path('productos', ProductoListView.as_view(), name='productos'),
]
