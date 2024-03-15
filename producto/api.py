from .models import Producto
from rest_framework import viewsets, permissions
from .serializers import ProductoSerializer

from rest_framework.response import Response
from rest_framework import status

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductoSerializer
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        
        # Obtener los parámetros de consulta
        nombre = request.query_params.get('nombre', None)
        codigo_producto = request.query_params.get('codigo_producto', None)
        descripcion = request.query_params.get('descripcion', None)
        precio = request.query_params.get('precio', None)
        estilo = request.query_params.get('estilo', None)
        lista = request.query_params.get('lista', None)
        # Agrega aquí más campos según sea necesario
        
        # Aplicar los filtros si los parámetros están presentes
        if nombre:
            queryset = queryset.filter(nombre__icontains=nombre)
        if codigo_producto:
            queryset = queryset.filter(codigo_producto__icontains=codigo_producto)
        if descripcion:
            queryset = queryset.filter(descripcion__icontains=descripcion)
        if precio:
            queryset = queryset.filter(precio__icontains=precio)
        if estilo:
            queryset = queryset.filter(estilo__icontains=estilo)
        if lista:
            queryset = queryset.filter(lista__icontains=lista)
        # Agrega aquí más filtros según sea necesario
        
        serializer = self.get_serializer(queryset, many=True)
        
        if not serializer.data:  
            return Response({"error": "No se encontraron productos con los criterios de búsqueda proporcionados"}, status=status.HTTP_404_NOT_FOUND)
        
        return Response({"data": serializer.data})
