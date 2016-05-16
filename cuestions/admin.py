from django.contrib import admin

# Register your models here.
from .models import Question, Answer



class AnwerTabularInline(admin.TabularInline):
    model = Answer

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnwerTabularInline]
    class Meta:
        model = Question

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass