from django.contrib.auth.models import User, Group
from rest_framework import serializers
from ProductosMedicos.models import ProductosMedicos


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ProductosMedicosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductosMedicos
        fields = ['url', 'id_producto_medico', 'nombre_producto_medico', 'stock_producto_medico']