from django.test import TestCase
from django.utils import timezone

from todo_app.models import Tag, Task


class ModelsTest(TestCase):
    def test_tag_str(self):
        tag = Tag.objects.create(name="Test Tag")
        self.assertEqual(str(tag), tag.name)

    def test_task_str(self):
        task = Task.objects.create(
            content="Test Task",
            created_at=timezone.now(),
            deadline=timezone.now() + timezone.timedelta(days=1),
            is_done=False,
        )
        tag1 = Tag.objects.create(name="Tag1")
        tag2 = Tag.objects.create(name="Tag2")
        task.tags.set([tag1, tag2])

        expected_str = f"{task.content} - {'Done' if task.is_done else 'Not Done'}"
        self.assertEqual(str(task), expected_str)
