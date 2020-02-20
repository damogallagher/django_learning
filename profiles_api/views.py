from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers

class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)'
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, primary_key=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, primary_key=None):
        """Handle a partial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, primary_key=None):
        """Handle the delete of an object"""
        return Response({'method': 'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update',
            'Automatically maps to URLs using Routes',
            'Provides more functionality with less code'
        ]

        return Response({'message': 'Hello', 'a_viewset': a_viewset})

    def create(self, request):
        """Cfreate a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, primary_key=None):
        """Handle getting an object by its Id"""
        return Response({'http_method': 'GET'})

    def update(self, request, primary_key=None):
        """Handle updating an object by its Id"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, primary_key=None):
        """Handle partially updating an object by its Id"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, primary_key=None):
        """Handle deleting an object by its Id"""
        return Response({'http_method': 'DELETE'})