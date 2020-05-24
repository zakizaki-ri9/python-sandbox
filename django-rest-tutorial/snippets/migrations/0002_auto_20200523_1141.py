# Generated by Django 3.0.6 on 2020-05-23 11:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("snippets", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="snippet",
            name="highlighted",
            field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="snippet",
            name="owner",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="snippets",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
