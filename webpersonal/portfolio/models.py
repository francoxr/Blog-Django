from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=255, verbose_name='Titulo')
    description = models.TextField(blank=True, verbose_name='Descripcion')
    image = models.ImageField(verbose_name='imagen', upload_to="projects")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')

    class Meta:
        """Se agregan metadatos extendidos"""
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created_at"]
    
    def __str__(self):
        return self.title