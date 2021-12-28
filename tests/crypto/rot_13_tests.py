"""
Rot 13 cryptography module tests.
"""

import unittest
import sys

sys.path.append('../../modules/crypto/')
import rot_13_crypto


class Rot13TestCase(unittest.TestCase):

    def test_rot13_decrypt_should_move_characters(self):
        """Decrypt method should move given characters 13 positions (should work with both directions)"""
        given_text = "abcdefghijklm"
        expected = "nopqrstuvwxyz"

        act = rot_13_crypto.decrypt(given_text)

        self.assertEqual(act, expected)

    def test_rot13_decrypt_should_work_for_upper_and_lower_chars(self):
        """Decrypt method for given lowercase should return letter in lower,
           in upper cases returned char should be in uppercase"""
        given_text = "lOwErAnDuPpEr"
        expected = 'yBjReNaQhCcRe'

        act = rot_13_crypto.decrypt(given_text)

        self.assertEqual(act, expected)

    def test_rot13_decrypt_same_value_for_non_alphabetic_characters(self):
        """Decrypt method should return same character if given char is not alphabetic
           for example: 1 should stay 1, _ should stay _ etc.
           Only letters from [a-zA-Z] should be transformed.
        """
        given_text = "S0m3_Ch@r@ct3r$_$h0uld_B3_s@m3"
        expected = "F0z3_Pu@e@pg3e$_$u0hyq_O3_f@z3"

        act = rot_13_crypto.decrypt(given_text)

        self.assertEqual(act, expected)

    def test_rot13_decrypt_contains_spaces(self):
        """Decrypt method should leave not changed space character if text contains spaces"""
        given_text = "qrpelcgrq grkg jvgu fcnprf"
        expected = "decrypted text with spaces"

        act = rot_13_crypto.decrypt(given_text)

        self.assertEqual(act, expected)

    def test_rot13_encrypt_should_move_characters(self):
        """Encrypt method should move given characters 13 positions (should work with both directions)"""
        given_text = "nopqrstuvwxyz"
        expected = "abcdefghijklm"

        act = rot_13_crypto.encrypt(given_text)

        self.assertEqual(act, expected)

    def test_rot13_encrypt_should_work_for_upper_and_lower_chars(self):
        """Encrypt method for given lowercase should return letter in lower,
           in upper cases returned char should be in uppercase"""
        given_text = 'yBjReNaQhCcRe'
        expected = "lOwErAnDuPpEr"

        act = rot_13_crypto.encrypt(given_text)

        self.assertEqual(act, expected)

    def test_rot13_encrypt_same_value_for_non_alphabetic_characters(self):
        """Encrypt method should return same character if given char is not alphabetic
           for example: 1 should stay 1, _ should stay _ etc.
           Only letters from [a-zA-Z] should be transformed.
        """
        given_text = "F0z3_Pu@e@pg3e$_$u0hyq_O3_f@z3"
        expected = "S0m3_Ch@r@ct3r$_$h0uld_B3_s@m3"

        act = rot_13_crypto.encrypt(given_text)

        self.assertEqual(act, expected)

    def test_rot13_encrypt_contains_spaces(self):
        """Encrypt method should leave not changed space character if text contains spaces"""
        given_text = "decrypted text with spaces"
        expected = "qrpelcgrq grkg jvgu fcnprf"

        act = rot_13_crypto.encrypt(given_text)

        self.assertEqual(act, expected)


if __name__ == "__main__":
    unittest.main()
