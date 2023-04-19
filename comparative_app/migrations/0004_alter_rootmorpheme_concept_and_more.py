# Generated by Django 4.2 on 2023-04-14 21:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comparative_app', '0003_rename_name_affixalmorpheme_morph_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rootmorpheme',
            name='concept',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='root_morphemes', to='comparative_app.concept'),
        ),
        migrations.AlterField(
            model_name='rootmorpheme',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='root_morphemes', to='comparative_app.language'),
        ),
    ]
