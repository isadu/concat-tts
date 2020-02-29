from pydub import AudioSegment
# lives inside libav.../win64/usr for import/path problems
# non-IPA-behaving characters:
# 1=ai 2=ei 3=schwa 4=I 5=wedge 8=sh 9=th c=tsh j=dzh y=j

quarter_rest = AudioSegment.silent(duration=150)
half_rest = AudioSegment.silent(duration=300)

def get_sound(letter):
    """Get the sound file for a letter (/single char code)"""
    filename = "recs/" + letter + ".wav"
    return AudioSegment.from_file(filename, format="wav")

def word2song(word):
    """Return new audio segment with sound version of each letter in given word"""
    song = []
    song.append(half_rest)
    for letter in word:
        if (letter == ' '):
            song.append(quarter_rest)
            continue
        if (not letter.isalnum()):
            continue
        song.append(get_sound(letter))
    song.append(half_rest)
    return sum(song)

def main():
    """Create and save sound file for input"""
    word = input()
    if (word == ''):
        print("no word")
        return
    song = word2song(word)
    song.export("songfor" + word + ".mp3", format="mp3")

if __name__ == '__main__':
    main()
