from django.contrib.auth.models import User
from news.models import Author, Category, Post, Comment

# 1. Создать двух пользователей
# (с помощью метода User.objects.create_user('username')).
# Создал 7 пользователей

User.objects.create_user(username='bulba')
User.objects.create_user(username='psyduck')
User.objects.create_user(username='bulb')
User.objects.create_user(username='Dan')
User.objects.create_user(username='Bob')
User.objects.create_user(username='Bulba')
User.objects.create_user(username='Psyduck')
User.objects.create_user(username='artem')

# 2. Создать два объекта модели Author, связанные с пользователями.
# Создал 4 автора

u1 = User.objects.get(pk=1)
Author.objects.create(authorUser=u1)
u3 = User.objects.get(pk=3)
Author.objects.create(authorUser=u3)
u6 = User.objects.get(pk=6)
Author.objects.create(authorUser=u6)
u7 = User.objects.get(pk=7)
Author.objects.create(authorUser=u7)

# 3. Добавить 4 категории в модель Category.
# Добавил 5 категорий

Category.objects.create(name='Sport')
Category.objects.create(name='Investing')
Category.objects.create(name='IT')
Category.objects.create(name='Humor')
Category.objects.create(name='Blog')

# 4. Добавить 2 статьи и 1 новость.
# Добавил 2 статьи и 2 новости

a1 = Author.objects.get(pk=1)
a2 = Author.objects.get(pk=2)
a3 = Author.objects.get(pk=3)
a4 = Author.objects.get(pk=4)

Post.objects.ctreate(postAuthor=a1, categoryType="art", title="1/64 finals",
                     text="Medvedev defeated Giron 6:0, 6:1, 6:2")
Post.objects.ctreate(postAuthor=a2, categoryType="art", title="1 USD = 85 RUB", text="oil = gold?")
Post.objects.ctreate(postAuthor=a3, categoryType="news", title="Dubai in shoсk!",
                     text="Durov did a hundred push-ups in one go")
Post.objects.ctreate(postAuthor=a4, categoryType="news", title="10 cup", text="Djokovic  is champion again")


# 5. Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий).

Post.objects.get(pk=1).postCategory.add(Category.objects.get(pk=1))
Post.objects.get(pk=1).postCategory.add(Category.objects.get(pk=2))
Post.objects.get(pk=2).postCategory.add(Category.objects.get(pk=2))
Post.objects.get(pk=3).postCategory.add(Category.objects.get(pk=3))
Post.objects.get(pk=3).postCategory.add(Category.objects.get(pk=4))
Post.objects.get(pk=4).postCategory.add(Category.objects.get(pk=1))


# 6. Создать как минимум 4 комментария к разным объектам модели Post
# (в каждом объекте должен быть как минимум один комментарий).

Comment.objects.create(commentPost=Post.objects.get(pk=2), commentUser=Author.objects.get(pk=4).authorUser,
                       commentText="Когда будет 100?")
Comment.objects.create(commentPost=Post.objects.get(pk=1), commentUser=Author.objects.get(pk=1).authorUser,
                       commentText="Джоковича пройдет?")
Comment.objects.create(commentPost=Post.objects.get(pk=2), commentUser=Author.objects.get(pk=4).authorUser,
                       commentText="Уже 75")
Comment.objects.create(commentPost=Post.objects.get(pk=2), commentUser=Author.objects.get(pk=3).authorUser,
                       commentText="А что с биткоином?")
Comment.objects.create(commentPost=Post.objects.get(pk=3), commentUser=Author.objects.get(pk=2).authorUser,
                       commentText="Дуров, ай красавец")
Comment.objects.create(commentPost=Post.objects.get(pk=1), commentUser=Author.objects.get(pk=4).authorUser,
                       commentText="Хорошая новость")


# 7. Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов.
# Рейтинг автора и рейтинг постов считает и обновляет

# Расставил лайки/дизлайки постам/комментариям:
Post.objects.get(id=1).like()
Post.objects.get(id=2).dislike()  # И так далее по аналогии
# Далее можно определить самый популярный пост или понравившийся комментарий
a = Post.objects.order_by('-rating')[:1]
b = Comment.objects.order_by('-rating')  # Так мы увидим весь список по убыванию


# 8. Обновить рейтинги пользователей.

a1 = Author.objects.get(id=1)
a2 = Author.objects.get(id=2)
a3 = Author.objects.get(id=3)
a4 = Author.objects.get(id=4)
a1.update_rating()
a1.ratingAuthor
a2.update_rating()
a2.ratingAuthor
a3.update_rating()
a3.ratingAuthor
a4.update_rating()
a4.ratingAuthor


# 9. Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).

a1 = Author.objects.order_by('-ratingAuthor')[:1]
for i in a:
    print(i.authorUser.username, 'имеет рейтинг = ', i.ratingAuthor)  # Ответ: "Bulba имеет рейтинг = 27"

av = Author.objects.order_by('-ratingAuthor').values('authorUser__username','ratingAuthor')[0] # Второй способ


# 10. Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на
# лайках/дизлайках к этой статье.

b = Post.objects.order_by('-rating').values('postAuthor_authorUser_username', 'rating', 'title')[0]

bp = Post.objects.order_by('rating')[0]
bp1 = Post.objects.order_by('rating')[0].preview()

# 11. Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.

Post.objects.order_by('-rating')[0].comment_set.all().values('commentUser__username','time_in_Comment','rating', 'commentText')

