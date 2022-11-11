import unittest
import Task


class TestTask(unittest.TestCase):

    def setUp(self):
        self.game_stamps = Task.generate_game()

    def test_offset_number(self):
    	# If inputed offset number in list
        index = self.game_stamps[45]
        offset = index['offset']
        away, home = index['score']['away'], index['score']['home']
        self.assertEqual((home, away), Task.get_score(self.game_stamps, offset))
        # If inputed offset number in list
        answer = "List not contain scores for current offset!"
        self.assertEqual(answer, Task.get_score(self.game_stamps, -100))

    def test_offset_is_str(self):
    	# If offset id number in str type
        index = self.game_stamps[25]
        offset = str(index['offset'])
        away, home = index['score']['away'], index['score']['home']
        self.assertEqual((home, away), Task.get_score(self.game_stamps, offset))
        # Check if offset is some str
        self.assertEqual("Inputed offset is incorrect!", Task.get_score(self.game_stamps, "some_word"))

    def test_incorrect_game_stamps_list(self):
    	# If game stamps is not a list
        self.assertEqual("Input correct list of game's stamps!", Task.get_score({"This is" : "not list"}, 25))
        # If game stamps is list with incorrect inner dict
        self.game_stamps = [{5: 0, 'score': {'away': 0, 'home': 0}}]
        self.assertEqual("Input correct list of game's stamps!", Task.get_score(self.game_stamps, 0))
        self.game_stamps = [{'offset': 5, 'not score': {'away': 0, 'home': 0}}]
        self.assertEqual("Input correct list of game's stamps!", Task.get_score(self.game_stamps, 0))
        self.game_stamps = [{'offset': 0, 'score': {'not away': 0, 'home': 0}}]
        self.assertEqual("Input correct list of game's stamps!", Task.get_score(self.game_stamps, 0))
        self.game_stamps = [{'offset': 0, 'score': {'away': 0, 'not home': 0}}]
        self.assertEqual("Input correct list of game's stamps!", Task.get_score(self.game_stamps, 0))

if __name__ == "main":
    unittest.main()
