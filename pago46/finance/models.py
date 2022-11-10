from django.db import models
from users.models import User
# Create your models here.
class IOU(models.Model):
    lender = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='lent')
    borrower = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='borrowed')
    value = models.FloatField()
    expiration = models.DateTimeField()
