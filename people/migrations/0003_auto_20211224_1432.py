# Generated by Django 3.2.9 on 2021-12-24 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_auto_20211218_1808'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='customuser',
            name='phonenumber',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]