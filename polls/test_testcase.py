from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Question


class AdditionalTestCaseTests(TestCase):

    def test_index_page_returns_200(self):
        
        """the polls index page should load successfully"""
        
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)

    def test_question_str_method(self):
        
        """the __str__ method of Question should return the question text"""
        
        question = Question.objects.create(
            question_text="Test Question",
            pub_date=timezone.now()
        )
        self.assertEqual(str(question), "Test Question")