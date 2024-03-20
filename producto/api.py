from .models import Producto
from rest_framework import viewsets, permissions
from .serializers import ProductoSerializer

from rest_framework.response import Response
from rest_framework import status
from .scraping import Producto as pr

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
    
    def destroy(self, request, *args, **kwargs):
        queryset = self.queryset
        
        # Obtener los parámetros de consulta
        nombre = request.query_params.get('nombre', None)
        codigo_producto = request.query_params.get('codigo_producto', None)
        descripcion = request.query_params.get('descripcion', None)
        precio = request.query_params.get('precio', None)
        estilo = request.query_params.get('estilo', None)
        lista = request.query_params.get('lista', None)
        # Agrega aquí más campos según sea necesario

        # Filtrar los productos según los parámetros de consulta
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
        
        # Verificar si hay productos que coincidan con los filtros
        if not queryset.exists():
            return Response({"error": "No se encontraron productos con los criterios de búsqueda proporcionados"}, status=status.HTTP_404_NOT_FOUND)
        
        # Eliminar los productos filtrados
        try:
            queryset.delete()
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response({"message": "Productos eliminados correctamente"})

class ProductoScrapingViewSet(viewsets.ModelViewSet):

    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def create(self, request, *args, **kwargs):
        url_productos = pr.scraping_url_ferrolux()
        for url_producto in url_productos:
            data = pr.extrac_attributes(url_producto)
            serializer = self.get_serializer(data=data)
            if serializer.is_valid():
                self.perform_create(serializer)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("Productos creados exitosamente", status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save()
        
    def list(self, request):
        url_productos = pr.scraping_url_ferrolux()
        productos_scrapeados = []
        for url_producto in url_productos:
            data = pr.extrac_attributes(url_producto)
            productos_scrapeados.append(data)
            print(data)
        serializer = self.serializer_class(productos_scrapeados, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)