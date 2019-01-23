from django.utils.translation import ugettext_lazy as _
from django.db.models import (
    Model, CharField, IntegerField,
    ForeignKey, PROTECT, PositiveSmallIntegerField
)



class Category(Model):

    name = CharField(_('category'), max_length=120)

    class Meta:  # pylint: disable=too-few-public-methods
        """Category Meta class"""

        verbose_name = _("category")
        verbose_name_plural = _("categories")
        ordering = ("name",)


class Gear(Model):

    name = CharField(_('name'), max_length=80)
    price = PositiveSmallIntegerField(_('price'), blank=False)
    encumberment = PositiveSmallIntegerField(_('encumberment'), blank=False)
    rarity = PositiveSmallIntegerField(_('rarity'), blank=False)
    index = CharField(_('index'), max_length= 80)
    category = ForeignKey(Category, on_delete=PROTECT, _('name'), blank=False)

    def __str__(self):
        return self.name

    class Meta:  # pylint: disable=too-few-public-methods
        """Gear Meta class"""

        verbose_name = _("gear")
        verbose_name_plural = _("gears")
        ordering = ("name", "category",)


class Weapon(Model):  

    name = CharField(_('name'), max_length=80)
    skill = CharField(_('skill'), max_length=80)
    damage = PositiveSmallIntegerField(_('damage'), blank=False)
    critical = PositiveSmallIntegerField(_('critical'), blank=False)
    rangemax = CharField(_('range'), max_length=80)
    encumberment = PositiveSmallIntegerField(_('encumberment'), blank=False)
    hardpoint = PositiveSmallIntegerField(_('hard point'), blank=False)
    price = PositiveSmallIntegerField(_('price'), blank=False)
    rarity = PositiveSmallIntegerField(_('rarity'), blank=False)
    special = CharField(_('range'), max_length=180)
    index = CharField(_('index'), max_length= 80)
    category = ForeignKey(Category, on_delete=PROTECT, _('name'), blank=False)

    def __str__(self):
        return self.name

    class Meta:  # pylint: disable=too-few-public-methods
        """Weapon Meta class"""

        verbose_name = _("weapon")
        verbose_name_plural = _("weapons")
        ordering = ("name", "category",)


class Armor(Model):  

    name = CharField(_('armor'), max_length=80)
    defense = PositiveSmallIntegerField(_('defense'), blank=False)
    soak = PositiveSmallIntegerField(_('soak'), blank=False)
    encumberment = PositiveSmallIntegerField(_('encumberment'), blank=False)
    hardpoint = PositiveSmallIntegerField(_('hard point'), blank=False)
    price = PositiveSmallIntegerField(_('price'), blank=False)
    rarity = PositiveSmallIntegerField(_('rarity'), blank=False)
    index = CharField(_('index'), max_length= 80)
    category = ForeignKey(Category, on_delete=PROTECT, _('name'), blank=False)

    def __str__(self):
        return self.name

    class Meta:  # pylint: disable=too-few-public-methods
        """Armor Meta class"""

        verbose_name = _("armor")
        verbose_name_plural = _("armors")
        ordering = ("name", "category",)


class Attachment(Model):  

    name = CharField(_('armor'), max_length=80)
    price = PositiveSmallIntegerField(_('price'), blank=False)
    encumberment = PositiveSmallIntegerField(_('encumberment'), blank=False)
    hardpoint = PositiveSmallIntegerField(_('hard point required'), blank=False)
    rarity = PositiveSmallIntegerField(_('rarity'), blank=False)
    index = CharField(_('index'), max_length= 80)
    category = ForeignKey(Category, on_delete=PROTECT, _('name'), blank=False)

    def __str__(self):
        return self.name

    class Meta:  # pylint: disable=too-few-public-methods
        """Attachment Meta class"""

        verbose_name = _("attachment")
        verbose_name_plural = _("attachements")
        ordering = ("name", "category",)    


