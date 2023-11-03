from django.contrib import admin
from .models import Company, Process, Duty, Shortlist
# Register your models here.

admin.site.register(Company)
admin.site.register(Process)
admin.site.register(Duty)
admin.site.register(Shortlist)