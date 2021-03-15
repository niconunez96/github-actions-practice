from main.dog import Dog


class TestDog:

    def test_it_should_print_bark_one_time(self):
        dog = Dog()
        assert "guau" == dog.greet(1)

    def test_it_should_print_bark_two_times(self):
        dog = Dog()
        assert "guauguau" == dog.greet(2)
