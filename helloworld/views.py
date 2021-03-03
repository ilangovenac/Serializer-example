from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView
from .serializers import PostSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Post
from rest_framework.permissions import IsAuthenticated

class helloworldview(APIView):
    def get(self,request):
        return Response({'info':'hello world'})

class postview(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class=PostSerializer
