from django.db import models


class News(models.Model):
    id_news = models.IntegerField(primary_key=True)
    rank = models.IntegerField()
    url = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200)
    text = models.TextField()
    time_ago = models.CharField(max_length=200)
    comments_count = models.IntegerField()
    score = models.IntegerField()
    sitestr = models.CharField(max_length=200)

    def __str__(self):
        return f"id: {self.id_news}, url: {self.url}, rank: {self.rank}, Title: {self.text[:50]}, Comments_count: {self.comments_count}, time_ago: {self.time_ago}, user_name: {self.user_name}," \
               f" score: {self.score}, sitestr: {self.sitestr}"