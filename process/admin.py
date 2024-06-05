from django.contrib import admin

from process.models import HavalehRow, Havaleh, Process, ProcessRow


# Register your models here.
class HavalehRowAdmin(admin.ModelAdmin):
    list_display = ['__str__']
    # list_display = ['__str__','name1', 'name2']
    # list_filter =['name1', 'name2']
    # list_editable =['name1', 'name2']
    # search_fields =['name1', 'name2']
    # list_per_page = 20
    class Meta:
        model = HavalehRow
class HavalehAdmin(admin.ModelAdmin):
    list_display = ['__str__']
    # list_display = ['__str__','name1', 'name2']
    # list_filter =['name1', 'name2']
    # list_editable =['name1', 'name2']
    # search_fields =['name1', 'name2']
    # list_per_page = 20
    class Meta:
        model = Havaleh
class ProcessAdmin(admin.ModelAdmin):
    list_display = ['__str__']
    # list_display = ['__str__','name1', 'name2']
    # list_filter =['name1', 'name2']
    # list_editable =['name1', 'name2']
    # search_fields =['name1', 'name2']
    # list_per_page = 20
    class Meta:
        model = Process
class ProcessRowAdmin(admin.ModelAdmin):
    list_display = ['__str__']
    # list_display = ['__str__','name1', 'name2']
    # list_filter =['name1', 'name2']
    # list_editable =['name1', 'name2']
    # search_fields =['name1', 'name2']
    # list_per_page = 20
    class Meta:
        model = ProcessRow

admin.site.register(HavalehRow, HavalehRowAdmin)
admin.site.register(Havaleh, HavalehAdmin)
admin.site.register(Process, ProcessAdmin)
admin.site.register(ProcessRow, ProcessRowAdmin)