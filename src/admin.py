from django.contrib import admin
from django.db import models
from django.forms import Textarea, TextInput

# Register your models here.
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from .models import Players
from .models import Matches
from .models import Updates
from .models import Slides
from .models import EBoard
from .models import Images
from .models import Practices
from .models import AttendanceHistory
from .models import OrganizationInformation
from .models import FrontPageContent
from .models import SocialMedia
from .models import Greeting
from .models import ColorScheme


class DownloadEmailAdmin(admin.ModelAdmin):
    actions = ['download_emails']
    def download_emails(self, request, queryset):
        import csv
        from django.http import HttpResponse
        import StringIO

        players = Players.objects.all()

        f = StringIO.StringIO()
        # writer = csv.writer(f)

        for player in queryset:
            if player.Email != '':
                output = '"%s %s" <%s>, ' % (player.First_Name, player.Last_Name, player.Email)
                f.write(output)


        f.seek(0)

        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=emails.txt'
        return response

    download_emails.short_description = "Download emails to a .txt file"

    def has_add_permission(self, request):
        return False


class TextInputAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'150'})},
    }

class AttendanceHistoryAdmin(admin.ModelAdmin):
    class Media:
        css = {
             'all': ('admin/css/attendance.css',)
        }

class TextareaAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': Textarea(attrs={
                                'rows': 1,
                                'cols': 150,
                                'style': 'height: 5em;'

        })},
    }

class AtMostOneEntryAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.count() > 0:
            return False
        else:
            return True

class NoAddPermissionAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

class OrganizationInformationAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': Textarea(attrs={
                                'rows': 1,
                                'cols': 150,
                                'style': 'height: 5em;'

        })},
    }

    def has_add_permission(self, request):
        if self.model.objects.count() > 0:
            return False
        else:
            return True

# admin.site.unregister(User)
# admin.site.unregister(Group)
admin.site.register(Players, DownloadEmailAdmin)
admin.site.register(Matches, TextInputAdmin)
admin.site.register(Updates, TextareaAdmin)
admin.site.register(Slides, TextInputAdmin)
admin.site.register(EBoard)
admin.site.register(Images, TextInputAdmin)
admin.site.register(Practices, NoAddPermissionAdmin)
admin.site.register(AttendanceHistory, AttendanceHistoryAdmin)
admin.site.register(OrganizationInformation, OrganizationInformationAdmin)
admin.site.register(FrontPageContent, TextareaAdmin)
admin.site.register(SocialMedia, TextareaAdmin)
admin.site.register(ColorScheme, AtMostOneEntryAdmin)
