import runner
import unittest

class RunnerTest(unittest.TestCase):

    def test_walk(self, walker=None):
        walker = runner.Runner("Тестовая дорожка для бега")#объект класса Runner с произвольным именем
        for _ in range(10):
            walker.walk() #
        self.assertEqual(walker.distance, 50,
                         "Пройденное расстояние должно составлять 50 км после 10-кратной ходьбы")

    def test_run(self, running=None):
        running = runner.Runner("Запуск тестового бегуна")
        for _ in range(10):
            running.run()
        self.assertEqual(running.distance, 100,
                         "После 10-кратного пробега дистанция должна составить 100 км")

    def test_challenge(self):
        runner1 = runner.Runner("TestRunner1")
        runner2 = runner.Runner("TestRunner2")

        for _ in range(10):
            runner1.run()  # Первый бегун выполняет 10 пробежек
            runner2.walk()  # Второй бегун выполняет 10 прогулок

        self.assertNotEqual(runner1.distance, runner2.distance,
                            "Расстояния после бега и ходьбы не должны быть одинаковыми")


# Запуск тестов
if __name__ == "__main__":
    unittest.main()

