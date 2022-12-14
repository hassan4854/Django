from django.test import TestCase, Client

from tasks.models import Task


class TestTasks(TestCase):
    def setUp(self):
        self.client = Client()

    def test_create_task(self):
        count_before_request = Task.objects.count()

        task = '| This task added right now | Testing |'
        response = self.client.post('/tasks/', {'task': task})

        content = response.content.decode('utf-8').strip()
        expected = "Task Created: '{}'".format(task)
        self.assertEqual(expected, content, "\nتابع مورد نظر باید عبارت Task Created: '{task_name}' را بازگرداند.")

        count_after_request = Task.objects.count()
        self.assertEqual(count_after_request, count_before_request + 1, '\nتسکی که با متد POST دریافت می‌کنید را باید با استفاده از تابع create یا تابع save ذخیره کنید.')