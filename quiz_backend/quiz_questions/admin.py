from django.contrib import admin
from .models import Quiz, Question, Option, CorrectAnswer

class OptionInline(admin.TabularInline):
    model = Option
    extra = 1  # Number of extra option fields to display

class QuestionAdmin(admin.ModelAdmin):
    inlines = [OptionInline]

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1  # Number of extra question fields to display

class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Option)
admin.site.register(CorrectAnswer)
