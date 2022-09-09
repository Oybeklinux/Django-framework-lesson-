# Mavzu 7. Kirish

## Reja:


- virtual nomli yangi virtual muhit ochamiz

```text
>>> python -m venv virtual
```

- django va rasm bilan ishlovchi pillow kutubhonasini o'rnatamiz

```text
>>> pip install django
>>> pip install pillow
```

- portfolio nomli loyiha ochamiz

```text
>>> django-admin startproject portfolio
```

- portfolio katalogiga kirib users va projects nomli ilovalar qo'shamiz

```text
>>> python manage.py startapp users
>>> python manage.py startapp projects
```

- ilovalarni ro'yxatdan o'tkazamiz

<p><b>portfolio/settings.py</b></p>

```text
...

INSTALLED_APPS = [
    ...
    'projects.apps.ProjectsConfig',
    'users.apps.UsersConfig'
]

...
```

- Loyihani ishga tushirib tekshirib ko'ramiz

```text
python manage.py runserver
```

![](../7.%20Kirish/img.png)

- projects ilovasiga tegishli modellarni yozamiz:

<p><b>projects/models.py</b></p>

```text
from django.db import models
from users.models import Profile


class Project(models.Model):
    title = models.CharField(max_length=100)  # Majburiy
    description = models.TextField(blank=True, null=True)  # Majburiy emas
    image = models.ImageField(upload_to='projects', default='projects/empty.png') # Majburiy emas
    demo_link = models.CharField(max_length=200, blank=True, null=True) # Majburiy emas
    source_code = models.CharField(max_length=200, blank=True, null=True) # Majburiy emas
    vote_count = models.IntegerField(default=0) # Majburiy emas
    vote_ratio = models.IntegerField(default=0) # Majburiy emas
    created = models.DateField(auto_now_add=True) # Majburiy emas
    user = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name="projects") # Majburiy emas
    tag = models.ManyToManyField('Tag', blank=True, related_name="project_tag") # Majburiy emas

    def __str__(self):
        return f"{self.title}"


class Message(models.Model):
    subject = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateField(auto_now_add=True)
    sender = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name="sender_message")
    receiver = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name="receiver_message")

    def __str__(self):
        return f"{self.subject}"


class Skill(models.Model):
    name = models.CharField(max_length=10)
    description = models.TextField()
    created = models.DateField(auto_now_add=True)
    user = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name="user_skills")

    def __str__(self):
        return f"{self.name}"


class Review(models.Model):
    body = models.TextField()
    value = models.IntegerField(default=0)
    user = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.body}"


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

```

- users ilovasiga tegishli modellarni yozamiz:

<p><b>projects/users.py</b></p>


```text
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=False, null=False)
    profile_image = models.ImageField(upload_to='portfolio')
    social_github = models.CharField(max_length=100, blank=True, null=True)
    social_telegram = models.CharField(max_length=100, blank=True, null=False)
    social_instagram = models.CharField(max_length=100, default="instagram")
    social_youtube = models.CharField(max_length=100, blank=True, null=True)
    social_website = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.last_name} {self.user.first_name}"

```

- bazaga tadbiq qilamiz

```text
>>> python manage.py makemigrations
>>> python manage.py migrate
```

- dinamik fayllar katalogini ko'rsatib qo'yamiz

<p><b>portfolio/settings.py</b></p>

```text
...
MEDIA_ROOT = "/media/"
...
```

- statik fayllar katalogini ko'rsatib qo'yamiz

<p><b>portfolio/settings.py</b></p>

```text
...
STATIC_ROOT = "/static/"
...
```

- static va dinamik fayllarni URL orqali ochish uchun quyidagi sozlashlarni bajaramiz

<p><b>portfolio/settings.py</b></p>


```text
...

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

...
```

<p><b>portfolio/urls.py</b></p>

```text
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
]

# rasm, fayl, videolarni url orqali ochish uchun
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# css, jss va boshqa static fayllarni url orqali ochish uchun
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

- Signallarni ulaymiz

<p><b>users/models.py</b></p>

```text
...

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

...

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    user = instance
    if created:
        Profile.objects.create(
            user=user
        )


@receiver(post_delete, sender=Profile)
def delete_user(sender, instance, **kwargs):
    user = instance.user
    user.delete()
```

- admin foydalanuvchi kiritamiz

```text
python manage.py createsuperuser
```
- Admin Paneldan ko'rish uchun modellarni admin.py ga qo'shib chiqamiz
- Admin Panel orqali quyidagi ma'lumotlarni kiritamiz

User 

| username    | first_name | last_name   | password |
|-------------|------------|-------------|----------|
| Asror       | Asror      | Abduvosiqov | 123!@qwQ |
| Murod       | Murod      | Kusherbayev | 123!@qwQ |
| Husniddin   | Husniddin  | Muminov     | 123!@qwQ |
| Diyor       | Diyor      | Malikov     | 123!@qwQ |

Profile

| user      | bio | location                    | image         | github                                            | telgram      |
|-----------|-----|-----------------------------|---------------|---------------------------------------------------|--------------|
| Asror     | ... | Toshkent sh. Yunusobod t.   | Asror.png     |                                                   |              |
| Diyor     | ... | Toshkent sh. Sergeli t.     | Diyor.png     |                                                   |              |
| Husniddin | ... | Toshkent v. Zagiota tumani  | Husniddin.png | https://17husniddin.github.io/Potfolio/index.html | @husniddin17 |   
| Murod     | ... | Toshkent sh. Mirzo Ulu'bek  | Murod.png     |                                                   |              |

Izoh: Rasmlarni [bu yerdan](../resurslar/Theme/images) olishingiz mumkin

Skill

| name       |
|------------|
| Python     |
| Django     |
| DRF        |
| React      |
| Javascript |
| HTML, CSS  |
| NextJs     |


- Bitiruvchilarga quyidagi malakalarni biriktiramiz:

- Asror: Python, Django, DRF
- Murod: Javascript, React
- Husniddin: CSS,HTML, Python, Django
- Diyor: Javascript, React, NextJs

Project

| user      | title                    | image         | vote_count | vote_ratio | description | Tag               |
|-----------|--------------------------|---------------|------------|------------|-------------|-------------------|
| Asror     | IT Academy online ta'lim | project-1.png | 100        | 60         | lorem ipsum | Python, Django    |
| Murod     | Kannas-textile           | project-5.png | 50         | 90         | lorem ipsum | React, Javascript |
| Husniddin | Alimax pro               | project-6.png | 300        | 90         | lorem ipsum | CSS, HTML         |
| Diyor     | ePark.uz                 | project-2.png | 150        | 20         | lorem ipsum | React, Javascript |
| Diyor     | ЧД - че думаеш?          | project-3.png | 200        | 10         | lorem ipsum | React, Javascript |
| Diyor     | Dolina capital           | project-4.png | 30         | 70         | lorem ipsum | React, Javascript |

Review

![](img_1.png)
 

- Loyihalarni qaytaruvchi url yasaymiz

<p><b>projects/view.py</b></p>

```text

```