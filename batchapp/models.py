from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers

# Create your models here.
class Batch(models.Model):
    batch_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    batch_name = models.CharField(max_length=20)
    number_of_code = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.user}, {self.batch_name}"

class Codes(models.Model):
    code_id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=10)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)

class BatchSerializers(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = "__all__"

class CodesSerializers(serializers.ModelSerializer):
    batch = BatchSerializers()
    class Meta:
        model = Codes
        fields = "__all__"