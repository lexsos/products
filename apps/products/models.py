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

    class Meta:
        verbose_name = _(u'category item')
        verbose_name_plural = _(u'category items')
        ordering = ['title', ]

    def __unicode__(self):
        return self.title


mptt.register(Category,)
