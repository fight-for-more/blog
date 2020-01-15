from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class TagInfo(models.Model):
    name = models.CharField(max_length=20)
    img_url = models.CharField(max_length=40, default="/static/images/html.jpg")

    def __str__(self):
        return self.name

class NoteInfo(models.Model):
    title = models.CharField(max_length=20)
    content = RichTextUploadingField()
    pub_date = models.DateField(default="2019-12-11")
    tag = models.ForeignKey(TagInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class CommentInfo(models.Model):
    content = models.TextField()
    NoteInfo = models.ForeignKey(NoteInfo, on_delete=models.CASCADE)


