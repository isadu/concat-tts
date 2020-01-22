from pydub import AudioSegment

def build_alphabet(source_file, file_type):
    full_song = AudioSegment.from_file(source_file, file_type)
    alphabet = []
    for start in range(1000,26000,1000):
        alphabet.append(full_song[start:start+1000])
    return alphabet

def word2song(alphabet, word):
    song = []
    for letter in word:
        song.append(alphabet[ord(letter)-ord('a')])
    return sum(song)

def main():
    word = input()
    if (word == ''):
        print("no word")
        return
    alphabet = build_alphabet("thirdpass.m4a", "m4a")
    song = word2song(alphabet, word)
    song.export("songfor" + word + ".mp3", format="mp3")

if __name__ == '__main__':
    main()
