from django.contrib import admin

# Register your models here.
from sale.models import Producer, Kinde_Kala, Kala, Customer


class ProducerAdmin(admin.ModelAdmin):
    list_display = ['__str__','name', 'active']
    list_filter =['name', 'active']
    list_editable =['name', 'active']
    search_fields =['name', 'active']
    # list_per_page = 20
    class Meta:
        model = Producer

class Kinde_KalaAdmin(admin.ModelAdmin):
    list_display = ['__str__','name', 'active']
    list_filter =['name', 'active']
    list_editable =['name', 'active']
    search_fields =['name', 'active']
    # list_per_page = 20
    class Meta:
        model = Kinde_Kala


class KalaAdmin(admin.ModelAdmin):
    list_display = ['__str__','name', 'active']
    list_filter =['name', 'active']
    list_editable =['name', 'active']
    search_fields =['name', 'active']
    # list_per_page = 20
    class Meta:
        model = Kala
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['__str__','name1', 'name2']
    list_filter =['name1', 'name2']
    list_editable =['name1', 'name2']
    search_fields =['name1', 'name2']
    # list_per_page = 20
    class Meta:
        model = Customer

admin.site.register(Producer, ProducerAdmin)
admin.site.register(Kinde_Kala, Kinde_KalaAdmin)
admin.site.register(Kala, KalaAdmin)
admin.site.register(Customer, CustomerAdmin)
