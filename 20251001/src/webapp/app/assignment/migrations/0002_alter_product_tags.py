from django.db import migrations

import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ("assignment", "0001_initial"),
        (
            "taggit",
            (
                "0006_rename_taggeditem_content_type_object_id_"
                "taggit_tagg_content_8fc721_idx"
            ),
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="tags",
            field=taggit.managers.TaggableManager(
                blank=True,
                help_text="A comma-separated list of tags.",
                through="taggit.TaggedItem",
                to="taggit.Tag",
                verbose_name="Tags",
            ),
        ),
    ]
