from django.test import TestCase
from django.core.exceptions import ValidationError
from task_manager.models import Position


class PositionModelTest(TestCase):

    def test_position_creation(self):
        position = Position.objects.create(name="Developer")
        self.assertIsInstance(position, Position)

    def test_str_representation(self):
        position = Position.objects.create(name="Developer")
        self.assertEqual(str(position), position.name)

    def test_unique_name(self):
        Position.objects.create(name="Developer")
        position = Position(name="DEVELOPER")
        with self.assertRaises(ValidationError):
            position.full_clean()

    def test_name_max_length(self):
        max_legth = Position._meta.get_field("name").max_length
        self.assertEqual(max_legth, 63)

    def test_name_ordering(self):
        Position.objects.create(name="Programmer")
        Position.objects.create(name="Analyst")
        Position.objects.create(name="Developer")

        positions = Position.objects.all()

        self.assertEqual(positions[0].name, "Analyst")
        self.assertEqual(positions[1].name, "Developer")
        self.assertEqual(positions[2].name, "Programmer")
