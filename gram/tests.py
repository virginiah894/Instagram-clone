# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post,Comment,Profile

# Create your tests here.
class PostTestClass(TestCase):

    
    def setUp(self):
        self.Perry=User(username='perry',email='perry@gmail.com')
        self.profile = Profile(profile_photo = '',name='' ,bio='',follows ='')
        self.post= Post(author = 'perry',image='arusha.jpg', caption ='cool pic',posted_date='12/12/2011',likes='1', profile=self.profile)
    
    def test_instance(self):
        self.assertTrue(isinstance(self.post,Post))

    def test_save_method(self):
        self.post.save_post()
        posts = Post.objects.all()
        self.assertTrue(len(posts) > 0)

class ProfileTestClass(TestCase):

    
    def setUp(self):
        
        self.profile = Profile(profile_photo = '',name='' ,bio='',follows ='')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_save_method(self):
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)






class CommentTestClass(TestCase):

    
    def setUp(self):
        self.Perry=User(username='perry',email='perry@gmail.com')
        self.profile = Profile(profile_photo = '',name='' ,bio='',follows ='')
        self.comment = Comment(post = 'post1',comment ='cool pic', user=self.Perry,commented_on='12/12/2011')

    
    def test_instance(self):
        self.assertTrue(isinstance(self.comment,Comment))

    def test_save_method(self):
        self.comment.save_comment()
        comments = Comment.objects.all()
        self.assertTrue(len(comments) > 0)


    def tearDown(self):
        Post.objects.all().delete()
        Profile.objects.all().delete()
        Comment.objects.all().delete()
