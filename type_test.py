from wonderwords import RandomSentence
import time

class TypeTest():
    def __init__(self, length=3) -> None:
        self.sentences_list = []
        self.paragraph = ""
        for i in range(length):
            sentence = RandomSentence()
            random_sentence = sentence.sentence()
            self.sentences_list.append(random_sentence)
            self.paragraph += random_sentence + " "

    def execute_test(self):
        print("Type the below paragraph as quickly as possible\n")
        print("When finished, press enter key.")
        print(self.paragraph)
        print("\n")

        start_time = time.time()
        typed_para = input()
        end_time = time.time()

        time_taken = end_time - start_time

        speed = len(typed_para)/time_taken
        print("******YOUR SCORE REPORT******")
        print(f"Your speed is {speed} words/sec")
