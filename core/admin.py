from django.contrib import admin
from .models import (
    Page, BusinessValue, TrainingProgram, 
    JobInstruction, CoffeeInfo, Language
)

# Временно регистрируем без TranslationAdmin
admin.site.register(Page)
admin.site.register(BusinessValue)
admin.site.register(TrainingProgram)
admin.site.register(JobInstruction)
admin.site.register(CoffeeInfo)
admin.site.register(Language)
