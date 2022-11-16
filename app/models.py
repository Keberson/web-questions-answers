from django.contrib.auth.models import User
from django.db import models


class QuestionManager(models.Manager):
    def last_questions(self):
        return self.all().order_by('-creation_date')

    def hot_questions(self):
        return self.all().order_by('-rating')

    def tag_questions(self, tag):
        try:
            return self.filter(tags__in=[Tags.objects.get(word=tag)]).order_by('-id')
        except:
            return []


class AnswerManager(models.Manager):
    def get_by_id(self, q_id):
        return self.all().filter(body_id=q_id)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=32)
    avatar = models.ImageField(upload_to="media/")
    date_reg = models.DateField(auto_now_add=True)
    rating = models.IntegerField()

    def __str__(self):
        return self.nickname


class Tags(models.Model):
    word = models.CharField(max_length=64)

    def __str__(self):
        return self.word


class Question(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey(Profile, on_delete=models.PROTECT)
    creation_date = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField(Tags)
    rating = models.IntegerField()

    objects = QuestionManager()

    def __str__(self):
        return self.title


class Answer(models.Model):
    body = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(Profile, on_delete=models.PROTECT)
    creation_date = models.DateField(auto_now_add=True)
    is_correct = models.BooleanField()
    rating = models.IntegerField()

    objects = AnswerManager()

    def __str__(self):
        return self.creation_date


class Like(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_liked = models.BooleanField()
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.question.title
