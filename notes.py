#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" notes, frequency """


def freq_of_note(note_number, octave_number=0):
    """ compute note frequency """
    return 440 * 2 ** ((note_number - 9 + 12 * (octave_number - 4)) / 12)

NOTES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

NOTE_MAP = {
    'C': 0, 'C#': 1, 'Db': 1, 'D': 2, 'Eb': 3, 'D#': 3, 'Fb': 4, 'E': 4,
    'F': 5, 'E#': 5, 'Gb': 6, 'F#': 6, 'G': 7, 'Ab': 8, 'G#': 8, 'A': 9,
    'Bb': 10, 'A#': 10, 'B': 11
}

OCT0 = {note: freq_of_note(note_number) for note, note_number in NOTE_MAP.items()}

def __main__():
    midi_n = 12
    for octave in range(6):
        for note in range(12):
            freq = freq_of_note(note, octave)
            s_note = f'{NOTES[note]}{octave}'
            print(f'{s_note:5}{freq:>8.3f}{midi_n:>5}')
            midi_n += 1

if __name__ == '__main__':
    __main__()
