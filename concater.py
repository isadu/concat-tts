from pydub import AudioSegment
import re
# lives inside libav.../win64/usr for import/path problems

quarter_rest = AudioSegment.silent(duration=150)
half_rest = AudioSegment.silent(duration=300)

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
        if pronunciation == '': # TODO: more validation
            return False
        self.dictionary.update({word.upper():pronunciation})
        return True
            
    def get_sound(self, phone):
        """Get the sound file for a letter (/single char code)"""
        phone = re.sub(r'[0-9]', "", phone)
        filename = "recARPAs/" + phone + ".wav"
        return AudioSegment.from_file(filename, format="wav")

    def word2song(self, word):
        """Return new audio segment with sound version of each letter in given word"""
        song = []
        word = word.upper()
        if word not in self.dictionary:
            if not self.add_to_dictionary(word):
                print("Missing dictionary entry. Could not finish.")
                return sum(song)
        pronunciation = self.dictionary[word]
        for phone in pronunciation.split():
            if (phone == ''):
                song.append(quarter_rest)
                continue
            if (not phone.isalnum()):
                continue
            song.append(self.get_sound(phone))
        song.append(half_rest)
        return sum(song)

def main():
    """Create and save sound file for input"""
    concater = Concater("cmudict2.txt")
    inp = input()
    while (inp != ''):
        sentence = []
        sentence.append(half_rest)
        for word in inp.split():
            song = concater.word2song(word)
            sentence.append(song)
        sum(sentence).export("songfor" + inp + ".mp3", format="mp3")
        inp = input()

if __name__ == '__main__':
    main()
