from __future__ import unicode_literals
from django.db import models
from jsonfield import JSONField


class CentralState(models.Model):
    name = models.TextField(primary_key=True)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'central_state'


class ExportApiAudit(models.Model):
    export_api_auth = models.ForeignKey('ExportApiAuth', blank=True, null=True)
    request = models.TextField()

    class Meta:
        managed = False
        db_table = 'export_api_audit'


class ExportApiAuth(models.Model):
    enabled = models.BooleanField()
    username = models.TextField(unique=True)
    hash = models.TextField()
    salt = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'export_api_auth'
        unique_together = (('enabled', 'username'),)


class HostsPublish(models.Model):
    host = models.TextField()
    # This field type is a guess.
    country_code = models.TextField(blank=True, null=True)
    asn = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    sticky = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'hosts_publish'


class HostsPublishLog(models.Model):
    host = models.TextField()
    # This field type is a guess.
    country_code = models.TextField(blank=True, null=True)
    asn = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    sticky = models.BooleanField()
    action = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'hosts_publish_log'


class HostsRelated(models.Model):
    host = models.TextField()
    related = models.TextField()

    class Meta:
        managed = False
        db_table = 'hosts_related'


class HostsUnsupported(models.Model):
    host = models.TextField()
    # This field type is a guess.
    country_code = models.TextField(blank=True, null=True)
    asn = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hosts_unsupported'


class Samples(models.Model):
    host = models.TextField()
    # This field type is a guess.
    country_code = models.TextField(blank=True, null=True)
    asn = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    origin = models.TextField()  # This field type is a guess.
    type = models.TextField()  # This field type is a guess.
    token = models.TextField(blank=True, null=True)
    data = JSONField()
    extra_data = JSONField()

    class Meta:
        managed = False
        db_table = 'samples'


class SimpleSamples(models.Model):
    # This field type is a guess.
    country_code = models.TextField(blank=True, null=True)
    asn = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    type = models.TextField()  # This field type is a guess.
    origin_id = models.TextField(blank=True, null=True)
    data = JSONField()

    class Meta:
        managed = False
        db_table = 'simple_samples'


class Upgrades(models.Model):
    artifact = models.TextField()
    version = models.TextField()
    published = models.BooleanField()
    created_at = models.DateTimeField(blank=True, null=True)
    sha256sum = models.TextField()
    ed25519sig = models.TextField()

    class Meta:
        managed = False
        db_table = 'upgrades'
