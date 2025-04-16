# Generated by Django 5.2 on 2025-04-15 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('nationality', models.CharField(blank=True, choices=[('AFEGANISTÃO', 'Afghanistan'), ('ALEMANHA', 'Germany'), ('ARGENTINA', 'Argentina'), ('AUSTRÁLIA', 'Australia'), ('ÁUSTRIA', 'Austria'), ('BÉLGICA', 'Belgium'), ('BOLÍVIA', 'Bolivia'), ('BRASIL', 'Brazil'), ('CANADÁ', 'Canada'), ('CHILE', 'Chile'), ('CHINA', 'China'), ('COLÔMBIA', 'Colombia'), ('COREIA DO SUL', 'South Korea'), ('CUBA', 'Cuba'), ('DINAMARCA', 'Denmark'), ('EGITO', 'Egypt'), ('EMIRADOS ÁRABES UNIDOS', 'United Arab Emirates'), ('ESPANHA', 'Spain'), ('ESTADOS UNIDOS', 'United States'), ('FILIPINAS', 'Philippines'), ('FINLÂNDIA', 'Finland'), ('FRANÇA', 'France'), ('GRÉCIA', 'Greece'), ('HOLANDA', 'Netherlands'), ('HONG KONG', 'Hong Kong'), ('HUNGRIA', 'Hungary'), ('ÍNDIA', 'India'), ('INDONÉSIA', 'Indonesia'), ('IRÃ', 'Iran'), ('IRAQUE', 'Iraq'), ('IRLANDA', 'Ireland'), ('ISLÂNDIA', 'Iceland'), ('ISRAEL', 'Israel'), ('ITÁLIA', 'Italy'), ('JAPÃO', 'Japan'), ('LÍBANO', 'Lebanon'), ('MÉXICO', 'Mexico'), ('MARROCOS', 'Morocco'), ('NIGÉRIA', 'Nigeria'), ('NORUEGA', 'Norway'), ('NOVA ZELÂNDIA', 'New Zealand'), ('PAQUISTÃO', 'Pakistan'), ('PERU', 'Peru'), ('POLÔNIA', 'Poland'), ('PORTUGAL', 'Portugal'), ('REINO UNIDO', 'United Kingdom'), ('REPÚBLICA TCHECA', 'Czech Republic'), ('RÚSSIA', 'Russia'), ('SUÉCIA', 'Sweden'), ('TAILÂNDIA', 'Thailand'), ('TURQUIA', 'Turkey')], max_length=100, null=True)),
            ],
        ),
    ]
