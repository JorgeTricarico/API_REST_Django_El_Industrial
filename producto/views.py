from rest_framework import permissions, viewsets

from .serializers import ProductoSerializer
from .models import Producto
from .scraping import Producto as pr
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

# class ProductoViewSet(viewsets.ModelViewSet):

#     queryset = Producto.objects.all()
#     serializer_class = ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    #permission_classes = [permissions.AllowAny]

class ProductoScrapingViewSet(viewsets.ViewSet):
    """
    API endpoint for scraping and listing products.
    """
    serializer_class = ProductoSerializer
    #permission_classes = [permissions.AllowAny]
    
    def list(self, request):
        url_productos = pr.scraping_url_ferrolux()
        productos_scrapeados = []
        for url_producto in url_productos:
            data = pr.extrac_attributes(url_producto)
            productos_scrapeados.append(data)
        serializer = ProductoSerializer(productos_scrapeados, many=True)
        return Response(serializer.data)
    
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
