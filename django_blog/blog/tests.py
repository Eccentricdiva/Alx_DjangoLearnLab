from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Post

User = get_user_model()

class PostCRUDTests(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='alice', password='password123')
        self.user2 = User.objects.create_user(username='bob', password='password123')
        self.post = Post.objects.create(title='Test Post', content='Hello world', author=self.user1)

    def test_list_view(self):
        resp = self.client.get(reverse('posts-list'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Test Post')

    def test_detail_view(self):
        resp = self.client.get(reverse('posts-detail', kwargs={'pk': self.post.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Hello world')

    def test_create_requires_login(self):
        resp = self.client.get(reverse('posts-create'))
        # redirect to login
        self.assertNotEqual(resp.status_code, 200)
        self.client.login(username='alice', password='password123')
        resp = self.client.post(reverse('posts-create'), {'title': 'New', 'content': 'Content'})
        self.assertEqual(Post.objects.filter(title='New').count(), 1)

    def test_update_only_author(self):
        # bob should not be able to edit alice's post
        self.client.login(username='bob', password='password123')
        resp = self.client.get(reverse('posts-update', kwargs={'pk': self.post.pk}))
        # should redirect or give 403 depending on middleware; ensure forbidden
        self.assertNotEqual(resp.status_code, 200)

        # author can edit
        self.client.login(username='alice', password='password123')
        resp = self.client.post(reverse('posts-update', kwargs={'pk': self.post.pk}), {'title': 'Updated', 'content': 'Changed'})
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'Updated')

    def test_delete_only_author(self):
        self.client.login(username='bob', password='password123')
        resp = self.client.post(reverse('posts-delete', kwargs={'pk': self.post.pk}))
        self.assertEqual(Post.objects.filter(pk=self.post.pk).exists(), True)

        self.client.login(username='alice', password='password123')
        resp = self.client.post(reverse('posts-delete', kwargs={'pk': self.post.pk}))
        self.assertFalse(Post.objects.filter(pk=self.post.pk).exists())
