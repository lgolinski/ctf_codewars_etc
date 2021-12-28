"""
Morse code cryptography module tests.
"""

import unittest
import sys
import test_data
sys.path.append('../../modules/crypto/')
import morse_code


class MorseCodeTestCase(unittest.TestCase):

    def test_decrypt_unique_morse_code_for_every_letter_and_digit(self):
        """Every letter [a-zA-Z] and digit[0-9] should have unique morse code"""
        all_codes = test_data.morse_code_dictionary
        for k, v in all_codes.items():
            act = morse_code.decrypt(v)
            self.assertEqual(act, k)

        # check if all codes are unique. Since I'm using dictionary then keys must be unique.
        unique_values = set(all_codes.values())
        self.assertEqual(len(unique_values), len(all_codes))

    def test_encrypt_spaces_in_text_should_be_translated_on_slash(self):
        """Every space character in text should be translated on / in text"""
        given_text = "test morse code"
        expected_encrypt = "- . ... - / -- --- .-. ... . / -.-. --- -.. ."

        result = morse_code.encrypt(given_text)

        self.assertEqual(expected_encrypt, result)

    def test_encrypt_not_recognized_characters(self):
        """Encrypt - Every not recognized character should be changed to # sign"""
        given_text = "Som123~```!@#$%^&*()_+}"
        expected_encrypt = '... --- -- .---- ..--- ...-- # # # # -.-.-- .--.-. # ...-..- # # .-... # -.--. -.--.- ..--.- .-.-. #'

        result = morse_code.encrypt(given_text)

        self.assertEqual(expected_encrypt, result)

    def test_decrypt_slash_to_space(self):
        """Decrypt - slash symbol in encrypted text should be translated to space"""
        given_text = "-- --- .-. ... . / .. ... / ..- ... . ..-. ..- .-.. .-.."
        expected_decrypt = "morse is usefull".upper()

        result = morse_code.decrypt(given_text)

        self.assertEqual(expected_decrypt, result)

    def test_decrypt_not_founded_code_should_return_original_text(self):
        """Decrypt - Every not founded code should return original text"""
        given_text = ".... .. -.. -.. . -. ------"
        expected_decrypt = "HIDDEN------"

        result = morse_code.decrypt(given_text)

        self.assertEqual(expected_decrypt, result)

    def test_encrypt_space_after_encrypted_characters(self):
        """Every encrypted character except last one should have space to identify how to decode this string"""
        given_text = "MorseCodeIsCool"
        expected_spaces = len(given_text) - 1

        result = morse_code.encrypt(given_text)
        print(result)
        count_spaces = result.count(' ')

        self.assertEqual(expected_spaces, count_spaces)


if __name__ == "__main__":
    unittest.main()
