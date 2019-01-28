from modeltranslation.translator import register, TranslationOptions
from core.models import (
    Category, Gear, Weapon, Armor,
    Attachment, Vehicule, Starship,
    VehiculeAttachment, Qualities, Book,
    Skill,
    )


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Gear)
class GearTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Weapon)
class WeaponTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Armor)
class ArmorTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Attachment)
class AttachmentTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Vehicule)
class VehiculeTranslationOptions(TranslationOptions):
    fields = ('name', 'weapon',)

@register(Starship)
class StarshipTranslationOptions(TranslationOptions):
    fields = ('name', 'weapon',)

@register(VehiculeAttachment)
class VehiculeAttachmentTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Qualities)
class QualitiesTranslationOptions(TranslationOptions):
    fields = ('name', 'effect',)

@register(Book)
class BookTranslationOptions(TranslationOptions):
    fields = ('name', 'system',)

@register(Skill)
class SkillTranslationOptions(TranslationOptions):
    fields = ('name',)