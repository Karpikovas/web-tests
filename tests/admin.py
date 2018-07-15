from django.contrib import admin
from .models import Question, Test, Answer,Tag
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin    

admin.site.unregister(User)

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff','is_active',)
    list_filter = ('is_staff', 'is_superuser', 'is_active',)    
admin.site.register(User, CustomUserAdmin)


class AnswerInline(admin.StackedInline):
	model = Answer
	extra = 3

class QuestionCase(admin.ModelAdmin):
	inlines = [AnswerInline]
	list_display = ('question_text', 'quiz', 'create_date', 'update_date')
	list_filter = ['quiz']

class TestCase(admin.ModelAdmin):
	list_display = ('name', 'tags', 'create_date', 'update_date')
	list_filter = ['tags']
	
admin.site.register(Question, QuestionCase)
admin.site.register(Test, TestCase)
admin.site.register(Tag)