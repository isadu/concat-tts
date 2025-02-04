from pydub import AudioSegment
import re
from pathlib import Path
# lives inside libav.../win64/usr for import/path problems

"""Pauses"""
quarter_rest = AudioSegment.silent(duration=0)
half_rest = AudioSegment.silent(duration=150)
whole_rest = AudioSegment.silent(duration=1000)

"""Natural classes"""
liquids = {'L', 'R'}
nasals = {'M', 'N', 'NG'}
voiceless_stops = {'P', 'T', 'K'}

class Concater:
    def __init__(self, dict_file):
        """Build the pronouncing dictionary"""
        dict_text = open(dict_file, mode='r')
        self.dictionary = {}
        self.dictionary.update({'take':'test'})
        for line in dict_text:
            if line.startswith(';'):
                continue
            split = line.split('\t')
            if len(split) < 2:
                continue
            self.dictionary.update({split[0]:split[1]})
            
    def add_to_dictionary(self, word):
        """Add an unknown word to the dictionary for this session"""
        print(word + " not found in dictionary. Enter pronunciation:\n")
        pronunciation = input()
        if pronunciation == "":
            return False
        if not self.is_valid(pronunciation):
            print("Invalid pronunciation. Try again or press enter to quit.")
            return self.add_to_dictionary(word)
        self.dictionary.update({word.upper():pronunciation})
        return True

    def is_valid(self, pronunciation):
        """Check whether the provided string is a sequence of available sounds"""
        if pronunciation == "" or not pronunciation.isalnum():
            return False
        phones = pronunciation.split()
        if all(map(self.is_sound, phones)):
            return True
        else:
            return False

    def is_sound(self, phone):
        """Check whether the provided string is an available sound"""
        file = Path("recARPAs/" + phone + ".wav")
        return file.is_file()            

    def is_vowel(self, phone):
        """Check whether phone is a vowel - all vowels have numerical stress marking"""
        return not phone.isalpha()
            
    def get_sound(self, phone):
        """Get the sound file for a phone"""
        filename = "recARPAs/" + phone + ".wav"
        return AudioSegment.from_file(filename, format="wav") # TODO handle failure

    def word_to_speech(self, word):
        """Return new audio segment with sound version of each letter in given word"""
        song = []
        word = word.upper()
        if word not in self.dictionary:
            if not self.add_to_dictionary(word):
                print("Missing dictionary entry. Could not finish.")
                return quarter_rest
        pronunciation = self.dictionary[word].split()
        print(pronunciation)
        index = 0
        while index < len(pronunciation):
            phones = ''
            phones += pronunciation[index]
            if phones == '':
                print("rest")
                song.append(quarter_rest)
                break
            if not self.is_sound(phones):
                print("not sound")
                break
            while index+1 < len(pronunciation) and \
                  self.is_sound(phones + pronunciation[index+1]):
                print("adding")
                phones += pronunciation[index+1]
                index += 1
            print(phones)
            song.append(self.get_sound(phones))
            index += 1
        song.append(half_rest)
        return sum(song)

def main():
    """Create and save sound file for input"""
    concater = Concater("cmudict2.txt")
    inp = input()
    while (inp != ''):
        sentence = []
        sentence.append(half_rest)
        for token in inp.split():
            word = concater.word_to_speech(token)
            sentence.append(word)
        sentence.append(whole_rest)
        sum(sentence).export("concated02 " + inp + ".mp3", format="mp3")
        inp = input()

if __name__ == '__main__':
    main()
