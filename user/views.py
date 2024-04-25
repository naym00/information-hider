from rest_framework.decorators import api_view
from rest_framework.response import Response
from user.serializers.serializer import UserSerializer
from rest_framework import status
from user.models import User

@api_view(['GET'])
def getusers(request):
    users = User.objects.all()
    userserializers = UserSerializer(users, many=True).data
    for index, userserialize in enumerate(userserializers): userserialize.update({'fullname': users[index].getfullname(), 'surname': users[index].get_surname()})
    
    return Response(userserializers, status=status.HTTP_200_OK)