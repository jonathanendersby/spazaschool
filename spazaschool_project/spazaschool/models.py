from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class MyUserManager(BaseUserManager):
    def create_user(self, msisdn, first_name, last_name, secret_code,
                    password=None):

        if not msisdn:
            raise ValueError('Users must have an msisdn')

        user = self.model(
            msisdn=msisdn,
            first_name=first_name,
            last_name=last_name,
            secret_code=secret_code,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, msisdn, first_name, last_name, secret_code,
                         password):

        user = self.create_user(msisdn,
                                password=password,
                                first_name=first_name,
                                last_name=last_name,
                                secret_code=secret_code,
                                )
        user.is_admin = True
        user.save(using=self._db)
        return user


class City(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    msisdn = models.CharField(max_length=14, unique=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    display_name = models.CharField(max_length=50, null=True, blank=True)
    date_registered = models.DateTimeField(auto_now_add=True)
    secret_code = models.CharField(max_length=10)
    city = models.ForeignKey(City, null=True, blank=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'msisdn'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'secret_code']

    def get_full_name(self):
        # The user is identified by their email address
        return "%s %s" % (self.first_name, self.last_name)

    def get_short_name(self):
        # The user is identified by their email address
        return self.first_name

    # On Python 3: def __str__(self):
    def __unicode__(self):
        return self.msisdn

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin



class Module(models.Model):
    sort_order = models.IntegerField()
    name = models.CharField(max_length=120)
    description = models.TextField()
    published = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name


class ModuleSection(models.Model):
    name = models.CharField(max_length=120)
    sort_order = models.IntegerField()
    html_copy = models.TextField()


class Question(models.Model):
    sort_order = models.IntegerField()
    html_copy = models.TextField()
    published = models.BooleanField(default=True)
    points = models.IntegerField()
    linked_module_section = models.ForeignKey(ModuleSection, null=True)


class Answer(models.Model):
    question = models.ForeignKey(Question)
    html_copy = models.TextField()
    is_correct = models.BooleanField()
    post_html_copy = models.TextField()


class UserQuestion(models.Model):
    user = models.ForeignKey(User)
    question = models.ForeignKey(Question, null=True)
    answered_correctly = models.BooleanField(default=False)


class Badge(models.Model):
    name = models.CharField(max_length=120)
    sort_order = models.IntegerField()
    description = models.TextField()


class UserBadge(models.Model):
    user = models.ForeignKey(User)
    badge = models.ForeignKey(Badge)
    earned_date = models.DateTimeField(auto_now_add=True)


class PageCopy(models.Model):
    slug = models.CharField(max_length=50, db_index=True)
    html_copy = models.TextField()
