# Generated by Django 3.2.18 on 2023-05-07 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=64)),
                ('code', models.CharField(max_length=3)),
            ],
        ),
        migrations.AlterField(
            model_name='flights',
            name='destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arival', to='flights.airport'),
        ),
        migrations.AlterField(
            model_name='flights',
            name='origin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departure', to='flights.airport'),
        ),
    ]