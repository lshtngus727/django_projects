from django.db import models
from django.contrib.auth.models import User
from django.db.models import ManyToManyField


class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    #max_length 최대 글자 200자, 길이 제한된 텍스트 CharField, 제한 없는 텍스트 TextField 사용
    create_date = models.DateTimeField()
    #작성일시 날짜 시간 관계된 속성 DateTimeField
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_question') #추천인 추가

    def __str__ (self):
        return self.subject

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    #ForeignKey 연결키, on_delete=modles.CASACADE 답변과 연결된 질문 삭제될 경우 답변도 함께 삭제
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')



