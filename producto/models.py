from django.db import models
import uuid
# Create your models here.
class Producto(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField( max_length=200)
    code = models.CharField( max_length=200)
    description = models.TextField()
    price = models.CharField( max_length=200)
    url_product = models.JSONField()
    url_image = models.JSONField()
    colors_style = models.JSONField()
    colors_text = models.JSONField()
    style = models.CharField( max_length=200)
    list = models.CharField( max_length=200)
    
    is_active = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add = True)