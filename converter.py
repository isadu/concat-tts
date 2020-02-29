from pydub import AudioSegment
"""
Convert all hardcoded letters to mp3
TODO: iterate through directory files
"""

def m4a_to_mp3(filename):
    audio = AudioSegment.from_file(filename + ".m4a", format="m4a")
    audio.export(filename + ".mp3", format="mp3")

def main():
    directory = input()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in alphabet:
        m4a_to_mp3(directory + "/" + letter)

if __name__ == '__main__':
    main()
