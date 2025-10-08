from django.contrib import admin
from .models import Category, Product, CartItem, Favourite, ProductImage
from .models import Order, OrderItem
from .models import SupportMessage

class ProductImageInline(admin.TabularInline):  # or StackedInline if you prefer
    model = ProductImage
    extra = 10  # how many empty upload boxes to show by default
    fields = ['image']
    readonly_fields = []
    show_change_link = False

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'inventory', 'created_at')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInline]  # ← allows adding multiple images in admin

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('product', 'quantity', 'price')  # Make it read-only in admin

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'full_name', 'email', 'total_price', 'payment_method', 'is_paid', 'created_at')
    list_filter = ('is_paid', 'payment_method', 'created_at')
    search_fields = ('user__username', 'email', 'full_name')
    inlines = [OrderItemInline]

@admin.register(SupportMessage)
class SupportMessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'subject', 'is_resolved', 'created_at')
    search_fields = ('user__username', 'subject', 'message')




admin.site.register(Order, OrderAdmin)
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(CartItem)
admin.site.register(Favourite)
admin.site.register(ProductImage)