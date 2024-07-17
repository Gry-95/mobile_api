from django.urls import path
from .views import ShopListView, VisitCreateView

urlpatterns = [
    path('shops/', ShopListView.as_view(), name='shop-list'),
    path('visits/', VisitCreateView.as_view(), name='visit-create'),
]