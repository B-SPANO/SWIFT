from django.db.models import (
    Model, CharField, IntegerField,
    BooleanField,
    )
from django.utils.translation import ugettext_lazy as _


class WeaponMelee(Model):
    """
    Model of harvestable Melee Weapons
    """
    name = CharField(_('Name'), max_length=120)
    Price = IntegerField(_('Price'), blank=False)
    Rarity = IntegerField(_('Rarity'), blank=False)
    Blueprint = BooleanField(_('Blueprint'), blank=True, default=False)

    class Meta:
        verbose_name = _('Melee Weapon')
        verbose_name_plural = _('Melee Weapons')

    def __str__(self):
        return self.name


class WeaponRanged(Model):
    """
    Model of harvestable Ranged Weapons
    """
    name = CharField(_('Name'), max_length=120)
    Price = IntegerField(_('Price'), blank=False)
    Rarity = IntegerField(_('Rarity'), blank=False)
    Blueprint = BooleanField(_('Blueprint'), blank=True, default=False)

    class Meta:
        verbose_name = _('Ranged Weapon')
        verbose_name_plural = _('Ranged Weapons')

    def __str__(self):
        return self.name


class Armor(Model):
    """
    Model of harvestable Armor
    """
    name = CharField(_('Name'), max_length=120)
    Price = IntegerField(_('Price'), blank=False)
    Rarity = IntegerField(_('Rarity'), blank=False)
    Blueprint = BooleanField(_('Blueprint'), blank=True, default=False)

    class Meta:
        verbose_name = _('Armor')
        verbose_name_plural = _('Armors')

    def __str__(self):
        return self.name


class Gadget(Model):
    """
    Model of harvestable Gadgets and other misc items
    """
    name = CharField(_('Name'), max_length=120)
    Price = IntegerField(_('Price'), blank=False)
    Rarity = IntegerField(_('Rarity'), blank=False)
    Blueprint = BooleanField(_('Blueprint'), blank=True, default=False)

    class Meta:
        verbose_name = _('Gadget')
        verbose_name_plural = _('Gadgets')

    def __str__(self):
        return self.name


class Droid(Model):
    """
    Model of harvestable Droids
    """
    name = CharField(_('Name'), max_length=120)
    Price = IntegerField(_('Price'), blank=False)
    Rarity = IntegerField(_('Rarity'), blank=False)
    Blueprint = BooleanField(_('Blueprint'), blank=True, default=False)

    class Meta:
        verbose_name = _('Doid')
        verbose_name_plural = _('Droids')

    def __str__(self):
        return self.name


class Vehicule(Model):
    """
    Model of harvestable vehicules
    """
    name = CharField(_('Name'), max_length=120)
    Price = IntegerField(_('Price'), blank=False)
    Rarity = IntegerField(_('Rarity'), blank=False)
    Blueprint = BooleanField(_('Blueprint'), blank=True, default=False)

    class Meta:
        verbose_name = _('Vehicule')
        verbose_name_plural = _('Vehicules')

    def __str__(self):
        return self.name