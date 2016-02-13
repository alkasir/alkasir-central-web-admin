from django.contrib import admin
from .models import (CentralState, ExportApiAudit, ExportApiAuth, HostsPublish,
                     HostsPublishLog, HostsRelated, HostsUnsupported, Samples,
                     SimpleSamples, Upgrades)


class CentralStateAdmin(admin.ModelAdmin):
    list_display = ['name', 'value']


class ExportApiAuditAdmin(admin.ModelAdmin):
    list_display = ['export_api_auth', 'request']


class ExportApiAuthAdmin(admin.ModelAdmin):
    list_display = ['enabled', 'username', 'created_at']


class HostsPublishAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'host', 'country_code', 'asn', 'created_at', 'sticky']
    list_filter = ['sticky', 'country_code']
    readonly_fields = ['host', 'country_code', 'asn', 'created_at', 'sticky']


class HostsPublishLogAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'host', 'action', 'country_code', 'asn', 'created_at', 'sticky']
    list_filter = ['action', 'country_code']
    search_fields = ['host', 'asn']
    readonly_fields = ['host', 'country_code',
                       'asn', 'created_at', 'action', 'sticky']


class HostsRelatedAdmin(admin.ModelAdmin):
    list_display = ['id', 'host', 'related']


class HostsUnsupportedAdmin(admin.ModelAdmin):
    list_display = ['id', 'host', 'country_code', 'asn', 'created_at', ]
    list_filter = ['country_code']
    search_fields = ['host', 'asn']


class SamplesAdmin(admin.ModelAdmin):
    list_display = ['id', 'host', 'country_code', 'asn',
                    'created_at', 'origin', 'type']
    list_filter = ['type', 'origin', 'country_code']
    search_fields = ['token', 'country_code', 'host', 'type', 'asn', ]
    readonly_fields = ['created_at', 'type',
                       'country_code', 'asn', 'token', 'host', 'origin']


class SimpleSamplesAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'type', 'country_code', 'asn', 'created_at', 'origin_id', ]
    list_filter = ['type', 'country_code']
    readonly_fields = ['created_at', 'type',
                       'country_code', 'asn', 'origin_id', ]
    search_fields = ['data']


def publish_upgrades(modeladmin, request, queryset):
    queryset.update(published=True)

publish_upgrades.short_description = 'Publish upgrades'


def unpublish_upgrades(modeladmin, request, queryset):
    queryset.update(published=False)

unpublish_upgrades.short_description = 'Unpublish upgrades'


class UpgradesAdmin(admin.ModelAdmin):
    list_display = ['id', 'published', 'artifact',
                    'version', 'created_at']
    list_filter = ['published', 'artifact']
    search_fields = ['version', 'sha256sum', 'ed25519sig']
    actions = [publish_upgrades, unpublish_upgrades]


admin.site.register(CentralState, CentralStateAdmin)
admin.site.register(ExportApiAudit, ExportApiAuditAdmin)
admin.site.register(ExportApiAuth, ExportApiAuthAdmin)
admin.site.register(HostsPublish, HostsPublishAdmin)
admin.site.register(HostsPublishLog, HostsPublishLogAdmin)
admin.site.register(HostsRelated, HostsRelatedAdmin)
admin.site.register(HostsUnsupported, HostsUnsupportedAdmin)
admin.site.register(Samples, SamplesAdmin)
admin.site.register(SimpleSamples, SimpleSamplesAdmin)
admin.site.register(Upgrades, UpgradesAdmin)
