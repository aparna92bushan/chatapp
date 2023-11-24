from django.db import models
from django.contrib.auth.models import User


class ChatRoom:
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Message:
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
