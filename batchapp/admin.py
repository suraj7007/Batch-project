from django.contrib import admin
from .models import Batch, Codes


@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    list_display = [
        "batch_id", "user", "batch_name", "number_of_code"
    ]


@admin.register(Codes)
class CodesAdmin(admin.ModelAdmin):
    list_display = [
        "code_id", "code", "batch"
    ]


