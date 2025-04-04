import math
import random
from typing import Tuple, Optional


def pick_prime_in_range(lowest: int, highest: int) -> int:
    """
    selects a prime number at random from the range lowest (inclusive) to highest (exclusive).
    :param lowest: the start of the range
    :param highest: one past the end of the range
    :return: a prime number selected from the range.
    """
    while True:
        n = random.randint(lowest, highest)
        is_prime = True
        # TODO: determine whether n is a prime number, and set is_prime to True or False, accordingly.

        if is_prime:
            return n


def gcd(a: int, b: int) -> int:
    """
    finds the greatest common divisor of a and b.
    :param a: a positive integer
    :param b: a positive integer
    :return: the largest integer that divides evenly into both a and b.
    """
    gcd, x, y = gcd_extended(a, b)
    return gcd


def lcm(a: int, b: int) -> int:
    """
    finds the lowest common multiplier of a and b.
    :param a: a positive integer
    :param b: a positive integer
    :return: the smallest integer into which both a and b divide evenly.
    """
    return a // gcd(a, b) * b

def gcd_extended(a: int, b: int) -> Tuple[int, int, int]:
    """
    Uses Euler's method to recursively find the greatest common divisor of a and b, and produces some extra information
    needed for the modular multiplicative inverse as a side product.
    :param a: a positive integer
    :param b: a positive integer
    :return: the largest integer that divides evenly into both a and b, as well as "x" and "y"
    """

    if (a == 0):
        return (b, 0, 1)
    gcd, x1, y1 = gcd_extended(b % a, a)

    x = y1 - (b // a) * x1
    y = x1

    return (gcd, x, y)


def mod_mult_inverse(a: int, m: int) -> int:
    """"
    calculates the modular multiplicative inverse of a mod m.
    """
    g, x, y = gcd_extended(a, m)
    if g != 1:
        raise Exception("Inverse doesn't exist.")
    return (x % m + m) % m


class Person:

    def __init__(self):
        self.my_public_n = 1
        self.my_public_e = 0
        self.__my_private_d__ = 0

        self.name = ""

        self.my_friends_e = 0
        self.my_friends_n = 0

    def request_name(self) -> None:
        self.name = input("Creating a new person: Hello, what is your name?")
        print(f"Welcome, {self.name}")

    def get_public_key_info(self) -> Tuple[int, int]:
        """
        returns the public n and e, calculated previously, that can be used for others to encrypt messages to me.
        :return: my public n & e values that compose my public key.
        """
        return (self.my_public_n, self.my_public_e)

    def receive_friends_public_key_info(self, n: int, e: int) -> None:
        """
        basically a "setter" for the friend's key info, so we can encode messages to him/her.
        :param n:  the public modulus value from the friend
        :param e: the encoding exponent from the friend
        :return: None
        """
        self.my_friends_n = n
        self.my_friends_e = e

    def select_tools_to_talk_to_me(self) -> None:
        """
        Generate the encryption/decryption tools for somebody to send me messages that I can read.
        You should update self.my_public_n, self.my_public_e, and self.__my_private_d__.
        :return: None
        """
        # TODO: You write this! I've put some suggested steps below that correspond to the steps in the instructions.

        # 1) select p and q with the pick_prime_in_range() method from the top of this file. At first, please pick
        # values that will give you an n in the range of 260 - 500.


        # 2) calculate self.my_public_n.


        # 3) calculate phi. This will make use of the lcm() method from the top of this file.
        phi = -1  # change this!!!!!!!

        # 4) select a value for self.my_public_e that is less than phi and mutually prime with phi. This may involve
        #   picking a value for e but you might need to do this more than once to find one that works.
        self.my_public_e = -1  # change this!!!!

        # 5) I've written this for you to find self.__my_private_d__. Note the dunders (double underscores) mean this
        # should be private.
        self.__my_private_d__ = mod_mult_inverse(self.my_public_e, phi)

    def test_encrypt_decrypt(self) -> None:
        """
        runs through 0-255 and confirms that each of these values is encrypted, but decryption restores the original
        value.
        :return: None
        """
        print("If select_tools_to_talk_to_me is working properly, first and last column should match.")
        print("i\t\tencrypted\tdecrypted")
        for i in range(0, 255):
            c = (i ** self.my_public_e) % self.my_public_n
            z = (c ** self.__my_private_d__) % self.my_public_n
            print(f"{i}\t\t{c}\t\t{z}")

    def encode_message(self, m: str) -> str:
        """
        turns a plaintext string into an encrypted version of the message, using your friend's n & e.
        :param m: the message to encrypt
        :return: the encrypted version of the message
        """
        encoded = ""
        # TODO: you write this. Loop through each letter in string "m" and build an output (encrypted) string.
        # note, to turn a character into its ASCII/unicode number, say x = ord(letter)
        #       to turn a ASCII/unicode number into a character, say c = chr(x)

        for letter in m:
            encoded += "👾"  # Change this!!!!!

        return encoded

    def decode_message(self, c: str, d: Optional[int] = None) -> str:
        """
        turns an encoded string back into a plaintext version of the message, using your own n & d.
        :param c: the message to dencrypt
        :param d: the decoding key to use, or None if you wish to use this instance's own private d.
        :return: the dencrypted version of the message
        """
        if d is None:
            d = self.__my_private_d__
        decoded = ""

        # TODO: you write this. Use "d" rather than self.__my_private_d__ for better flexibility.
        for letter in m:
            decoded += "💩"  # Change this!!!!!
        return decoded

