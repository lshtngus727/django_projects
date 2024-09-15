from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    #max_length 최대 글자 200자, 길이 제한된 텍스트 CharField, 제한 없는 텍스트 TextField 사용
    create_date = models.DateTimeField()
    #작성일시 날짜 시간 관계된 속성 DateTimeField

    def __str__ (self):
        return self.subject

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    #ForeignKey 연결키, on_delete=modles.CASACADE 답변과 연결된 질문 삭제될 경우 답변도 함께 삭제
    content = models.TextField()
    create_date = models.DateTimeField()



