from django.contrib import admin
from devolution.models import Devolution, DevolutionStatus, DevolutionType, DevolutionReason, DevolutionProductOrder

# Register your models here.
class DevolutionAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_order', 'id_devolution_type', 'id_devolution_reason', 'id_devolution_status', 'date', 'buyer_reason')

class DevolutionProductOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_order_product', 'id_devolution', 'id_devolution_status')

class DevolutionReasonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')

class DevolutionStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')

class DevolutionTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')

admin.site.register(Devolution, DevolutionAdmin)
admin.site.register(DevolutionProductOrder, DevolutionProductOrderAdmin)
admin.site.register(DevolutionReason, DevolutionReasonAdmin)
admin.site.register(DevolutionStatus, DevolutionStatusAdmin)
admin.site.register(DevolutionType, DevolutionTypeAdmin)