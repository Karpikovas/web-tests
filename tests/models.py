from django.db import models

class Tag(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name

class Test(models.Model):
	tags = models.ForeignKey(Tag, on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	create_date = models.DateTimeField()
	update_date = models.DateTimeField(auto_now=True, null=True)

	def __str__(self):
		return self.name

class Question(models.Model):
	quiz = models.ForeignKey(Test, on_delete=models.CASCADE)
	question_text = models.CharField(max_length=255)
	create_date = models.DateTimeField()
	update_date = models.DateTimeField(auto_now=True, null=True)

	def __str__(self):
		return self.question_text

class Answer(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	answer_text = models.CharField(max_length=255)
	correct = models.BooleanField(default=False)