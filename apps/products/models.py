import mptt
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):

    parent = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        verbose_name=_('parent'),
        related_name='child',
    )
    title = models.CharField(
        _('title'),
        max_length=255,
    )
    weight = models.PositiveIntegerField(
        verbose_name=_('weight'),
        default=0,
        help_text=_('Rocord will be first with greate weight.'),
    )
    enabled = models.BooleanField(
        verbose_name=_('enabled'),
        default=True,
        help_text=_('show/hide'),
    )

    class Meta:
        verbose_name = _(u'category item')
        verbose_name_plural = _(u'category items')
        ordering = ['weight', 'title']

    def __unicode__(self):
        return self.title


class Shop(models.Model):

    title = models.CharField(
        _('title'),
        max_length=255,
    )
    address = models.CharField(
        _('address'),
        max_length=255,
    )
    weight = models.PositiveIntegerField(
        verbose_name=_('weight'),
        default=0,
        help_text=_('Rocord will be first with greate weight.'),
    )
    enabled = models.BooleanField(
        verbose_name=_('enabled'),
        default=True,
        help_text=_('show/hide'),
    )

    class Meta:
        verbose_name = _(u'shop item')
        verbose_name_plural = _(u'shop items')
        ordering = ['weight', 'title']

    def __unicode__(self):
        return self.title


class Product(models.Model):

    title = models.CharField(
        _('title'),
        max_length=255,
    )
    category = models.ForeignKey(
        Category,
        verbose_name=_('category item'),
    )
    weight = models.PositiveIntegerField(
        verbose_name=_('weight'),
        default=0,
        help_text=_('Rocord will be first with greate weight.'),
    )
    enabled = models.BooleanField(
        verbose_name=_('enabled'),
        default=True,
        help_text=_('show/hide'),
    )

    class Meta:
        verbose_name = _(u'product item')
        verbose_name_plural = _(u'product items')
        ordering = ['weight', 'title']

    def __unicode__(self):
        return self.title


class Cost(models.Model):

    product = models.ForeignKey(
        Product,
        verbose_name=_('product item'),
    )
    shop = models.ForeignKey(
        Shop,
        verbose_name=_('shop item'),
    )
    price = models.FloatField(
        verbose_name=_('price'),
    )

    class Meta:
        verbose_name = _(u'cost item')
        verbose_name_plural = _(u'cost items')
        ordering = ['product', 'shop']
        unique_together = ('product', 'shop')

    def __unicode__(self):
        return u'{0}:{1}'.format(self.product.title, self.shop.title)


mptt.register(Category,)
