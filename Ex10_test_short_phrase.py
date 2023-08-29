class TestExample:
    def test_short_phrase(self):
        phrase = input("Set a phrase:")
        expected_result = 15
        assert len(phrase) <= expected_result, f"Длинна строки более {expected_result}"
