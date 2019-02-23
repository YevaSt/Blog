from django.db import models

# Create your models here.
class Post(models.Model):
      title=models.CharField(max_length=255)
      text=models.TextField()
      user=models.ForeignKey("auth.User", on_delete=models.CASCADE)
      created_att= models.DateTimeField(auto_now_add= True)
      def __str__(self):
        return self.title
class Comment(models.Model):
      username=models.CharField(max_length=50)
      text = models.TextField()
      post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)