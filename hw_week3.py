import pytest
import requests

class TestPhraseTerminal:

    def test_phrase_input(self):
        answer = input("Please, enter word or phrase shorter than 15 symbols: ")

        assert len(answer) <= 15, f"You phrase is more than 15 symbols "
