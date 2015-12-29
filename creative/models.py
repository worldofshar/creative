from django.db import models
from passlib.hash import pbkdf2_sha256

# Create your models here.


class Repository(models.Model):
    name = models.CharField(max_length=200)
    tag = models.CharField(default="short", max_length=15)
    status = models.CharField(default="draft", max_length=15)
    content = models.TextField(max_length=100000)

    def __str__(self):
        return self.name


class AdminUser(models.Model):
    user = models.CharField(default="worldofshar", max_length=20)
    pwd = models.CharField(max_length=512)

    def set_pwd(self, password):
        pwd_hash = pbkdf2_sha256.encrypt(password, rounds=20000, salt_size=16)
        admin_user = AdminUser()
        admin_user.pwd = pwd_hash
        admin_user.save()

    def verify_pwd(self, password):
        pwd_hash = AdminUser.objects.filter(user="worldofshar")[0].pwd
        return pbkdf2_sha256.verify(password, pwd_hash)
