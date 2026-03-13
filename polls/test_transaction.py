from django.test import TransactionTestCase
from django.utils import timezone

from .models import Question

"""tests that a question object can be created and saved correctly in the database"""
class PollsTransactionTests(TransactionTestCase):
    reset_sequences = True

    def test_question_is_saved_to_database(self):
        Question.objects.create(
            question_text="Transaction test question",
            pub_date=timezone.now(),
        )
        self.assertEqual(Question.objects.count(), 1)