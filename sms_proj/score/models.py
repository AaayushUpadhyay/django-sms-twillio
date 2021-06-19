from django.db import models
import os
from twilio.rest import Client
from django.conf import settings
# Create your models here.
class Score(models.Model):
    result=models.PositiveIntegerField()

    def __str__(self):
        return str(self.result)
    
    def save(self,*args,**kwargs):
        if self.result<70:
            account_sid = settings.TWILIO_ACCOUNT_SID
            auth_token = settings.TWILIO_AUTH_TOKEN
            client = Client(account_sid, auth_token)

            message = client.messages \
                            .create(
                                body="The current result is less - "+str(self.result),
                                from_=settings.TWILIO_NO,
                                to=settings.MY_NO
                            )

            print(message.sid)
        return super().save(*args,**kwargs)