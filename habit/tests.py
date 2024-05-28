from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from habit.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    def setUp(self):
        """
        Устанавливаем начальные данные для тестов.
        Создаем двух пользователей и одну привычку.
        """
        self.user = User.objects.create(email="smth@mail.com", is_superuser=True)

        self.client.force_authenticate(user=self.user)

        self.habit = Habit.objects.create(
            place="your favorite place", action="do_something"
        )

        # Создаем второго пользователя для тестов
        # self.user = User.objects.create(email="example@example.com", is_superuser=True)

    def test_get_list(self):
        """
        Тестируем получение списка привычек.
        """
        url = reverse("habit:list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_habit(self):
        """
        Тестируем создание новой привычки.
        """
        data = {
            "place": self.habit.place,
            "owner": self.user.id,
            "action": self.habit.action,
        }
        url = reverse("habit:create")
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Habit.objects.all().exists())
        self.assertEqual(response.json()["place"], data["place"])
        self.assertEqual(response.json()["action"], data["action"])

    def test_update_habit(self):
        habit = Habit.objects.create(
            user=self.user, place="Test", action="Test", is_pleasant=True, period=1
        )
        data_habit_change = {
            "name": "Test_1",
        }
        response = self.client.patch(
            reverse("habit:update", kwargs={"pk": habit.pk}), data=data_habit_change
        )
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_delete_habit(self):
        habit = Habit.objects.create(
            user=self.user, place="Test", action="Test", is_pleasant=True, period=1
        )
        response = self.client.delete(reverse("habit:delete", kwargs={"pk": habit.pk}))
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
