from django.db import models
from django.contrib import admin
from django.utils.text import slugify
from django.db.models.signals import post_save
from catalog.ctlg.Thumbnail import ThumbnailImageField
from pytils import translit


class Unit(models.Model):
    sub = models.ForeignKey('Category', related_name='units')
    name = models.CharField(max_length=50)
    image = ThumbnailImageField(upload_to='photos', null=True, blank=True)
    slug = models.SlugField(editable=False, null=True, unique=True)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return u'{self.id}: {self.name}'.format(self=self)

    def get_absolute_url(self):
        return u'{old}/prod/{self.slug}'.format(self=self, old=self.sub.get_absolute_url())

    @staticmethod
    def post_save(sender, **kwargs):
        my_unit = kwargs['instance']
        my_unit.slug = slugify(translit.translify(u'{slug}_{id}'.format(slug=my_unit.name, id=my_unit.id)))
        post_save.disconnect(Unit.post_save, sender=Unit)
        my_unit.save()
        post_save.connect(Unit.post_save, sender=Unit)


class Category(models.Model):
    sub = models.ForeignKey('Category', related_name='categories', null=True, blank=True)
    name = models.CharField(max_length=50)
    slug = models.SlugField(editable=False, null=True, unique=True)
    image = ThumbnailImageField(upload_to='photos', null=True)

    def __unicode__(self):
        return u'{self.id}: {self.name}'.format(self=self)

    def get_absolute_url(self):
        if self.sub is None:
            return u'{self.slug}'.format(self=self)
        else:
            return u'{old}/{self.slug}'.format(self=self, old=self.sub.get_absolute_url())

    @staticmethod
    def post_save(sender, **kwargs):
        my_category = kwargs['instance']
        my_category.slug = slugify(translit.translify(u'{slug}_{id}'.format(slug=my_category.name, id=my_category.id)))
        post_save.disconnect(Category.post_save, sender=Category)
        my_category.save()
        post_save.connect(Category.post_save, sender=Category)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'sub')


class UnitAdmin(admin.ModelAdmin):
    list_display = ('name', 'sub')


admin.site.register(Unit, UnitAdmin)
admin.site.register(Category, CategoryAdmin)

post_save.connect(Unit.post_save, sender=Unit)
post_save.connect(Category.post_save, sender=Category)