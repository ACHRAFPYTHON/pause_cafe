from click import command
from django.contrib import admin
from .models import*
admin.site.register(serveur)
admin.site.register(carte)
admin.site.register(boissonschaudes)
admin.site.register(boissonsfraiches)
admin.site.register(glaces)

admin.site.register(jus)
admin.site.register(crepes)
admin.site.register(lignecommande)
admin.site.register(comande)

# Register your models here.
