# Generated by Django 4.2 on 2023-05-21 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_suscripcion"),
    ]

    operations = [
        migrations.CreateModel(
            name="Historial",
            fields=[
                ("id_historial", models.AutoField(primary_key=True, serialize=False)),
                ("nombre_historial", models.CharField(max_length=40)),
                ("precio_historial", models.IntegerField()),
                ("cantidad_historial", models.IntegerField()),
                (
                    "imagen_historial",
                    models.ImageField(null=True, upload_to="historia"),
                ),
            ],
            options={
                "db_table": "db_Historial",
            },
        ),
        migrations.CreateModel(
            name="TipoUsuario",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tipo", models.CharField(max_length=40)),
            ],
        ),
    ]
