# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-27 20:52
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    replaces = [
        ("post", "0001_initial"),
        ("post", "0002_auto_20160319_0936"),
        ("post", "0003_auto_20160319_2101"),
        ("post", "0004_auto_20160319_2323"),
        ("post", "0005_auto_20160612_2323"),
    ]

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=128, verbose_name="name")),
                (
                    "location",
                    models.CharField(
                        choices=[("I", "internal"), ("E", "external")],
                        max_length=1,
                        verbose_name="location",
                    ),
                ),
            ],
            options={"verbose_name": "contact", "verbose_name_plural": "contacts",},
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=128, verbose_name="name")),
                (
                    "grouping",
                    models.BooleanField(default=False, verbose_name="grouping"),
                ),
                (
                    "counting",
                    models.BooleanField(default=False, verbose_name="counting"),
                ),
            ],
            options={"verbose_name": "category", "verbose_name_plural": "categories",},
        ),
        migrations.CreateModel(
            name="Item",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateTimeField(auto_now_add=True, verbose_name="date")),
                (
                    "description",
                    models.CharField(max_length=128, verbose_name="description"),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="post.Category",
                        verbose_name="category",
                    ),
                ),
                (
                    "recipient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="received_items",
                        to="post.Contact",
                        verbose_name="recipient",
                    ),
                ),
                (
                    "sender",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sent_items",
                        to="post.Contact",
                        verbose_name="sender",
                    ),
                ),
            ],
            options={
                "ordering": ("date",),
                "verbose_name": "item",
                "verbose_name_plural": "items",
            },
        ),
        migrations.AlterModelOptions(
            name="category",
            options={
                "ordering": ["name"],
                "verbose_name": "category",
                "verbose_name_plural": "categories",
            },
        ),
    ]
