from rest_framework import serializers

from.models import *


class RegSerializers(serializers.ModelSerializer):

    class Meta:
        model=Adminreg
        fields=['FirstName','LasttName','Username','MobileNumber','Email','branch']

    def create(self, validated_data):
        user=Adminreg.objects.create(FirstName=validated_data['FirstName'],LasttName=validated_data['LasttName'],Username=validated_data['Username'],
                                     MobileNumber=validated_data['MobileNumber'],
                                     Email=validated_data['Email'],branch=validated_data['branch'])
        user.save()
        return user


class UpdateRegSerializers(serializers.ModelSerializer):
    class Meta:
        model=Adminreg
        fields=['FirstName','LasttName','Username','MobileNumber','Email','branch']