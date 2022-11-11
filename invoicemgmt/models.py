from django.db import models

# Create your models here.
class Invoice(models.Model):
    comments = models.TextField(max_length=3000, default='', blank=True, null=True)
    invoice_number = models.IntegerField('Invoice Number:', blank=True, null=True)
    invoice_date = models.DateField('Date (YYYY-MM-DD):', auto_now_add=False, auto_now=False, blank=True, null=True)
    invoice_date_created = models.DateTimeField('Date Created:',auto_now_add=True, null=True)
    name = models.CharField('Client Name:', max_length=120, default='', blank=True, null=True)
    company_name = models.CharField('Company Name:', max_length=50, default='', blank=True, null=True)

    line_one = models.CharField('Item 1:', max_length=120, default='', blank=True, null=True)
    line_one_quantity = models.IntegerField('Quantity:', default=0, blank=True, null=True)
    line_one_unit_price = models.IntegerField('Price per Unit:', default=0, blank=True, null=True)
    line_one_total_price = models.IntegerField('Total (PHP):', default=0, blank=True, null=True)

    line_two = models.CharField('Item 2:', max_length=120, default='', blank=True, null=True)
    line_two_quantity = models.IntegerField('Quantity:', default=0, blank=True, null=True)
    line_two_unit_price = models.IntegerField('Price per Unit:', default=0, blank=True, null=True)
    line_two_total_price = models.IntegerField('Total (PHP):', default=0, blank=True, null=True)

    line_three = models.CharField('Item 3:', max_length=120, default='', blank=True, null=True)
    line_three_quantity = models.IntegerField('Quantity:', default=0, blank=True, null=True)
    line_three_unit_price = models.IntegerField('Price per Unit:', default=0, blank=True, null=True)
    line_three_total_price = models.IntegerField('Total (PHP):', default=0, blank=True, null=True)

    phone_number = models.CharField('Phone Number:', max_length=120, default='', blank=True, null=True)
    total = models.IntegerField(default='0', blank=True, null=True)
    balance = models.IntegerField(default='0', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True, blank=True)
    paid_choice = (
        ('Payment Complete', 'Payment Complete'),
        ('Payment not done', 'Payment not done'),
    )
    paid = models.CharField(max_length=50, default='', blank=True, null=True, choices=paid_choice)

    invoice_type_choice = (
        ('Receipt', 'Receipt'),
        ('Invoice', 'Invoice'),
    )
    invoice_type = models.CharField(max_length=50, default='', blank=True, null=True, choices=invoice_type_choice)


    def __str__(self):
        return self.name