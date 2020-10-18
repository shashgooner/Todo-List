from django.db import models
from account.models import Account


class Task(models.Model):
  user = models.ForeignKey(Account, on_delete=models.CASCADE)
  title = models.CharField(max_length=200)
  end_date = models.DateField()
  completed = models.BooleanField(default=False, blank=True, null=True)
      
  def __str__(self):
    return self.title

  class Meta:
      ordering = ["end_date"]


class Comment(models.Model):
  user = models.ForeignKey(Account, on_delete=models.CASCADE)
  task = models.ForeignKey(Task, on_delete=models.CASCADE)
  comment = models.CharField(max_length=20)
  reply = models.CharField(max_length=20)

  



