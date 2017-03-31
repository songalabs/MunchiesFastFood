from django.db import models
#class Restaurant(model.Models):
#    name = models.CharField(max_length=120,db_index=True)
#    class Meta:
#        ordering=('name', )
#        verbose_name = 'restaurant'
#        verbose_name_plural = 'restaurants'

#   def __str__(self):
#        return self.name

class Category(models.Model):
    name = models.CharField(max_length=120,db_index=True) #veg, non-veg
    slug = models.SlugField(max_length=120,db_index=True)

    class Meta:
        ordering=('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name



class Menu(models.Model):
    category = models.ForeignKey(Category, related_name="menu")
    name = models.CharField(max_length=120,db_index=True)
    image = models.ImageField(upload_to='menu/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering=('name', )


    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #   return reverse('restaurant:menu_detail', args=[self.id, self.slug])

# Create your models here.
