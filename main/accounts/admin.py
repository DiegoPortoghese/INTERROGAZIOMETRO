from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from accounts.models import Profile
from django.http import HttpResponse
from django.core import serializers
from django.forms.models import model_to_dict
import json
import csv

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profili Utente'
    verbose_name = "Profilo utente"

class UserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups', 'date_joined')
    actions = ['export_as_json','export_as_csv']

    def export_as_json(modeladmin, request, queryset):
        response = HttpResponse(content_type="application/json")

        tmp = []
        for u in queryset:
            if hasattr(u, 'profiloutente'):
                tmp.append(u.profiloutente)


        dati = serializers.serialize("json", tmp)
        output =[]
        for e in json.loads(dati):
            _ = User.objects.get(id=e['fields']['user'])
            e['fields']['email'] =  _.email
            e['fields']['first_name'] = _.first_name
            e['fields']['last_name'] = _.last_name
            output.append(e)

        response['Content-Disposition'] = 'attachment; filename=output.json'
        response.write(json.dumps(output))
        return response


    def export_as_csv(modeladmin, request, queryset):
        response = HttpResponse(content_type="text/csv")
        writer = csv.writer(response)

        tmp = []
        for u in queryset:
            if hasattr(u, 'profiloutente'):
                tmp.append(u.profiloutente)

        for e in tmp:
            u = User.objects.get(pk=e.user.pk)
            user_row = [u.email,u.first_name, u.last_name]
            profilo = model_to_dict(e)
            
            # appendo il profiloutente
            for x in profilo:
                if x != 'email_on_login' and x != 'user' and x != 'interno':
                    user_row.append(u'{0}'.format(profilo[x]).encode('utf-8'))
            writer.writerow(user_row)

        response['Content-Disposition'] = 'attachment; filename=output.csv'
        return response

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
