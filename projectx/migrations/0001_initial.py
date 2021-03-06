# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-27 14:42
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import projectx.models.helpers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.ASCIIUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone_number', models.CharField(max_length=16, unique=True)),
                ('_user_type', models.CharField(choices=[('U', 'Unknown'), ('M', 'Main User')], default='U', max_length=1)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Apparel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('price', models.FloatField()),
                ('online', models.BooleanField()),
                ('link', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='ApparelTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x_coord', models.FloatField()),
                ('y_coord', models.FloatField()),
                ('apparel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectx.Apparel')),
            ],
        ),
        migrations.CreateModel(
            name='ApparelType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='HashTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='HashTagLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hashtag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectx.HashTag')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('geo_long', models.FloatField()),
                ('geo_lat', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media_type', models.CharField(choices=[('U', 'Unknown'), ('I', 'Image'), ('V', 'Video')], default='U', max_length=1)),
                ('media', models.FileField(blank=True, null=True, upload_to=projectx.models.helpers.item_upload_path)),
                ('thumbnail', models.FileField(blank=True, null=True, upload_to=projectx.models.helpers.item_upload_path)),
            ],
        ),
        migrations.CreateModel(
            name='Outfit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Save',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outfit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectx.Outfit')),
            ],
        ),
        migrations.CreateModel(
            name='MainUser',
            fields=[
                ('baseuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'main users',
            },
            bases=('projectx.baseuser',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='like',
            name='outfit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectx.Outfit'),
        ),
        migrations.AddField(
            model_name='hashtaglink',
            name='outfit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectx.Outfit'),
        ),
        migrations.AddField(
            model_name='comment',
            name='outfit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectx.Outfit'),
        ),
        migrations.AddField(
            model_name='appareltag',
            name='media',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectx.Media'),
        ),
        migrations.AddField(
            model_name='apparel',
            name='apparel_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='projectx.ApparelType'),
        ),
        migrations.AddField(
            model_name='apparel',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='projectx.Location'),
        ),
        migrations.AddField(
            model_name='baseuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='baseuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AddField(
            model_name='save',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectx.MainUser'),
        ),
        migrations.AddField(
            model_name='outfit',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectx.MainUser'),
        ),
        migrations.AddField(
            model_name='like',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectx.MainUser'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectx.MainUser'),
        ),
    ]
