

from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from rest_framework.response import Response

from .models import Adminreg
from .serializers import RegSerializers, UpdateRegSerializers


# Create your views here.
class Register(generics.GenericAPIView):
    serializer_class = RegSerializers

    def post(self, request, *args, **kwargs):
        a = self.get_serializer(data=request.data)
        b =Adminreg.objects.all()
        count = 0
        for i in b:
            count+=1
        print(count)
        a.is_valid(Register)
        user = a.save(raise_expection=True)
        return Response({'message': 'Successful',
                         'result': RegSerializers(user).data,
                         'Haseerror': False,
                         'status': 200
                         })

class Getadmindetaiies(generics.GenericAPIView):
    serializer_class = RegSerializers

    def get(self,request,*args,**kwargs):
        user=Adminreg.objects.all()
        serializer_class=RegSerializers(user,many=True)
        return Response({'message':'Successful',
                         'result':serializer_class.data,
                          'Haseerror':False,
                           'status':200
                         })

class Getbyidadmindetaiies(generics.GenericAPIView):
    serializer_class = RegSerializers

    def get(self,request,Id):
        user=Adminreg.objects.filter(id=Id).first()
        serializer_class=RegSerializers(user)
        return Response({'message':'Successful',
                         'result':serializer_class.data,
                          'Haseerror':False,
                           'status':200
                         })

class Updateadmindetailes(generics.GenericAPIView):
    serializer_class = UpdateRegSerializers

    def put(self,request,Id):
        user=Adminreg.objects.get(id=Id)
        FirstName=request.data.get('FirstName')
        LasttName=request.data.get('LasttName')
        Username=request.data.get('Username')
        MobileNumber=request.data.get('MobileNumber')
        Email=request.data.get('Email')
        branch=request.data.get('branch')

        data={'FirstName':FirstName,'LasttName':LasttName,'Username':Username,
              'MobileNumber':MobileNumber,'Emal':Email,'branch':branch}

        s=UpdateRegSerializers(user,data=data,partial=True)
        s.is_valid(raise_exception=True)
        s.save()

        return Response({'message':'Successful',
                         'result':UpdateRegSerializers(user).data,
                          'Haseerror':True,
                           'status':200
                         })


class Deletereg(generics.GenericAPIView):
    serializer_class = UpdateRegSerializers

    def delete(self,request,id):
        a = Adminreg.objects.get(id=id)
        b =a.delete()
        count = 0
        for i in b:
            count= count-1
            print(count)
        return Response({'message': 'Successful',
                         'Haseerror': True,
                         'status': 200
                         })

