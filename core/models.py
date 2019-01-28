from django.utils.translation import ugettext_lazy as _
from django.db.models import (
    Model, CharField, IntegerField,
    ForeignKey, PROTECT, PositiveSmallIntegerField,
    BooleanField, TextField,
)



class Category(Model):

    name = CharField(_('category'), max_length=120)

    def __str__(self):
        return str(self.name)

    class Meta:  # pylint: disable=too-few-public-methods
        """Category Meta class"""

        verbose_name = _("category")
        verbose_name_plural = _("categories")
        ordering = ("name",)


class Skill(Model):
    
    name = CharField(_('skill'), max_length=30)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = _("Skill")
        verbose_name_plural = _("Skills")
        ordering = ("name",)


class Qualities(Model):
    """
    Armor / Weapons Qualities (attributes)
    """

    name = CharField(_('Quality'), max_length=80)
    active = BooleanField(_('Active'))
    ranked = BooleanField(_('Ranked'))
    effect = TextField(_('Effect'))
    index = CharField(_('index'), max_length= 80)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = _("Quality")
        verbose_name_plural = _("Qualities")
        ordering = ("name",)


class Book(Model):

    name = CharField(_('book'), max_length=80)
    system = CharField(_('system'), max_length=80)
    translate = BooleanField(_('tanslate'), default=False)
    key = CharField(_('product key'), max_length=12)
    initials = CharField(_('initials'), max_length=12)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = _("Book")
        verbose_name_plural = _("Books")
        ordering = ("name","system","translate",)


class Gear(Model):

    name = CharField(_('name'), max_length=80)
    price = PositiveSmallIntegerField(_('price'), blank=False)
    legal = BooleanField(_('legal'), default=True)
    encumberment = PositiveSmallIntegerField(_('encumberment'), blank=False)
    rarity = PositiveSmallIntegerField(_('rarity'), blank=False)
    index = CharField(_('index'), max_length= 80)
    category = ForeignKey(Category, on_delete=PROTECT, related_name=_('Gear_Category'), blank=False)

    def __str__(self):
        return str(self.name)

    class Meta:  # pylint: disable=too-few-public-methods
        """Gear Meta class"""

        verbose_name = _("gear")
        verbose_name_plural = _("gears")
        ordering = ("name", "category",)


class Weapon(Model):  

    name = CharField(_('name'), max_length=80)
    skill = ForeignKey(Skill, on_delete=PROTECT, related_name=_('weapon_skill'), blank=False)
    damage = PositiveSmallIntegerField(_('damage'), blank=False)
    critical = PositiveSmallIntegerField(_('critical'), blank=False)
    rangemax = CharField(_('range'), max_length=80)
    encumberment = PositiveSmallIntegerField(_('encumberment'), blank=False)
    hardpoint = PositiveSmallIntegerField(_('hard point'), blank=False)
    price = PositiveSmallIntegerField(_('price'), blank=False)
    legal = BooleanField(_('legal'), default=True)
    rarity = PositiveSmallIntegerField(_('rarity'), blank=False)
    special = CharField(_('special'), max_length=180)
    index = CharField(_('index'), max_length= 80)
    category = ForeignKey(Category, on_delete=PROTECT, related_name=_('Weapon_Category'), blank=False)

    def __str__(self):
        return str(self.name)

    class Meta:  # pylint: disable=too-few-public-methods
        """Weapon Meta class"""

        verbose_name = _("weapon")
        verbose_name_plural = _("weapons")
        ordering = ("name", "category",)


class Armor(Model):  

    name = CharField(_('armor'), max_length=80)
    defense = PositiveSmallIntegerField(_('defense'), blank=False, default=0)
    soak = PositiveSmallIntegerField(_('soak'), blank=False)
    encumberment = PositiveSmallIntegerField(_('encumberment'), blank=False)
    hardpoint = PositiveSmallIntegerField(_('hard point'), blank=False)
    price = PositiveSmallIntegerField(_('price'), blank=False)
    legal = BooleanField(_('legal'), default=True)
    rarity = PositiveSmallIntegerField(_('rarity'), blank=False)
    index = CharField(_('index'), max_length= 80)

    def __str__(self):
        return str(self.name)

    class Meta:  # pylint: disable=too-few-public-methods
        """Armor Meta class"""

        verbose_name = _("armor")
        verbose_name_plural = _("armors")
        ordering = ("name", )


