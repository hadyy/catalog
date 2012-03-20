from django.db import models
from django.forms import ModelForm
from datetime import *
from django.utils.translation import ugettext as _

class Category(models.Model):
	name = models.CharField(_("name"), max_length=50)
	sort = models.IntegerField(_("sort"), max_length=2, default=0, blank=True)

	def __unicode__(self):
		return u'%s' % (self.name)

	class Meta:
		verbose_name = _("category")
		verbose_name_plural = _("categories")

class Product(models.Model):
	name           = models.CharField(_("name"), max_length=256)
	description    = models.TextField(_("description"), blank=True)
	price          = models.IntegerField(_("price"), help_text=_("K.D"))
	category       = models.ForeignKey(Category, verbose_name=_('category'))
	photo          = models.ImageField(_("photo"), upload_to='products_images', null=True, help_text=_("570px x 270px"))
	photo_thumb    = models.ImageField(_("photo thumb"), upload_to='products_images/thumb', null=True, help_text=_("192px x 128px"))
	photo_large    = models.ImageField(_("photo large"), upload_to='products_images/large', null=True, help_text=_("582px x 387px"))
	show_in_slider = models.BooleanField(_("show_in_slider"), default=True)
	
	def __unicode__(self):
		return u'%s' % (self.name)

	class Meta:
		verbose_name = _("product")
		verbose_name_plural = _("products")

class Pages(models.Model):
	title = models.CharField(_("title"), max_length=60)
	content = models.TextField(_("content"))
	
	def __unicode__(self):
		return u'%s' % (self.title)

	class Meta:
		verbose_name = _("page")
		verbose_name_plural = _("pages")
		
class Order(models.Model):	
	SIZE_CHOICES = (
        ('43', _('4x3')),
        ('32', _('3x2')),
		('22', _('2x2')),
    )
	DELIVER_CHOICES = (
		('CD', _('CD')),
		('url', _('url')),
		('Printed', _('Printed')),
	)
	size    = models.CharField(_("size"), max_length=2, choices=SIZE_CHOICES)
	deliver = models.CharField(_("deliver"), max_length=30, choices=DELIVER_CHOICES)
	product = models.ForeignKey(Product, verbose_name=_('product'))
	groom   = models.CharField(_("groom"), max_length=60)
	da3i    = models.CharField(_("da3i"), max_length=60)
	date    = models.DateField(_("date"))
	place   = models.CharField(_("place"), max_length=60)
	phone   = models.CharField(_("phone"), max_length=50)
	generalinvite = models.BooleanField(_("general invite"), help_text=_("<span id='helptext'>would you want to add this sentence</span>"))
	contactname = models.CharField(_("contactname"), max_length=60)
	contactphone = models.CharField(_("contactphone"), max_length=60)
	email   = models.EmailField(_("email"))
	notes   = models.TextField(_("notes"), blank=True)
	status  = models.BooleanField(default=False)
	
	def __unicode__(self):
			return u'%s %s %s' % (self.name, self.email, self.date)

	class Meta:
		verbose_name = _("order")
		verbose_name_plural = _("orders")
	
class OrderForm(ModelForm):
	class Meta:
		model = Order
		exclude = ('product', 'status', )
