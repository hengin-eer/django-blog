from turtle import title
from django.db import models
from django.contrib.auth import get_user_model
import markdown

class Category(models.Model):
    name = models.CharField('カテゴリー', max_length=30)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    auther = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField('タイトル', max_length=100)
    slug = models.SlugField('URL', unique=True)
    intro = models.CharField('説明', max_length=200)
    body = models.TextField('本文')
    category = models.ForeignKey(
        Category, verbose_name='カテゴリー', on_delete=models.PROTECT
    )
    posted_date = models.DateField('作成日', auto_now_add=True)
    upgrade_date = models.DateField('更新日', auto_now=True)
    public = models.BooleanField('公開する', default=False, help_text="公開するにはチェックを入れて下さい")
    
    def __str__(self):
        return self.title
    
    def markdown_to_html(self):
        md = markdown.Markdown(
            extensions=['extra', 'admonition', 'sane_lists', 'toc'])
        html = md.convert(self.body)
        return html