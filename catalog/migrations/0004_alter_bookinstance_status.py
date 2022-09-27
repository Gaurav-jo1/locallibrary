# Generated by Django 4.1.1 on 2022-09-27 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_bookinstance_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='status',
            field=models.CharField(blank=True, choices=[('Maintenance', 'Maintenance'), ('Loan', 'On loan'), ('Available', 'Available'), ('Reserved', 'Reserved')], default='Maintenance', help_text='Book availability', max_length=20),
        ),
    ]
