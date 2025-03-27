from django.test import TestCase


from django.urls import reverse, resolve
from student_app.views import All_Students, Single_Student


class Test_urls(TestCase):

  def test_001_all_students(self):
    url = resolve(reverse('all_student'))

    with self.subTest():
      self.assertEquals(url.route, 'student/')
    
    self.assertTrue(url.func.view_class is All_Students)