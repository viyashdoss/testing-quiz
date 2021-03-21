from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import api_view,permission_classes
from .serializers import testSerializer,categorySerializer,optionSerializer
from .models import *
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated,IsAdminUser

@api_view(['GET'])
def category(request):
    query=Category.objects.all()
    serializer=categorySerializer(query,many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def question(request,name):
    paginator = PageNumberPagination()
    paginator.page_size = 1
    query=Options.objects.filter(category=name)
    context = paginator.paginate_queryset(query, request)
    serializer=optionSerializer(context,many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def test(request):
    serializer=testSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

