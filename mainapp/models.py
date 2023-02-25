from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

# Create your models here.
from mailer.models import EmailConfiguration, Email


class AppConfig(models.Model):
    app = models.CharField(max_length=30, blank=True, null=True, default="main", unique=True)

    account_creation_email = models.ForeignKey(Email, blank=True, null=True, on_delete=models.SET_NULL,
                                               related_name="account_creation_Email")

    account_creation_emailconfig = models.ForeignKey(EmailConfiguration, blank=True, null=True,
                                                     on_delete=models.SET_NULL,
                                                     related_name="account_creation_email_config")

    reset_password_email = models.ForeignKey(Email, blank=True, null=True, on_delete=models.SET_NULL,
                                             related_name="password_reset_Email")
    reset_password_emailconfig = models.ForeignKey(EmailConfiguration, blank=True, null=True, on_delete=models.SET_NULL,
                                                   related_name="password_reset_email_config")

    activate_account_email = models.ForeignKey(Email, blank=True, null=True, on_delete=models.SET_NULL,
                                               related_name="account_activation_email")
    activate_account_emailconfig = models.ForeignKey(EmailConfiguration, blank=True, null=True,
                                                     on_delete=models.SET_NULL,
                                                     related_name="account_activation_email_config")

    order_placement_email = models.ForeignKey(Email, blank=True, null=True, on_delete=models.SET_NULL,
                                              related_name="order_placement_email")
    order_placement_emailconfig = models.ForeignKey(EmailConfiguration, blank=True, null=True,
                                                    on_delete=models.SET_NULL,
                                                    related_name="order_placement_emailconfig")

    payment_made_email = models.ForeignKey(Email, blank=True, null=True, on_delete=models.SET_NULL,
                                           related_name="payment_made_email")
    payment_made_emailconfig = models.ForeignKey(EmailConfiguration, blank=True, null=True,
                                                 on_delete=models.SET_NULL, related_name="payment_made_emailconfig")

    application_url = models.CharField(blank=True, null=True, max_length=255)
    listing_activated = models.BooleanField(default=True)
    account_creation_activated = models.BooleanField(default=True)

    def __str__(self):
        return f"Application {self.app}"


class Tag(models.Model):
    name = models.CharField(blank=False, null=False, max_length=50)

    created_on = models.DateTimeField(auto_created=True, auto_now_add=True)
    updated_on = models.DateTimeField(auto_created=True, auto_now=True)

    def __str__(self):
        return self.name


class Blog(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=500, blank=False, null=False)
    slug = models.SlugField(blank=True, null=True)
    body = models.TextField(blank=False, null=False)
    tags = models.ManyToManyField(Tag, blank=True)
    image = models.ImageField(upload_to="blogs/images/", blank=True, null=True)

    created_on = models.DateTimeField(auto_created=True, auto_now_add=True)
    updated_on = models.DateTimeField(auto_created=True, auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Blog, self).save(*args, **kwargs)


class Reply(models.Model):

    author = models.CharField(max_length=100)
    blog = models.ForeignKey(Blog, blank=False, null=True, on_delete=models.CASCADE)
    comment = models.TextField()
    email = models.EmailField()

    created_on = models.DateTimeField(auto_created=True, auto_now_add=True)
    updated_on = models.DateTimeField(auto_created=True, auto_now=True)

    def __str__(self):
        return self.author
