from django.contrib import admin

# Register your models here.
from index.models import *

admin.site.register(company_member)
admin.site.register(customer_info)
admin.site.register(supplier_info)
admin.site.register(factory_info)


