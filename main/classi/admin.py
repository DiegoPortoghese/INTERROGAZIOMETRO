from django.contrib import admin
from .models import Classe
from .models import ClasseMateria
from .models import ClasseOraMateria
from .models import ClasseInterrogazione
from .models import ClasseImage

class ClasseAdmin(admin.ModelAdmin):
    
    class Meta:
        model = Classe
    
    list_display = ["__str__", "creation_date"]
    list_filer = ["creation_date"]
    search_fields = ["nome", "descrizione"]


admin.site.register(Classe, ClasseAdmin)
admin.site.register(ClasseMateria)
admin.site.register(ClasseOraMateria)
admin.site.register(ClasseInterrogazione)
admin.site.register(ClasseImage)
