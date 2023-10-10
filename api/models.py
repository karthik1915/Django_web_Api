from django.db import models

class ImagesModel(models.Model):
    id = models.AutoField(primary_key=True)
    image_url = models.URLField()
    title = models.CharField(max_length=255)
    category =models.CharField(max_length=100,default="")
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_safe = models.BooleanField(default=True)
    tags = models.JSONField(default=list)
    
    def __str__(self):
        return self.title