from django.db import models

ACTIVE = 'active'
STATUS_CHOICES = ((ACTIVE, 'Active'), ('blocked', 'Blocked'))


class Review(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Name')
    email = models.EmailField(null=False, blank=False, verbose_name='Email')
    text = models.TextField(max_length=1000, null=False, blank=False, verbose_name='Text')
    created = models.DateTimeField(auto_now_add=True,  verbose_name='Created')
    edited = models.DateTimeField(auto_now_add=True,  verbose_name='Edited')
    status = models.CharField(max_length=40, null=False, blank=False, verbose_name='Status', default=ACTIVE,
                              choices=STATUS_CHOICES)

    def __str__(self):
        return self.text