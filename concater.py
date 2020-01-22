from pydub import AudioSegment

def build_alphabet(source_file, file_type):
    """Build an alphabet of clips from a given source file"""
    full_song = AudioSegment.from_file(source_file, file_type)
    alphabet = []
    for start in range(1000,26000,1000):
        alphabet.append(full_song[start:start+1000])
    return alphabet

# TODO: alphabet from individual/non-fixed length clips

def word2song(alphabet, word):
    """Return new audio segment with sound version of each letter in given word"""
    song = []
    for letter in word:
        song.append(alphabet[ord(letter)-ord('a')])
    return sum(song)

def main():
    """Create and save sound file for input"""
    word = input()
    # TODO: account for non a-z input
    if (word == ''):
        print("no word")
        return
    source_file = "thirdpass.m4a"
    alphabet = build_alphabet(source_file, source_file[-3:])
    song = word2song(alphabet, word)
    song.export("songfor" + word + ".mp3", format="mp3")

if __name__ == '__main__':
    main()
