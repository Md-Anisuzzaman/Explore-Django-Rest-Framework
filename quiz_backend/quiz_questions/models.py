from django.db import models
from quiz_category.models import Category


class Quiz(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text


class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)

    def __str__(self):
        return self.text


class CorrectAnswer(models.Model):
    question = models.OneToOneField(Question, on_delete=models.CASCADE)
    option = models.OneToOneField(Option, on_delete=models.CASCADE)

    def __str__(self):
        return self.option
