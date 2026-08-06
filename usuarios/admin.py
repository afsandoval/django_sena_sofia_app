
from django.contrib import admin
from .models import Usuario
 
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('documento', 'nombre', 'apellido', 'correo_personal', 'telefono')
    search_fields = ('documento', 'nombre', 'apellido', 'correo_personal')
    list_filter = ('apellido',)
    ordering = ('apellido', 'nombre')
