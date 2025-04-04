from typing import List, Tuple

import PersonFile

class Interceptor(PersonFile.Person):

    def __init__(self):
        super().__init__()
        self.name = "Villain"
        self.possible_decryption_keys: List[int] = []
        self.targets_public_n = 0
        self.targets_public_e = 0
        self.word_list: List[str] = []
        self.load_words_from_file("Four letter words.txt")

    def load_words_from_file(self, word_filename: str):
        """
        loads the self.word_list with all the words in the given file.
        :param word_filename: the file to read in a format "word# <tab> word"
        :return: None
        """
        print(f"**** Loading Words from {word_filename}.")
        count = 0
        with open(word_filename, 'r') as ins:
            for line in ins:
                pairs = line.split(
                    "\t")  # make a 2-item list with the part before the tab and the part after the tab.
                # if count % 100 == 0:  # show progress....
                #     print(f"Loaded {count} words....")

                count += 1
                self.word_list.append(
                    pairs[1].split("\n")[0])  # The split{"\n") part gets rid of the carriage return.
        print(f"**** Done Loading {len(self.word_list)} words from file {word_filename}.")
        print("-------------------------------------------")

    def intercept_n_and_e(self, n:int, e:int) -> None:
        self.targets_public_n = n
        self.targets_public_e = e

    def count_four_letter_words_in_string(self, sentence: str) -> int:
        """
        loops through the string, selecting four-character sequences and counts how many are contained in
        self.word_list.
        :param sentence: the string in which to search for words
        :return: the count of matching four-letter words.
        """
        return -1  # TODO: write this method!

    def brute_force_decrypt(self, c: str) -> List[str]:
        """
        receives an intercepted string that was encoded with self.targets_public_n and self.targets_public_e. Attempts
        to decrypt this string by brute force trying different decryption keys.
        :param c: the encrypted string to try to hack
        :return: a list of decrypted strings that contained one or more four-letter words. That is, a list of strings
        that might be successfully decrypted.
        """
        # This is a method that might get called multiple times.
        # If this is the first time (i.e., if self.possible_decryption_keys is empty, then loop through all the
        # decryption keys (d) between 3 and the target's intercepted n value. Try decrypting the string and see whether
        # any of the decryptions contain one or more real four-letter words. If so, add that decryption key to
        # self.possible_decryption_keys and add the decrypted string to the list of possibilities to return.

        # If this is a later pass, then we either have a winner, or we need to refine our search:
        #    If there is only one value here, then just return the list with a single decrypted string,
        #    But if there are several possible d values, try each one. If one or more do have four-letter words, remove
        #    the d's that didn't do well, keep the d's that did, and return the candidate decryptions. If none had any
        #    four-letter words, it's possible that there weren't any to find, so keep all the d's and return all the
        #    decrypted strings.

        if len(self.possible_decryption_keys) == 0:
            pass
            # TODO: loop through all values of d between 3 and target's intercepted n value.
            #     try decrypting c with each d, and check whether each result has any real four-letter words.
            #     If so, add d to the list of possibilities and add this decrypted message into the list to return.

            # note: Interceptor is a subclass of Person, so you already have access to decode_message(c, d).

        elif len(self.possible_decryption_keys) == 1:
            pass
            # TODO: decrypt the given message using the one value of d in self.possible_decryption_keys and put this
            #    sole decrypted message as the only item in the list to return.

        else:
            pass
            # TODO: for each possible d value, decrypt the message using that d and count how many real four-letter
            #     words there are in it.
            #     If none have any, add all the decrypted messages into the list to return.
            #     If one or more have some four letter words, put those messages into the list to return, and remove any
            #        of the d's that corresponded to zero words from the list of possibilities.

