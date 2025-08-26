from modeltranslation.translator import translator
from .models import (
    Page, PageTranslation,
    BusinessValue, BusinessValueTranslation,
    TrainingProgram, TrainingProgramTranslation,
    JobInstruction, JobInstructionTranslation,
    CoffeeInfo, CoffeeInfoTranslation
)

def register_translations():
    """Регистрирует переводы для всех моделей"""
    translator.register(Page, PageTranslation)
    translator.register(BusinessValue, BusinessValueTranslation)
    translator.register(TrainingProgram, TrainingProgramTranslation)
    translator.register(JobInstruction, JobInstructionTranslation)
    translator.register(CoffeeInfo, CoffeeInfoTranslation)
