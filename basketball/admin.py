from django.contrib import admin
from basketball.models import Team, Player, Coach, Partido
from django.utils.safestring import mark_safe
# Register your models here.


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'logo_equipo', )
    search_fields = ('nombre', )
    def logo_equipo(self, obj):
        return mark_safe("<img src='%s' width='20' height='20' >" % obj.logo.url)
    logo_equipo.allow_tags = True
    logo_equipo._name_= 'Logo del equipo'


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('nombreplayer', 'foto_jugador')
    list_filter = ('fnacimiento',)
    filter_horizontal = ('team',)
    search_fields = ('nombreplayer', 'apodo', 'rut', )

    def foto_jugador(self, obj):
        return mark_safe("<img src='%s' width='20' height='20' >" % obj.foto.url)
    foto_jugador.allow_tags = True
    foto_jugador.__name__ = 'Foto del jugador'

@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ('nombreentrenador', 'apodo', )

@admin.register(Partido)
class PartidoAdmin(admin.ModelAdmin):
    list_display = ('nombrepartido', )
