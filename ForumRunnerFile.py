from PersonFile import Person
from InterceptorFile import Interceptor

class ForumRunner():

    def __init__(self):

        self.person_1 = Person()
        self.person_2 = Person()
        self.villain = Interceptor()

        self.person_1.request_name()
        self.person_2.request_name()

        print(f"We're going to try to have communications from {self.person_1.name} to {self.person_2.name}.")

    def share_public_private_info(self):
        print(f"FR: {self.person_2.name}, {self.person_1.name} would like to send you messages. What is your public "
              f"key for encoding?")
        self.person_2.select_tools_to_talk_to_me()
        # self.person_2.test_encrypt_decrypt()  # uncomment to test previous step worked, but don't keep this.
        key_to_talk_to_2 = self.person_2.get_public_key_info()
        print(f"{self.person_2.name}: {key_to_talk_to_2}")
        print(f"FR: {self.person_2.name}'s n is {key_to_talk_to_2[0]} and e is {key_to_talk_to_2[1]}. Villain, here's "
              f"that same info.")
        self.person_1.receive_friends_public_key_info(key_to_talk_to_2[0], key_to_talk_to_2[1])
        self.villain.intercept_n_and_e(key_to_talk_to_2[0], key_to_talk_to_2[1])
        print(f"{self.person_1.name}: Got it!")
        print("V: (Twisting mustache) Got it.")

    def try_sending_message(self) -> str:
        print("-"*40)
        message = input(f"{self.person_1.name}, what message do you want to send to {self.person_2.name}? (Please "
                        f"include at least one (polite) four-letter word.) ")
        encoded_message = self.person_1.encode_message(message)
        print(f"{self.person_1.name}: \"{encoded_message}\"")
        decoded = self.person_2.decode_message(encoded_message)
        print(f"{self.person_2.name}: (To self): {self.person_1.name} just said \"{decoded}\".")

        return encoded_message


    def attempt_brute_force(self, encoded):
        options_list = fr.villain.brute_force_decrypt(encoded)
        if len(options_list) == 0:
            print("No decryption found.")
        elif len(options_list) > 20:
            print(f"Way too many ({len(options_list)}) options for decryption found to list.")
        elif len(options_list) == 1:
            print(f"Villain has intercepted \"{options_list[0]}\".")
        else:
            print("Villain has found several options:")
            for option in options_list:
                print(f"\t{option}")


if __name__ == "__main__":
    fr = ForumRunner()
    fr.share_public_private_info()
    while True:
        encoded = fr.try_sending_message()
        # fr.attempt_brute_force(encoded)
