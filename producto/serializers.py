from rest_framework import serializers
from .models import Producto


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        # fields = ('uuid', 'nombre', 'codigo_producto', 'descripcion',
        #           'precio', 'url_producto', 'url_imagenes',
        #           'estilo', 'colores', 'created_at')
        #read_only_fields = ('created_at', 'uuid',)
        fields = '__all__'
