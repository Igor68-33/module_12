import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1

        # сортируем участников по скорости
        self.participants.sort(key=lambda x: x.speed, reverse=True)

        # продолжим стандартное выполнение
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)
                    break  # добавим чтобы работало правильно на малых дистанциях

        return finishers


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_walk(self):
        runner_walk = Runner('Walk')
        for i in range(10):
            runner_walk.walk()
        self.assertEqual(runner_walk.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_run(self):
        runner_run = Runner('Run')
        for i in range(10):
            runner_run.run()
        self.assertEqual(runner_run.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_challenge(self):
        runner_walk = Runner('Walk')
        runner_run = Runner('Run')
        for i in range(10):
            runner_walk.walk()
            runner_run.run()
        self.assertNotEqual(runner_walk.distance, runner_run.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        # print('Начинаем тестирование')
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = Runner('Усэйн', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)

    # забеги теперь не зависят от очерёдности передачи участников
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test1(self):
        tournament_90 = Tournament(90, self.runner_1, self.runner_3)
        self.all_result = tournament_90.start()
        self.all_results['test1'] = self.all_result
        self.assertEqual(self.all_result[max(self.all_result.keys())], 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test2(self):
        tournament_90 = Tournament(90, self.runner_2, self.runner_3)
        self.all_result = tournament_90.start()
        self.all_results['test2'] = self.all_result
        self.assertEqual(self.all_result[max(self.all_result.keys())], 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test3(self):
        tournament_90 = Tournament(1, self.runner_3, self.runner_1, self.runner_2)
        self.all_result = tournament_90.start()
        self.all_results['test3'] = self.all_result
        self.assertEqual(self.all_result[max(self.all_result.keys())], 'Ник')

    @classmethod
    def tearDownClass(cls):
        # print('Тестирование завершили')
        for i, j in cls.all_results.items():
            print('{', end='')
            for ii, jj in j.items():
                print(f'{ii}: {jj}', end=', ')
            print('\b\b}')


if __name__ == '__main__':
    unittest.main()
