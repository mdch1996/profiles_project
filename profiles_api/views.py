from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers

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


class HelloViewset(viewsets.ViewSet):

    def list(self, request):

        a_viewset = [
            'uses actions (list, create, retrieve, update, partial_update)',
            'automatically map to urls'
        ]

        return Response({'message': 'hello', 'a_viewset': a_viewset})
