from models import Snippet
from django.contrib import admin
from django.db.models import TextField

from djangocodemirror.widgets import CodeMirrorWidget

class SnippetAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ['name']
    formfield_overrides = {
        TextField: {'widget': CodeMirrorWidget(config_name='cms_snippet')},
    }

admin.site.register(Snippet, SnippetAdmin)
