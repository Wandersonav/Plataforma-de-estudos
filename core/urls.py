from django.urls import path
from .views import CursoListCreateView, CursoRetrieveDestroyView

urlpatterns = [
   ## path('cursos/', CursoListView.as_view()),
    path('cursos/', CursoListCreateView.as_view(), name='curso-list-create'),
    path('cursos/<int:pk>/', CursoRetrieveDestroyView.as_view(), name='curso-retrieve-destroy'),

]
