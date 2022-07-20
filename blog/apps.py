from django.apps import AppConfig


class BlogConfig(AppConfig):                                #register this class within your your mainapp folder's(Blog_Site here) file settings.py
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
