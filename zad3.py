
class Environment:
    def getTime(self):
        return datetime.now()

    def playWavFile(self, file) -> None:
        pass


class Checker:
    def __init__(self) -> None:
        self._env = Environment()
        self._was_played = False

    @property
    def was_played(self):
        return self._was_played

    def wavWasPlayed(self) -> None:
        self._was_played = True

    def resetWav(self) -> None:
        self._was_played = False

    def reminder(self) -> None:
        current_hour = self._env.getTime().hour
        if current_hour >= 17:
            self._env.playWavFile("some_file")
            self.wavWasPlayed()


from unittest import TestCase
from unittest.mock import *
from datetime import datetime

class TestChecker(TestCase):
    @patch.object(Environment, 'getTime')
    def test_reminder_before_17(self, mock_method) -> None:
        mock_method.return_value = datetime(2021, 6, 12, 16, 59, 0, 0)
        checker = Checker()
        checker.resetWav()
        checker.reminder()
        self.assertFalse(checker.was_played)

    @patch.object(Environment, 'getTime')
    def test_reminder_after_17(self, mock_method) -> None:
        mock_method.return_value = datetime(2021, 6, 12, 17, 1, 0, 0)
        checker = Checker()
        checker.resetWav()
        checker.reminder()
        self.assertTrue(checker.was_played)