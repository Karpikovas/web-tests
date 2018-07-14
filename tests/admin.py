from django.contrib import admin
from .models import Question, Test, Answer,Tag
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