class Attachment(Model):  

    name = CharField(_('armor'), max_length=80)
    price = PositiveSmallIntegerField(_('price'), blank=False)
    legal = BooleanField(_('legal'), default=True)
    encumberment = PositiveSmallIntegerField(_('encumberment'), blank=False)
    hardpoint = PositiveSmallIntegerField(_('hard point required'), blank=False)
    rarity = PositiveSmallIntegerField(_('rarity'), blank=False)
    index = CharField(_('index'), max_length= 80)
    category = ForeignKey(Category, on_delete=PROTECT, related_name=_('Attachment_Category'), blank=False)

    def __str__(self):
        return str(self.name)

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
    defense = CharField(_('defense'), max_length=20)
    hull = PositiveSmallIntegerField(_('hull trauma'), blank=False)
    strain = PositiveSmallIntegerField(_('system strain'), blank=False)
    manufacturer = CharField(_('manufacturer'), blank=False, max_length=60)
    crew = PositiveSmallIntegerField(_('crew'), blank=False)
    encumberment = PositiveSmallIntegerField(_('encumberment'), blank=False)
    passenger = PositiveSmallIntegerField(_('passenger'), blank=False)
    hardpoint = PositiveSmallIntegerField(_('hard point'), blank=False)
    price = PositiveSmallIntegerField(_('cost'), blank=False)
    legal = BooleanField(_('legal'), default=True)
    weapon = CharField(_('weapon'), blank=False, max_length=80)
    rarity = PositiveSmallIntegerField(_('rarity'), blank=False)
    index = CharField(_('index'), max_length= 80)
    category = ForeignKey(Category, on_delete=PROTECT, related_name=_('Vehicule_Category'), blank=False)

    def __str__(self):
        return str(self.name)

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
    defense = CharField(_('defense'), max_length=20)
    hull = PositiveSmallIntegerField(_('hull trauma'), blank=False)
    strain = PositiveSmallIntegerField(_('system strain'), blank=False)
    manufacturer = CharField(_('manufacturer'), blank=False, max_length=60)
    hd_nc = CharField(_('hyperdrive/navicomputer'), blank=False, max_length=20)
    crew = PositiveSmallIntegerField(_('crew'), blank=False)
    encumberment = PositiveSmallIntegerField(_('encumberment'), blank=False)
    passenger = PositiveSmallIntegerField(_('passenger'), blank=False)
    hardpoint = PositiveSmallIntegerField(_('hard point'), blank=False)
    price = PositiveSmallIntegerField(_('cost'), blank=False)
    legal = BooleanField(_('legal'), default=True)
    weapon = CharField(_('weapon'), blank=False, max_length=80)
    rarity = PositiveSmallIntegerField(_('rarity'), blank=False)
    index = CharField(_('index'), max_length= 80)
    category = ForeignKey(Category, on_delete=PROTECT, related_name=_('Starship_Category'), blank=False)

    def __str__(self):
        return str(self.name)

    class Meta:  # pylint: disable=too-few-public-methods
        """starship Meta class"""

        verbose_name = _("starship")
        verbose_name_plural = _("starships")
        ordering = ("name", "category",)


class VehiculeAttachment(Model):  

    name = CharField(_('armor'), max_length=80)
    price = PositiveSmallIntegerField(_('price'), blank=False)
    legal = BooleanField(_('legal'), default=True)
    hardpoint = PositiveSmallIntegerField(_('hard point required'), blank=False)
    rarity = PositiveSmallIntegerField(_('rarity'), blank=False)
    index = CharField(_('index'), max_length= 80)
    category = ForeignKey(Category, on_delete=PROTECT, related_name=_('Vehicule_Attachment_Category'), blank=False)

    def __str__(self):
        return str(self.name)

    class Meta:  # pylint: disable=too-few-public-methods
        """Vehicule Attachment Meta class"""

        verbose_name = _("vehicule attachment")
        verbose_name_plural = _("vehicules attachements")
        ordering = ("name", "category",)    
