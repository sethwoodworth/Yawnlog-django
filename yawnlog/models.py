# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class AverageSleeps(models.Model):
    """
    I think this is what displays the average sleep time on the front page of YL.
    """
    id = models.IntegerField(primary_key=True)
    value = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'average_sleeps'

class Feedbacks(models.Model):
    """
    Meta: Site feedback. By site-user. Only 765 characters in length (modify this?)
    """
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(null=True, blank=True)
    body = models.TextField(blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    response = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'feedbacks'

class Friends(models.Model):
    """
    Graph database, edges. Should check t osee if this is the best way of doing this. non-directional?
    """
    id = models.IntegerField(primary_key=True)
    user_id_1 = models.IntegerField(null=True, blank=True)
    user_id_2 = models.IntegerField(null=True, blank=True)
    accepted = models.IntegerField(null=True, blank=True)
    rejected = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'friends'

class News(models.Model):
    """
    Site news, might depricate.
    """
    id = models.IntegerField(primary_key=True)
    text = models.TextField(blank=True)
    title = models.CharField(max_length=765, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'news'

class SchemaMigrations(models.Model):
    """
    Depricated, from rails.
    """
    version = models.CharField(unique=True, max_length=765)
    class Meta:
        db_table = u'schema_migrations'

class Sleeps(models.Model):
    """
    The heart of the matter. Zip ~= location.
    """
    id = models.IntegerField(primary_key=True)
    start = models.DateTimeField(null=True, blank=True)
    stop = models.DateTimeField(null=True, blank=True)
    user_id = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    zip = models.CharField(max_length=765, blank=True)
    quality = models.IntegerField(null=True, blank=True)
    note = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'sleeps'

class Tags(models.Model):
    """
    Not sure where this is used.
    """
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'tags'

class UserLogins(models.Model):
    """
    Handy meta-model for seeing if accounts are active or not.
    """
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(null=True, blank=True)
    username = models.CharField(max_length=765, blank=True)
    password = models.CharField(max_length=765, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'user_logins'

class Users(models.Model):
    """
    Everything we want to know about a person...
    We need to migrate this to django.Users and user_profile, as well as expand the system.
    """
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=765, blank=True)
    email = models.CharField(max_length=765, blank=True)
    password = models.CharField(max_length=765, blank=True)
    realname = models.CharField(max_length=765, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    public_profile = models.IntegerField(null=True, blank=True)
    zip = models.CharField(max_length=765, blank=True)
    target_hours = models.DecimalField(null=True, max_digits=11, decimal_places=0, blank=True)
    twitter = models.CharField(max_length=765, blank=True)
    admin = models.IntegerField(null=True, blank=True)
    last_login_at = models.DateTimeField(null=True, blank=True)
    last_sleep_at = models.DateTimeField(null=True, blank=True)
    num_of_sleeps = models.IntegerField(null=True, blank=True)
    pw_reset = models.IntegerField(null=True, blank=True)
    user_login_id = models.IntegerField(null=True, blank=True)
    screen_name = models.CharField(max_length=765, blank=True)
    token = models.CharField(max_length=765, blank=True)
    secret = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'users'

