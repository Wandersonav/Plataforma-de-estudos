from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Curso
from .serializers import CursoSerializer
from django.shortcuts import render
from rest_framework import generics

## class CursoListView(APIView):
##    def get(self, request):
##        cursos = Curso.objects.all()
##        serializer = CursoSerializer(cursos, many=True)
##        return Response(serializer.data)


# Endpoint para listar todos os cursos (GET) e criar um novo curso (POST)
class CursoListCreateView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

# Endpoint para buscar um único curso (GET) e excluir (DELETE)
class CursoRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

