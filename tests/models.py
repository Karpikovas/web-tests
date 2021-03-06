from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=255)


    def __str__(self):
        return self.name

class Test(models.Model):
    tags = models.ForeignKey(Tag, on_delete=models.CASCADE)
    test_name = models.CharField(max_length=200)

    def __str__(self):
        return self.test_name


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text


class TestParticipant(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.user.username


class TestParticipantAnswers(models.Model):
    test_participant = models.ForeignKey(TestParticipant, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

    def __str__(self):
        return self.test_participant.__str__() + self.test_participant.__str__() \
               + self.question.__str__() + self.answer.__str__()
