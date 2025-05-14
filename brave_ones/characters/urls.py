from django.urls import path
from .views import CharacterListCreate, CharacterDetail

urlpatterns = [
    path('characters/', CharacterListCreate.as_view(), name='character-list-create'),
    path('characters/<int:pk>/', CharacterDetail.as_view(), name='character-detail'),
]