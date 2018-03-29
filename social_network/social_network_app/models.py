from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField(unique=True)

    def __str__(self):
        return self.user.username


class Message(models.Model):
    sender = models.ForeignKey(Profile,
                               on_delete=models.CASCADE,
                               related_name='sender')

    receiver = models.ForeignKey(Profile,
                                 on_delete=models.CASCADE,
                                 related_name='receiver')

    message_body = models.TextField(blank=False)
    date = models.DateField()

    def __str__(self):
        return ('from ' + self.sender.user.username +
                ' to ' + self.receiver.user.username)


class FriendsRecord(models.Model):
    first_friend = models.ForeignKey(Profile,
                                     on_delete=models.CASCADE,
                                     related_name='first_friend')

    second_friend = models.ForeignKey(Profile,
                                      on_delete=models.CASCADE,
                                      related_name='second_friend')

    def __str__(self):
        return ('friend ' + self.first_friend.user.username +
                ' friend ' + self.second_friend.user.username)
