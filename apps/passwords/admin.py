from reversion.admin import VersionAdmin
from django.contrib import admin
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

from models import Password, Category


class _AbstractModelAdmin(admin.ModelAdmin):
    save_on_top = True


class _AbstractVersionAdmin(VersionAdmin):
    history_latest_first = True
    ignore_duplicate_revisions = True


class CategoryAdmin(_AbstractModelAdmin):
    pass


class PasswordAdmin(_AbstractVersionAdmin, _AbstractModelAdmin):
    list_display = ('name', 'username', 'password_js', 'url_link', 'category', 'host', 'notes')
    list_filter = ('category',)
    list_per_page = 999999
    search_fields = ('name', 'url', 'category', 'host', 'notes')
    change_list_template = 'admin/passwords/password/change_list.html'

    class Media:
        js = (
            '/media/js/jquery-ui.min.js',
            '/media/js/ZeroClipboard.js',
            '/media/js/jquery.highlight.js',
            '/media/js/filter.js',
            '/media/js/copy_password.js',
            '/media/js/filter_list_collapse.js',
        )
        css = {
            'screen': (
                '/media/css/password_list.css',
            ),
        }

    def url_link(self, obj):
        markup = '<a href="{}" target="_blank" style="line-height: 18px;">' \
                 'Link</a>'
        return markup.format(obj.url) if obj.url else ''
    url_link.short_description = 'URL'
    url_link.allow_tags = True

    def queryset(self, request):
        qs = super(PasswordAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(owned_by__in=request.user.groups.all()).distinct(['id'])

    def has_change_permission(self, request, obj=None):
        if obj is None:
            return True  # So they can see the change list page
        if request.user.is_superuser:
            return True
        if obj.owned_by.filter(pk__in=[g.pk for g in request.user.groups.all()]).count():
            return True
        return False

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super(PasswordAdmin, self).get_search_results(request, queryset, search_term)
        if request.user.is_superuser:
            return queryset, use_distinct
        else:
            return queryset.filter(owned_by__in=request.user.groups.all()), use_distinct

    has_delete_permission = has_change_permission

    def password_js(self, obj):
        context = {'password_id': obj.pk}
        html = render_to_string('admin/passwords/password/password_widget.html',
                                context)
        return mark_safe(html)
    password_js.allow_tags = True
    password_js.short_description = 'Password'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Password, PasswordAdmin)
