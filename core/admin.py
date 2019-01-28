from django.contrib import admin

from core.models import (
    Category, Gear, Weapon, Armor, Attachment,
    Vehicule, Starship, VehiculeAttachment, 
    Qualities, Book, Skill,
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    
    list_display = (
        'name',
        )
    

@admin.register(Gear)
class GearAdmin(admin.ModelAdmin):

    list_display = (
        'name','price',
        )


@admin.register(Weapon)
class WeaponAdmin(admin.ModelAdmin):
    
    list_display = (
        'name','skill','damage',
        'special','index','category',
        )


@admin.register(Armor)
class ArmorAdmin(admin.ModelAdmin):
   
    list_display = (
        'name','soak','encumberment',
        'price','rarity','index',
        )



@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    
    list_display = (
        'name','price','rarity','index','category'
        )


@admin.register(Vehicule)
class VehiculeAdmin(admin.ModelAdmin):
    
    list_display = (
        'name','silhouette','price',
        'rarity','index','category'
        )


@admin.register(Starship)
class StarshipAdmin(admin.ModelAdmin):
    
    list_display = (
        'name','silhouette','price',
        'rarity','index','category'
        )


@admin.register(VehiculeAttachment)
class VehiculeAttachmentAdmin(admin.ModelAdmin):
    
    list_display = (
        'name','price','rarity','index','category'
        )


@admin.register(Qualities)
class QualitiesAdmin(admin.ModelAdmin):
    
    list_display = (
        'name','active','ranked','index'
        )


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    
    list_display = (
        'name','system','translate','initials',
        )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):

    list_display = (
        'name',
    )