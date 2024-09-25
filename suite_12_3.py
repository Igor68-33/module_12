import unittest
import tests_12_1
import tests_12_2

my_tests = unittest.TestSuite()
my_tests.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))
my_tests.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))

my_tests_runner = unittest.TextTestRunner(verbosity=2)
my_tests_runner.run(my_tests)
