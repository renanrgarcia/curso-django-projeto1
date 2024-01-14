from django.urls import path
from recipes.views import contato, home, sobre


urlpatterns = [
    path('', home),  # Home
    path('contato/', contato),
    path('sobre/', sobre),
]
