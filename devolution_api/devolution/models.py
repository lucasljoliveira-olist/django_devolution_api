from django.db import models

# Create your models here.
class DevolutionReason(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=200, null=False, blank=False)

class DevolutionStatus(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=200, null=False, blank=False)

class DevolutionType(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=200, null=False, blank=False)

class Devolution(models.Model):
    id_order = models.IntegerField()
    id_devolution_type = models.ForeignKey(
        DevolutionType,
        on_delete=models.RESTRICT
    )
    id_devolution_reason = models.ForeignKey(
        DevolutionReason,
        on_delete=models.RESTRICT
    )
    id_devolution_status = models.ForeignKey(
        DevolutionStatus,
        on_delete=models.RESTRICT
    )
    date = models.DateField(auto_now_add=True)
    buyer_reason = models.CharField(max_length=100, null=False, blank=False)


class DevolutionProductOrder(models.Model):
    id_order_product = models.IntegerField()
    id_devolution = models.ForeignKey(
        Devolution,
        on_delete=models.RESTRICT
    )
    id_devolution_status = models.ForeignKey(
        DevolutionStatus,
        on_delete=models.RESTRICT
    )

