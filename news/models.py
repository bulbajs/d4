from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


class Author(models.Model):
    objects = None
    ratingAuthor = models.IntegerField(default=0)
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(args, kwargs)
    #     self.post_set = None


    def update_rating(self):
        postRat = self.post_set.aggregate(postRating=Sum('rating'))
        pRat = 0
        pRat += postRat.get('postRating') if postRat.get('postRating') else 0

        commentRat = self.authorUser.comment_set.aggregate(commentRating=Sum('rating'))
        cRat = 0
        cRat += commentRat.get('commentRating') if commentRat.get('commentRating') else 0


        self.ratingAuthor = pRat * 3 + cRat
        self.save()
        # return self.ratingAuthor


class Category(models.Model):
    objects = None
    name = models.CharField(max_length=128, unique=True)


class Post(models.Model):
    objects = None
    article = 'art'
    news = 'news'

    PUBLICATION = [
        (article, 'Статья'),
        (news, 'Новость'),
    ]

    postAuthor = models.ForeignKey(Author, on_delete=models.CASCADE)
    categoryType = models.CharField(max_length=4, choices=PUBLICATION, default=news)
    title = models.CharField(max_length=255)
    time_in_Post = models.DateTimeField(auto_now_add=True)
    time_out = models.DateTimeField(null=True)
    postCategory = models.ManyToManyField(Category, through='PostCategory')
    text = models.TextField()
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    # def preview(self):
    #     return '{} ... {}'.format(self.text[0:123], str(self.rating))

    def __str__(self):
        return f'{self.title}:{self.text[:50]}'


class PostCategory(models.Model):
    postThrough = models.ForeignKey(Post, on_delete=models.CASCADE)
    categoryThrough = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    commentText = models.TextField()
    time_in_Comment = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

