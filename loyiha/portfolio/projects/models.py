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
