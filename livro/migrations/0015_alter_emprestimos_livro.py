# Generated by Django 3.2.6 on 2021-09-16 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0014_alter_emprestimos_livro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimos',
            name='livro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='livro.livros'),
        ),
    ]
