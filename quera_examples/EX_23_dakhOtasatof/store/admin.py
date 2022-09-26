from django.contrib import admin, messages
from .models import Product, Address, Company, Category
# from django.utils.html import format_html
from django.db.models import F

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['postal_address', 'city']
    list_filter = ['city']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ['id', 'name', 'category', 'company', 'price']
    list_filter = ('company', 'category')
    sortable_by = ['price']
    list_display_links = ['id', 'name']

    fieldsets = (
        ('general_info', {
            'fields': ('name', 'category')
         }),
        ('Details', {
            'classes': ('collapse',),
            'fields': ('company', 'price')
        }),
    )

    actions = ['raise_price']

    def raise_price(self, request, queryset):
        new_price = queryset.update(price=F("price")+200)

        self.message_user(
            request, f"{new_price} new price for our product", messages.SUCCESS
        )

    raise_price.short_description = 'raise 2 unit to selected price'


class ProductInline(admin.StackedInline):
    model = Product

    def get_extra(self, request, obj=None, **kwargs):
        extra = 0
        return extra


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [ProductInline]

class ProductInlineTable(admin.TabularInline):
    model = Product

    def get_extra(self, request, obj=None, **kwargs):
        extra = 0
        return extra


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    inlines = [ProductInlineTable]

    fieldsets = (
        ('general_info', {
            'fields': ('name', )
         }),
        ('Details', {
            'classes': ('collapse',),
            'fields': ('address', )
        }),
    )





# class CompanyFilter(admin.SimpleListFilter):
#     title = 'company'
#     parameter_name = 'company'
#
#     def lookups(self, request, model_admin):
#         company_names = [(product.company.name, product.company.name) for product in Product.objects.all()]
#         return set(company_names)
#
#     def queryset(self, request, queryset):
#         if self.value():
#             return queryset.filter(company__name__exact=self.value())
#
#
# class CategoryFilter(admin.SimpleListFilter):
#     title = 'category'
#     parameter_name = 'category'
#
#     def lookups(self, request, model_admin):
#         category_names = [(product.category.name, product.category.name) for product in Product.objects.all()]
#         return set(category_names)
#
#     def queryset(self, request, queryset):
#         if self.value():
#             return queryset.filter(category__name__exact=self.value())


# def show_name(self, obj):
#     return format_html(f'<a href="{obj.id}">{obj.name}</a>')
# show_name.short_description = "NAME"