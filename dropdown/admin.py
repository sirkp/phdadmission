from django.contrib import admin
from dropdown.models import (Category, BranchQualifyingExamination, Country,
                                    PGDiscipline, ResearchArea, State, TypeOfWork,
                                     UGDiscipline)
# Register your models here.
admin.site.register(Country)
admin.site.register(BranchQualifyingExamination)
admin.site.register(Category)
admin.site.register(PGDiscipline)
admin.site.register(ResearchArea)
admin.site.register(State)
admin.site.register(TypeOfWork)
admin.site.register(UGDiscipline)
