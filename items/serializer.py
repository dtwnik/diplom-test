from rest_framework import serializers

from .models import *


class CPUSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CPU
        fields = '__all__'


class MBSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MB
        fields = '__all__'


class RamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ram
        fields = '__all__'


class StorageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Storage
        fields = '__all__'


class GPUSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GPU
        fields = '__all__'


class PSUSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PSU
        fields = '__all__'