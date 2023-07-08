from rest_framework.test import APITestCase
from authentication.models import User


class TestModel(APITestCase):

    def test_create_user(self):
        user= User.objects.create_user('Drey', 'drey@gmail.com', 'password123@')
        self.assertIsInstance(user,User)
        self.assertFalse(user.is_staff)
        self.assertEqual(user.email,'drey@gmail.com')

    def test_create_superuser(self):
        user= User.objects.create_superuser('Drey', 'drey@gmail.com', 'password123@')
        self.assertIsInstance(user,User)
        self.assertTrue(user.is_staff)
        self.assertEqual(user.email,'drey@gmail.com')

    def test_raises_error_when_no_username_is_supplied(self):
        self.assertRaises(ValueError,User.objects.create_user,username='', email='drey@gmail.com', password='password123@')

    def test_raises_error_with_message_when_no_username_is_supplied(self):
        with self.assertRaisesMessage(ValueError, 'The given username must be set'):
            User.objects.create_user(username='', email='drey@gmail.com', password='password123@')
    
    def test_raises_error_when_no_email_is_supplied(self):
        self.assertRaises(ValueError,User.objects.create_user,username='Drey', email='', password='password123@')

    def test_raises_error_with_message_when_no_email_is_supplied(self):
        with self.assertRaisesMessage(ValueError, 'The given email must be set'):
            User.objects.create_user(username='Drey', email='', password='password123@')    

    def test_cant_create_superuser_with_no_is_staff_status(self):
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_staff=True.'):
            User.objects.create_superuser(username='Drey', email='drey@gmail.com', password='password123@', is_staff=False)

    def test_cant_create_superuser_with_no_is_superuser_status(self):
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_superuser=True.'):
            User.objects.create_superuser(username='Drey', email='drey@gmail.com', password='password123@', is_superuser=False)