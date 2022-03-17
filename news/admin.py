from django.contrib import admin
from .models import User, Lector, Periodista, Noticia, Valoracio

admin.site.register(User)
admin.site.register(Lector)
admin.site.register(Periodista)
admin.site.register(Noticia)
admin.site.register(Valoracio)

