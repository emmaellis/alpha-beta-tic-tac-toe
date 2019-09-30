import tictactoe
import unittest

class TestGameOver(unittest.TestCase):
	def test_game_over0(self):
		board0 = [[0, 1, 0], [1, 1, 0], [1, 0, 1]]
		self.assertEqual(tictactoe.gameOver(board0),(True, None), "Should be a tie")

	def test_game_over1(self):
		board1 = [[0, 1, 0], [1, 1, 0], [0, 1, 1]]
		self.assertEqual(tictactoe.gameOver(board1),(True, 1), "Win for x horizontally")
	
	def test_game_over2(self):
		board2 = [[1, 1, 1], [0, None, 0], [None, 1, 0]]
		self.assertEqual(tictactoe.gameOver(board2),(True, 1), "Win for x vertically")

	def test_game_over3(self):
		board3 = [[None, 1, 0], [1, None, 0], [1, 1, 0]]
		self.assertEqual(tictactoe.gameOver(board3),(True, 0), "Win for o horizontally")

	def test_game_over4(self):
		board4 = [[0, 0, 0], [1, None, 1], [1, 1, 0]]
		self.assertEqual(tictactoe.gameOver(board4),(True, 0), "Win for o vertically")
	
	def test_game_over5(self):
		board5 = [[1, 0, 0], [0, 1, 1], [1, 0, 1]]
		self.assertEqual(tictactoe.gameOver(board5),(True, 1), "Win for x diagonally")

	def test_game_over6(self):
		board6 = [[1, 0, 0], [0, 1, 1], [1, 1, 0]]
		self.assertEqual(tictactoe.gameOver(board6),(True, None), "It's a tie")

	def test_game_over7(self):
		board7 = [[0, None, 0], [1, None, 1], [1, 1, 0]]
		self.assertEqual(tictactoe.gameOver(board7),(False, None), "Game not over")

	def test_game_over8(self):
		board8 = [[0, 0, 0], [1, None, 1], [1, 1, 0]]
		self.assertEqual(tictactoe.gameOver(board8),(True, 0), "Win for o vertically")

class TestBestMove(unittest.TestCase):
	def test_game_over0(self):
		board0 = [[None, None, 0],[0, 1, 1],[None, None, 1]]
		self.assertEqual(tictactoe.bestMove(board0),(0,0), "Should be (0,0)")
	
	def test_game_over1(self):
		board1 = [[0, None, None], [1, 1, None], [None, None, None]]
		self.assertEqual(tictactoe.bestMove(board1),(1,2), "Should be (1,2)")



if __name__ == '__main__':
    unittest.main()

