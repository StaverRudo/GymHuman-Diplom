from django.contrib import admin

# Register your models here.
from articles.models import *
from users.models import *

admin.site.register(ArticleCategory)
admin.site.register(ArhivCategory)
admin.site.register(Article)


admin.site.register(About)
admin.site.register(Home)
admin.site.register(One)
admin.site.register(Two)
admin.site.register(Three)
admin.site.register(Fo)
admin.site.register(Five)
admin.site.register(Six)

