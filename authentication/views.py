from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from authentication.serializers import RegisterSerializer, LoginSerializer
from rest_framework import response, status, permissions
from django.contrib.auth import authenticate

# Create your views here.

class AuthUserAPIView(GenericAPIView):
    """
    View to retrieve authenticated user information.
    Requires authentication.

    GET request:
    - Returns information about the authenticated user.

    Permissions:
    - Requires the user to be authenticated.
    """
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        """
        Retrieve authenticated user information.

        Returns:
        - Serialized data of the authenticated user.
        """
        user = request.user
        serializer = RegisterSerializer(user)
        return response.Response({'user': serializer.data})


class RegisterAPIView(GenericAPIView):
    # all everyone to access this view
    authentication_classes = []
    """
    View to register a new user.

    POST request:
    - Registers a new user with the provided data.

    Permissions:
    - No special permissions required.
    """
    class_serializer = RegisterSerializer

    def post(self, request):
        """
        Register a new user.

        Returns:
        - Serialized data of the registered user.
        """
        serializer = self.class_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(GenericAPIView):
    # all everyone to access this view
    authentication_classes = []
    """
    View to authenticate a user.

    POST request:
    - Authenticates a user with the provided credentials.

    Permissions:
    - No special permissions required.
    """
    class_serializer = LoginSerializer

    def post(self, request):
        """
        Authenticate a user.

        Returns:
        - Serialized data of the authenticated user if successful.
        - Error message if authentication fails.
        """
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        user = authenticate(username=email, password=password)

        if user:
            serializer = self.class_serializer(user)
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        return response.Response({'message': "Invalid credentials, try again"}, status=status.HTTP_401_UNAUTHORIZED)
