from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Curso
from .serializers import CursoSerializer

class CursoListView(APIView):
    def get(self, request):
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data)
from django.shortcuts import render

# Create your views here.
