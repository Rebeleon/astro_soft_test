from django.test import TestCase, Client
from epoch.models import LogEntry


class DataEndpointTestCase(TestCase):
    def test_data_endpoint_returns_json_with_timestamp(self):
        client = Client()
        headers = {
            'REMOTE_ADDR': '192.168.0.1',
            'HTTP_USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                               ' Chrome/58.0.3029.110 Safari/537.3',
            'HTTP_ACCEPT_LANGUAGE': 'en-US,en;q=0.9',
        }
        response = client.get('/data/', **headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().keys(), {'ts'})
        self.assertIsInstance(response.json().get('ts'), int)


class LogEntryTestCase(TestCase):
    def test_log_entry_creation(self):
        log_entry = LogEntry.objects.create(
            ip_address='127.0.0.1',
            user_agent='Mozilla/5.0',
            accept_language='en-US,en;q=0.9'
        )
        self.assertEqual(log_entry.ip_address, '127.0.0.1')
        self.assertEqual(log_entry.user_agent, 'Mozilla/5.0')
        self.assertEqual(log_entry.accept_language, 'en-US,en;q=0.9')
