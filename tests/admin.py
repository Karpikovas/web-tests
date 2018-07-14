from django.contrib import admin
from .models import Question, Test, Answer,Tag
class AnswerInline(admin.StackedInline):
	model = Answer
	extra = 3

class QuestionCase(admin.ModelAdmin):
	inlines = [AnswerInline]

class TagsInline(admin.StackedInline):
	model = Tag
	extra = 0

class TestCase(admin.ModelAdmin):
	inlines = [TagsInline]

admin.site.register(Question, QuestionCase)
admin.site.register(Test, TestCase)