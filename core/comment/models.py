from django.db import models
from accounts.models import User
from blog.models import BlogPostModel

class Comment(models.Model):
    post = models.ForeignKey(BlogPostModel , on_delete=models.CASCADE)
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-date_posted']

    def __str__(self):
        return str(self.author) + ' comment: ' + str(self.content)