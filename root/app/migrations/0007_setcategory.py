# Generated by Django 4.1.3 on 2022-11-15 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_delete_setcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='SetCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardSetId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cardset')),
                ('categoryId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category')),
            ],
            options={
                'db_table': 'omniflash_set_category',
            },
        ),
    ]
