from django.contrib import admin, messages

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'is_active']
    list_display_links = ['id', 'name']
    list_editable = ['is_active']
    fieldsets = (
        ('Identification', {
            'fields': ('name', 'price', 'is_active')}),
        ('Details', {
         'classes': ('collapse', ),
         'fields': ('category', 'company')})
        )

    actions = ['make_inactive_product']

    def make_inactive_product(self, request, queryset):
        inactive_product = queryset.update(is_active=False)

        self.message_user(
            request, f"{inactive_product} status changed to inactive", messages.SUCCESS
        )
    make_inactive_product.short_description = 'Make inactive'


