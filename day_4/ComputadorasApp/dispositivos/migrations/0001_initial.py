# Generated by Django 4.0.6 on 2022-07-22 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_component', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='InputDevice',
            fields=[
                ('component_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='dispositivos.component')),
                ('mark', models.CharField(max_length=50)),
            ],
            bases=('dispositivos.component',),
        ),
        migrations.CreateModel(
            name='OutputDevice',
            fields=[
                ('component_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='dispositivos.component')),
                ('mark', models.CharField(max_length=50)),
            ],
            bases=('dispositivos.component',),
        ),
        migrations.CreateModel(
            name='Display',
            fields=[
                ('outputdevice_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='dispositivos.outputdevice')),
                ('quantity', models.IntegerField()),
                ('cost', models.FloatField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            bases=('dispositivos.outputdevice',),
        ),
        migrations.CreateModel(
            name='Keyboard',
            fields=[
                ('inputdevice_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='dispositivos.inputdevice')),
                ('quantity', models.IntegerField()),
                ('cost', models.FloatField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            bases=('dispositivos.inputdevice',),
        ),
        migrations.CreateModel(
            name='Mouse',
            fields=[
                ('inputdevice_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='dispositivos.inputdevice')),
                ('quantity', models.IntegerField()),
                ('cost', models.FloatField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            bases=('dispositivos.inputdevice',),
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('outputdevice_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='dispositivos.outputdevice')),
                ('quantity', models.IntegerField()),
                ('cost', models.FloatField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            bases=('dispositivos.outputdevice',),
        ),
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('total_cost', models.FloatField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('display', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dispositivos.display')),
                ('keyboard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dispositivos.keyboard')),
                ('mouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dispositivos.mouse')),
                ('speaker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dispositivos.speaker')),
            ],
        ),
    ]