class Vehicule(Model):  

    name = CharField(_('armor'), max_length=80)
    silhouette = PositiveSmallIntegerField(_('silhouette'), blank=False)
    speed = PositiveSmallIntegerField(_('speed'), blank=False)
    handling = IntegerField(_('handling'), blank=False)
    armor = PositiveSmallIntegerField(_('armor'), blank=False)
    defense = CharField(_('defense'), max_lenght=20)
    hull = PositiveSmallIntegerField(_('hull trauma'), blank=False)
    strain = PositiveSmallIntegerField(_('system strain'), blank=False)
    manufacturer = CharField(_('manufacturer'), blank=False)
    crew = PositiveSmallIntegerField(_('crew'), blank=False)
    encumberment = PositiveSmallIntegerField(_('encumberment'), blank=False)
    passenger = PositiveSmallIntegerField(_('passenger'), blank=False)
    hardpoint = PositiveSmallIntegerField(_('hard point'), blank=False)
    cost = PositiveSmallIntegerField(_('cost'), blank=False)
    weapon = CharField(_('weapon'), blank=False)
    rarity = PositiveSmallIntegerField(_('rarity'), blank=False)
    index = CharField(_('index'), max_length= 80)
    category = ForeignKey(Category, on_delete=PROTECT, _('name'), blank=False)

    def __str__(self):
        return self.name

    class Meta:  # pylint: disable=too-few-public-methods
        """Vehicule Meta class"""

        verbose_name = _("vehicule")
        verbose_name_plural = _("vehicules")
        ordering = ("name", "category",)


class Starship(Model):  

    name = CharField(_('armor'), max_length=80)
    silhouette = PositiveSmallIntegerField(_('silhouette'), blank=False)
    speed = PositiveSmallIntegerField(_('speed'), blank=False)
    handling = IntegerField(_('handling'), blank=False)
    armor = PositiveSmallIntegerField(_('armor'), blank=False)
    defense = CharField(_('defense'), max_lenght=20)
    hull = PositiveSmallIntegerField(_('hull trauma'), blank=False)
    strain = PositiveSmallIntegerField(_('system strain'), blank=False)
    manufacturer = CharField(_('manufacturer'), blank=False)
    hd_nc = CharField(_('hyperdrive/navicomputer'), blank=False)
    crew = PositiveSmallIntegerField(_('crew'), blank=False)
    encumberment = PositiveSmallIntegerField(_('encumberment'), blank=False)
    passenger = PositiveSmallIntegerField(_('passenger'), blank=False)
    hardpoint = PositiveSmallIntegerField(_('hard point'), blank=False)
    cost = PositiveSmallIntegerField(_('cost'), blank=False)
    weapon = CharField(_('weapon'), blank=False)
    rarity = PositiveSmallIntegerField(_('rarity'), blank=False)
    index = CharField(_('index'), max_length= 80)
    category = ForeignKey(Category, on_delete=PROTECT, _('name'), blank=False)

    def __str__(self):
        return self.name

    class Meta:  # pylint: disable=too-few-public-methods
        """starship Meta class"""

        verbose_name = _("starship")
        verbose_name_plural = _("starships")
        ordering = ("name", "category",)


class VehiculeAttachment(Model):  

    name = CharField(_('armor'), max_length=80)
    price = PositiveSmallIntegerField(_('price'), blank=False)
    hardpoint = PositiveSmallIntegerField(_('hard point required'), blank=False)
    rarity = PositiveSmallIntegerField(_('rarity'), blank=False)
    index = CharField(_('index'), max_length= 80)
    category = ForeignKey(Category, on_delete=PROTECT, _('name'), blank=False)

    def __str__(self):
        return self.name

    class Meta:  # pylint: disable=too-few-public-methods
        """Vehicule Attachment Meta class"""

        verbose_name = _("vehicule attachment")
        verbose_name_plural = _("vehicules attachements")
        ordering = ("name", "category",)    