from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=150)
    landing_page = models.ImageField(upload_to='landingpage/')
    description = HTMLField()
    link= models.CharField(max_length=255)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    screenshot1 = models.ImageField(upload_to='screenshots/')
    screenshot2 = models.ImageField(upload_to='screenshots/')
    screenshot3 = models.ImageField(upload_to='screenshots/')
    screenshot4 = models.ImageField(upload_to='screenshots/')
    design = models.IntegerField(blank=True,default=0)
    usability = models.IntegerField(blank=True,default=0)
    creativity = models.IntegerField(blank=True,default=0)
    content = models.IntegerField(blank=True,default=0)
    overall_score = models.IntegerField(blank=True,default=0)
    country = models.ForeignKey(countries,on_delete=models.CASCADE)
    technologies = models.ManyToManyField(technologies)
    categories = models.ManyToManyField(categories)
    colors = models.ManyToManyField(colors)
    post_date = models.DateTimeField(auto_now_add=True)
    avatar = models.ImageField(upload_to='avatars/')

    def __str__(self):
        return self.title

    @classmethod
    def search_project(cls,search_term):
        # projects = cls.objects.filter(Q(username__username=search_term) | Q(title__icontains=search_term) | Q(colors__colors=search_term) | Q(technologies__technologies=search_term) | Q(categories__categories=search_term) | Q(country__countries=search_term))
        projects = cls.objects.filter(Q(username__username=search_term) | Q(title__icontains=search_term) | Q(country__countries=search_term) | Q(overall_score__icontains=search_term))
        return projects