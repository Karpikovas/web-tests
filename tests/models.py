from django.db import models

class Test(models.Model):
	name = models.CharField(max_length=255)
	create_date = models.DateTimeField()
	update_date = models.DateTimeField(auto_now=True, null=True)

	def __str__(self):
		return self.name

class Tag(models.Model):
	quiz = models.ForeignKey(Test)
	name = models.CharField(max_length=255)

class Question(models.Model):
	quiz = models.ForeignKey(Test)
	question_text = models.CharField(max_length=255)
	create_date = models.DateTimeField()
	update_date = models.DateTimeField(auto_now=True, null=True)

	def __str__(self):
		return self.question_text

class Answer(models.Model):
	question = models.ForeignKey(Question)
	answer_text = models.CharField(max_length=255)
	correct = models.BooleanField(default=False)