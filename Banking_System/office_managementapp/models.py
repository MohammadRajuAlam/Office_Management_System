from django.db import models
from django.utils import timezone
# Create your models here.

class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)

class SoftDeleteModel(models.Model):
    deleted_at = models.DateTimeField(null=True, blank=True)

    objects = SoftDeleteManager()
    all_objects = models.Manager()  # To access both deleted and non-deleted objects

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        self.deleted_at = None
        self.save()

    class Meta:
        abstract = True

class Company(SoftDeleteModel):
    company_name=models.CharField(max_length=100)
    company_id=models.CharField(
        max_length=10,
        unique=True,
        error_messages={
            'unique':"Company Id is already used."
            }
        )
    address=models.CharField(max_length=255)
    # you can write more fields
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.company_name}'
    
    class Meta:
        ordering=['company_name']
        
class Branch(SoftDeleteModel):
    company=models.ForeignKey(Company, on_delete=models.CASCADE)
    branch_name=models.CharField(max_length=100)
    branch_id=models.CharField(
        max_length=10,
        unique=True,
        error_messages={
            "unique":"branch id is already used."
            }
        )
    
    def __str__(self):
        return f'{self.branch_name}'
    
    class Meta:
        ordering=['branch_name']