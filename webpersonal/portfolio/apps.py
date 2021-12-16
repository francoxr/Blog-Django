from django.apps import AppConfig


class PortfolioConfig(AppConfig):
    """Define los atributos de la app"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'portfolio'
    # nombre publico
    verbose_name = 'Portafolio'