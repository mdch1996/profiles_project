from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers
from . import models


class HelloApiView(APIView):

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):

            an_apiview = [
                "ba slalm",
                "how are u?",
                "whats your name?"
            ]

            return Response({'message': "hello world", 'an_apiview': an_apiview})

    def post(self, request):

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            # message = 'Hello {0}'.format(name)
            return Response({'message': name})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):

        return Response({'methode': 'put'})

    def patch(self, request, pk=None):

        return Response({'methode': 'patch'})

    def delete(self, request, pk=None):

        return Response({'methode': 'delete'})


class HelloViewSet(viewsets.ViewSet):

    serializer_class = serializers.HelloSerializer

    def list(self, request):

        a_viewset = [
            'uses actions (list, create, retrieve, update, partial_update)',
            'automatically map to urls'
        ]

        return Response({'message': 'hello', 'a_viewset': a_viewset})

    def create(self, request):

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):

        return Response({'message': 'GET'})

    def update(self, request, pk=None):

        return Response({'message': 'put'})

    def partial_update(self, request, pk=None):

        return Response({'message': 'patch'})

    def destroy(self, request, pk=None):

        return Response({'message': 'delete'})


class UserProfileViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
