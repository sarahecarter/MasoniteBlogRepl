"""BlogTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.Blog import Blog


class BlogTableSeeder(Seeder):
    def run(self):
        Blog.create({"title": "My Morning", "body": "This morning I ate a delicious breakfast at the new cafe on my street"})
        Blog.create({"title": "My Birthday", "body": "For my birthday, my friends and I went to a farm and did goat yoga."})
        Blog.create({"title": "My Cat", "body": "I have the cutest cat ever. His name is Cas."})
