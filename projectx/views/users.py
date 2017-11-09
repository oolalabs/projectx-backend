# -*- coding: utf-8 -*-

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import permission_classes

from projectx.models import *
from projectx.serializers import *
from projectx.permissions import *


class MainUserViewSet(viewsets.ModelViewSet):
    queryset = MainUser.objects.all()
    permission_classes = (MainUserViewSetPermission,)

    def get_serializer_class(self, *args, **kwargs):
        try:
            if self.request.user._user_type == BaseUser.MAIN_USER_TYPE or self.request.user.is_superuser:
                return MainUserSerializer
        except: pass
        return MainUserPublicSerializer

    '''
        If no username is provided, use the phone number
    '''
    def create(self, request):
        data = request.data
        if type(data) != type(dict()): # could be a QueryDict
            data = dict(data)
            for k in data: # data is (k, [V]), make it (k, V)
                data[k] = data[k][0]
        if 'username' not in data and 'phone_number' in data:
            data['username'] = data['phone_number']
        serializer = MainUserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)