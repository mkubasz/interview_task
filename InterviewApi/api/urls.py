from django.urls import path, include
from .views import CurrenciesView, DetailsView

urlpatterns = [
    path('currencies/', CurrenciesView.as_view(), name="currency-all"),
    path('currencies/<str:pk>/', DetailsView.as_view(), name="currency")
]
