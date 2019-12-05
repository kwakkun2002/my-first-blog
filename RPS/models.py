from django.db import models

# Create your models here.

class InputData(models.Model):#내가 ai에 넣을거 저장
    num = models.IntegerField()
    Player = models.CharField(max_length=10)
    ai = models.CharField(max_length=10)
    Lose_or_Win = models.IntegerField()


class Output(models.Model):#ai로부터 받을거 저장
    output = models.CharField(max_length=10)

    def __str__(self):
        return self.output

class Score(models.Model):#둘 사이의 점수계산
    player_score = models.IntegerField()
    ai_score = models.IntegerField()












