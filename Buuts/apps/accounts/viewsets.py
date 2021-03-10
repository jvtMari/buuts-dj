from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
#
from .models import User
from .functions import send_acc_active_email
#
from .serializers import (
    GetUserSerializer,
    PostUserSerializer,
    PatchUserSerializer,
    ChangePassUserSerializer,
    UserPagination
)


class UserViewSet (viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = GetUserSerializer
    pagination_class = UserPagination
    #
    authentication_classes = (TokenAuthentication,)

    def get_permissions(self):
        if (self.action in ['partial_update','retrieve','list']):
            self.permission_classes = [IsAuthenticated]

        return [permission() for permission in self.permission_classes]

    def create (self, request, *args, **kwargs):
        serializer = PostUserSerializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        self.perform_create(serializer)
        
        #Verify email
        sent = send_acc_active_email(request, serializer.instance)

        if(sent):
            return Response(serializer.data)
        else:
            serializer.instance.delete()
            return Response(
                {
                    'code': "NOK",
                    'msg': "Couldn't send email to verify the account. User instance removed, Try again."
                }
            )

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if(request.data.get('password', None) is not None):
            serializer = ChangePassUserSerializer(instance, data=request.data, partial=True, context={'request':request})
        else:
            serializer = PatchUserSerializer(instance, data=request.data, partial=True, context={'request':request})
        
        serializer.is_valid(raise_exception = True)
        self.perform_update(serializer)

        return Response(serializer.data)


