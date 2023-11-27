from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from todo_app.models import Task, Tag


class TaskListViewTest(TestCase):
    def test_task_list_view_status_code(self):
        response = self.client.get(reverse("todo_app:task-list"))
        self.assertEqual(response.status_code, 200)

    def test_task_list_view_template(self):
        response = self.client.get(reverse("todo_app:task-list"))
        self.assertTemplateUsed(response, "todo_app/task_list.html")

    def test_task_create_view_status_code(self):
        response = self.client.get(reverse("todo_app:task-create"))
        self.assertEqual(response.status_code, 200)

    def test_task_create_view_template(self):
        response = self.client.get(reverse("todo_app:task-create"))
        self.assertTemplateUsed(response, "todo_app/task_form.html")

    def test_task_update_view_status_code(self):
        task = Task.objects.create(content="Test Task", created_at=timezone.now())
        response = self.client.get(reverse("todo_app:task-update", kwargs={"pk": task.pk}))
        self.assertEqual(response.status_code, 200)

    def test_task_update_view_template(self):
        task = Task.objects.create(content="Test Task", created_at=timezone.now())
        response = self.client.get(reverse("todo_app:task-update", kwargs={"pk": task.pk}))
        self.assertTemplateUsed(response, "todo_app/task_form.html")

    def test_task_delete_view_status_code(self):
        task = Task.objects.create(content="Test Task", created_at=timezone.now())
        response = self.client.get(reverse("todo_app:task-delete", kwargs={"pk": task.pk}))
        self.assertEqual(response.status_code, 200)

    def test_task_delete_view_template(self):
        task = Task.objects.create(content="Test Task", created_at=timezone.now())
        response = self.client.get(reverse("todo_app:task-delete", kwargs={"pk": task.pk}))
        self.assertTemplateUsed(response, "todo_app/task_confirm_delete.html")


class TagListViewTest(TestCase):
    def test_tag_list_view_status_code(self):
        response = self.client.get(reverse("todo_app:tag-list"))
        self.assertEqual(response.status_code, 200)

    def test_tag_list_view_template(self):
        response = self.client.get(reverse("todo_app:tag-list"))
        self.assertTemplateUsed(response, "todo_app/tag_list.html")

    def test_tag_create_view_status_code(self):
        response = self.client.get(reverse("todo_app:tag-create"))
        self.assertEqual(response.status_code, 200)

    def test_tag_create_view_template(self):
        response = self.client.get(reverse("todo_app:tag-create"))
        self.assertTemplateUsed(response, "todo_app/tag_form.html")

    def test_tag_update_view_status_code(self):
        tag = Tag.objects.create(name="Test Tag")
        response = self.client.get(reverse("todo_app:tag-update", kwargs={"pk": tag.pk}))
        self.assertEqual(response.status_code, 200)

    def test_tag_update_view_template(self):
        tag = Tag.objects.create(name="Test Tag")
        response = self.client.get(reverse("todo_app:tag-update", kwargs={"pk": tag.pk}))
        self.assertTemplateUsed(response, "todo_app/tag_form.html")

    def test_tag_delete_view_status_code(self):
        tag = Tag.objects.create(name="Test Tag")
        response = self.client.get(reverse("todo_app:tag-delete", kwargs={"pk": tag.pk}))
        self.assertEqual(response.status_code, 200)

    def test_tag_delete_view_template(self):
        tag = Tag.objects.create(name="Test Tag")
        response = self.client.get(reverse("todo_app:tag-delete", kwargs={"pk": tag.pk}))
        self.assertTemplateUsed(response, "todo_app/tag_confirm_delete.html")
