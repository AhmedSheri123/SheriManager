# Generated by Django 4.1.1 on 2022-09-12 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_remove_userpaymentdata_is_payed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpaymentdata',
            name='pay_date',
            field=models.DateField(),
        ),
    ]
