from django.contrib import admin
from afra7.catalog.models import *
from django.utils.translation import ugettext as _

class OrderAdmin(admin.ModelAdmin):
    list_display = [
		"date",
        "name",
		"da3i",
		"size",
		"product",
		"email",
		"printed",
		"deliver",
		"phone",
		"notes",
		"status",
    ]
class PagesAdmin(admin.ModelAdmin):
	list_display = [
		"title",
		"content",
		]

admin.site.register(Product)
admin.site.register(Pages, PagesAdmin)
admin.site.register(Category)
admin.site.register(Order, OrderAdmin)
