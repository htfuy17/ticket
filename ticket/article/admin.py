from django.contrib import admin
from article.models import Article

class SendPackageAdmin(admin.ModelAdmin):
    list_display = ('name','phone','title','ticket','number')


admin.site.register(Article,SendPackageAdmin)