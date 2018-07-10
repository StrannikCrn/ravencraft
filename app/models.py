from django.db import models
import os

class NewsCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Категория статей'
        verbose_name_plural = 'Категории статей'


class News(models.Model):
    url = models.CharField(max_length=255, verbose_name="URL",default="")
    name = models.CharField(max_length=255, verbose_name="Название")
    date = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Дата")
    short_description = models.CharField(max_length=255,verbose_name="Короткое описание")
    text = models.TextField(verbose_name="Текст")
    category = models.ForeignKey(NewsCategory, verbose_name="Категория",related_name="category",on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to="app/static/images/news/", verbose_name="Картинка",
                                    null=True)

    def filename(self):
        if self.image.name is None:
            return ""
        return os.path.basename(self.image.name)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости и статьи'


class NewsPhotoSpecif(models.Model):
    news_item = models.ForeignKey(News,related_name="gallery_photos",verbose_name="Фото в галлерею",on_delete=models.CASCADE)
    image = models.ImageField(upload_to="News/", verbose_name="Фото")

    def __str__(self):
        return str("")

    class Meta:
        verbose_name = 'Фото в галлерею'
        verbose_name_plural = 'Фото в галлерею'

class Level(models.Model):
    value = models.IntegerField(verbose_name="Уровень")
    def __str__(self):
        return str(self.value)

    class Meta:
        verbose_name = 'Уровень'
        verbose_name_plural = 'Уровни'


class Wineglasses(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    text = models.TextField(default="",verbose_name="Краткое описание")
    image = models.ImageField(upload_to="bottles_groups/", verbose_name="Фотография", null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Бокал'
        verbose_name_plural = 'Бокалы'


class BottleProperties(models.Model):
    name = models.CharField(max_length=255,verbose_name="Название")
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Свойство'
        verbose_name_plural = 'Свойства'


class BeerGroup(models.Model):
    name = models.CharField(max_length=255,verbose_name="Название")
    url = models.CharField(max_length=255,default="", verbose_name="Url")
    image = models.ImageField(upload_to="bottles_groups/", verbose_name="Иконка")
    image2 = models.ImageField(upload_to="bottles_groups/", null=True, verbose_name="Иконка (неактивн.)")
    text = models.TextField(verbose_name="Текст", default="")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип пива'
        verbose_name_plural = 'Типы пива'


class FilterTag(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    url = models.CharField(max_length=255,default="", verbose_name="url")
    group = models.ForeignKey(BeerGroup, related_name="cat", null=True, verbose_name="Тип пива",on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег для фильтра'
        verbose_name_plural = 'Теги для фильтра'


class Bottle(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    sub_name = models.CharField(max_length=255,verbose_name="Транслит",default="")
    drink_with = models.CharField(max_length=255,verbose_name="Пить с")
    drink_from = models.ForeignKey(Wineglasses, verbose_name="Пить из",on_delete=models.SET_NULL,null=True)
    group = models.ForeignKey(BeerGroup,null=True, verbose_name="Тип пива",on_delete=models.SET_NULL)
    temperature = models.IntegerField(verbose_name="Пить при")
    ABV = models.DecimalField(max_digits=3,decimal_places=1, verbose_name="ABV")
    OG = models.IntegerField(verbose_name="OG")
    IBU = models.IntegerField(verbose_name="IBU")
    image_index = models.ImageField(upload_to="app/static/images/bottles/", verbose_name="Фото", null=True)
    image_index_dark = models.ImageField(upload_to="app/static/images/bottles", verbose_name="Фото (затемнённое)", null=True)
    image_big = models.ImageField(upload_to="app/static/images/bottles/", verbose_name="Фото большое", null=True)
    text = models.TextField(default="", verbose_name="Текст")
    composition = models.TextField(default="",verbose_name="Состав")
    volume = models.CharField(default="",max_length=20,verbose_name="Объем")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пиво'
        verbose_name_plural = 'Пиво'


class BottleTagSpecif(models.Model):
    bottle = models.ForeignKey(Bottle, related_name="tag", verbose_name="Бутылка",on_delete=models.CASCADE)
    tag = models.ForeignKey(FilterTag, related_name="filter_tag", verbose_name="Тег для фильтра",on_delete=models.CASCADE)

    def __str__(self):
        return self.tag.name
    class Meta:
        verbose_name = 'Тег для фильтра'
        verbose_name_plural = 'Теги для фильтра'


class BottlePropLevelSpecif(models.Model):
    bottle = models.ForeignKey(Bottle, default= "", related_name="properties", verbose_name="Бутылка",on_delete=models.CASCADE)
    prop_id = models.ForeignKey(BottleProperties, related_name="prop", verbose_name="Свойство",on_delete=models.CASCADE)
    level_id = models.ForeignKey(Level, related_name="level", verbose_name="Уровень",on_delete=models.CASCADE)

    def __str__(self):
        return self.prop_id.name
    class Meta:
        verbose_name = 'Свойство пива'
        verbose_name_plural = 'Свойства пива'


class NewsBottleSpecif(models.Model):
    news_item = models.ForeignKey(News, related_name="news_item_specif", verbose_name="Новость",on_delete=models.CASCADE)
    bottle = models.ForeignKey(Bottle, related_name="bottle", verbose_name="Бутылка",on_delete=models.CASCADE)

    def __str__(self):
        return self.bottle.name
    class Meta:
        verbose_name = 'Пиво к новости'
        verbose_name_plural = 'Пиво к новости'

