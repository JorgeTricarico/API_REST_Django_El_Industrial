from django.db import models
import uuid
# Create your models here.
class Producto(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    nombre = models.CharField( max_length=200)
    codigo_producto = models.CharField( max_length=200)
    descripcion = models.TextField()
    precio = models.CharField( max_length=200)
    url_producto = models.JSONField()
    url_imagenes = models.JSONField()
    colores = models.JSONField()
    estilo = models.CharField( max_length=200)
    lista = models.CharField( max_length=200)
    
    created_at = models.DateTimeField(auto_now_add = True)