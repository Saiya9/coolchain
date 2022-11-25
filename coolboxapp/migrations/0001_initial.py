# Generated by Django 4.1.3 on 2022-11-24 18:18

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('car_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('car_band', models.CharField(max_length=20)),
                ('total_coolbox_weight', models.FloatField(blank=True, null=True)),
                ('temp_max', models.FloatField(blank=True, null=True)),
                ('temp_min', models.FloatField(blank=True, null=True)),
                ('license_plate', models.CharField(max_length=15)),
                ('car_picture', models.ImageField(upload_to='Car_images')),
            ],
        ),
        migrations.CreateModel(
            name='Coolbox',
            fields=[
                ('coolbox_id', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('weight', models.FloatField(blank=True, null=True)),
                ('coolboxtemp_max', models.FloatField(blank=True, null=True)),
                ('coolboxtemp_min', models.FloatField(blank=True, null=True)),
                ('dimension', models.CharField(max_length=40)),
                ('d_measurement', models.CharField(max_length=40)),
                ('t_measurement', models.CharField(max_length=40)),
                ('total', models.FloatField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('Shipped', 'Shipped'), ('Shipping', 'Shipping'), ('Cancelled', 'Cancelled')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('driver_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('driver_user', models.CharField(max_length=30)),
                ('driver_password', models.CharField(max_length=30)),
                ('driver_fname', models.CharField(max_length=30)),
                ('driver_lname', models.CharField(max_length=30)),
                ('driver_email', models.CharField(max_length=30)),
                ('id_card', models.CharField(max_length=13)),
                ('driver_phone', models.CharField(max_length=30)),
                ('drivinglicense_id', models.CharField(max_length=30)),
                ('issue_date', models.DateField(blank=True, null=True)),
                ('expire_date', models.DateField(blank=True, null=True)),
                ('profile_driver', models.ImageField(default='/Driver_Images/default.png', upload_to='Driver_Images')),
            ],
        ),
        migrations.CreateModel(
            name='Type_medicine',
            fields=[
                ('type_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('type_name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='shipping',
            fields=[
                ('shipping_id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('ship_date', models.DateField(blank=True, null=True)),
                ('ship_time', models.TimeField(blank=True, null=True)),
                ('original', models.CharField(max_length=200)),
                ('destination', models.CharField(max_length=200)),
                ('car_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carfk', to='coolboxapp.car')),
                ('coolbox_id', models.ManyToManyField(to='coolboxapp.coolbox')),
                ('driver_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='driverfk', to='coolboxapp.driver')),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('medicine_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('medicine_name', models.CharField(max_length=50)),
                ('medicine_tempmax', models.FloatField(blank=True, null=True)),
                ('medicine_tempmin', models.FloatField(blank=True, null=True)),
                ('description', models.CharField(max_length=200)),
                ('total', models.FloatField(blank=True, null=True)),
                ('t_measurement', models.CharField(max_length=40)),
                ('medicine_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medicinetype', to='coolboxapp.type_medicine')),
            ],
        ),
        migrations.AddField(
            model_name='coolbox',
            name='medicine_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medicinename', to='coolboxapp.medicine'),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('admin_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('role_user', models.CharField(blank=True, choices=[('admin', 'ADMIN'), ('driver', 'DRIVER')], max_length=20)),
                ('id_card', models.CharField(max_length=13)),
                ('profile_user', models.ImageField(default='/Profile_Images/default.png', upload_to='Profile_Images')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]