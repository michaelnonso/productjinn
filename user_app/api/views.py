from lib2to3.pgen2 import token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status

from django.contrib.auth.models import User

from user_app.api.serializers import RegistrationSerialer

@api_view(['POST'])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
    
@api_view(['POST',])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerialer(data=request.data)
        data = {}
        
        if serializer.is_valid():
            account =serializer.save() # needs to be overwritten in serializer(2 password needs to be checked b4 saving one, email needs to be checked if unique)
            data['response'] = "Registration successful"
            data['username'] = account.username
            
            #using Token 
            token = Token.objects.get(user=account).key
            data['token'] = token
            
            
        else:
            data = serializer.errors
            
        return Response(data )  #to the client excluding password as it is write only
 

        
    