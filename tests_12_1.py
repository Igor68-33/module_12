# Простые Юнит-Тесты
import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5
        # print('wal=', self.distance)

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner_walk = Runner('Walk')
        for i in range(10):
            runner_walk.walk()
        self.assertEqual(runner_walk.distance, 50)

    def test_run(self):
        runner_run = Runner('Run')
        for i in range(10):
            runner_run.run()
        self.assertEqual(runner_run.distance, 100)

    def test_challenge(self):
        runner_walk = Runner('Walk')
        runner_run = Runner('Run')
        for i in range(10):
            runner_walk.walk()
            runner_run.run()
        self.assertNotEqual(runner_walk.distance, runner_run.distance)


if __name__ == '__main__':
    unittest.main()
