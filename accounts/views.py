from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import RegisterSerializer
from rest_framework.generics import CreateAPIView
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token 
from rest_framework.permissions import IsAuthenticated
from .permissions import IsNotAuthenticated

""" class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid:
            serializer.save()
            return Response({
                "msg": "Usuario Creado",
                "Username": user.username,
                "email": user.email
            }, status= 201)
            
        return Response(serializer.errors, status=400) """
        
class ResgisterView(CreateAPIView):
    permission_classes = [IsNotAuthenticated]
    serializer_class = RegisterSerializer
    

@api_view(['POST'])
@permission_classes([IsNotAuthenticated]) 
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    user = authenticate(username=username, password=password)
    
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.id,
            'username': user.username,
            'email': user.email,
        })
    return Response({'error': 'Credenciales inválidas'}, status=400)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            request.user.auth_token.delete()
        except AttributeError:
            return Response(
                {"error": "No active token found"},
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(
            {"msg": "Successfully logged out"},
            status=status.HTTP_200_OK
        )
