#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
generate harmonics for LSP Parametric Equalizer
https://lsp-plug.in/?page=manuals&section=para_equalizer_x16_stereo
"""

from argparse import ArgumentParser, ArgumentTypeError
import re
import notes

HARM_NUM = 6
EQ_GAIN = 2.0
EQ_Q = 16

def t_note(value):
    """
    parse note str, return tuple (note, octave, frequency)
    """
    match = re.search(r'([A-Gb#]+)(\d+)', value)
    if match:
        note = match.group(1)
        octave = int(match.group(2))
        if note in notes.OCT0:
            f_freq = notes.OCT0[note]
        else:
            raise ArgumentTypeError("Invalid note name argument")
    else:
        raise ArgumentTypeError("Invalid note argument")

    return note, octave, f_freq * (octave + 1)

def __main__():
    argp = ArgumentParser()
    argp.add_argument("-n", dest="note", required=True, type=t_note,
                      help="Note, e.g. G1")
    argp.add_argument("--hn", dest="harm_num", type=int, default=HARM_NUM,
                      help="Number of harmonics (default: %(default)s)")
    argp.add_argument("--gain", dest="eq_gain", type=float, default=EQ_GAIN,
                      help="EQ gain (default: %(default)s)")
    argp.add_argument("--eqq", dest="eq_q", type=float, default=EQ_Q,
                      help="EQ Q (default: %(default)s)")
    argp.add_argument("-f", action='store_true', dest="only_freq",
                      help="Print only frequency")
    args = argp.parse_args()
    note, octave, freq = args.note
    print(f'# {note}{octave}, frequency: {freq}')
    nth_harmonic = 1
    for i in range(-1, args.harm_num + 1):
        if i >= 0:
            c_freq = freq * (i + 1)
        else:
            c_freq = freq / (abs(i) + 1)
        if args.only_freq:
            harmonic_part = f'{nth_harmonic:3}' if c_freq >= freq else ''
            print(f'{c_freq:>22.14f}{harmonic_part}')
            if c_freq >= freq:
                nth_harmonic += 1
        else:
            print(f'f_{i+1} = {c_freq}')
            c_q = 5.0
            c_fm = 0
            if c_freq == freq:
                gain = 0
                filt = 8
                c_q = 0
                slope = 0
            elif c_freq < freq:
                gain = 0.0
                filt = 2
                c_q = 0.0
                slope = 1
                c_fm = 4
            else:
                gain = args.eq_gain
                filt = 1
                c_q = args.eq_q
                slope = 0
            print(f'g_{i+1} = {gain} db')
            print(f'ft_{i+1} = {filt}')
            print(f'q_{i+1} = {c_q}')
            print(f's_{i+1} = {slope}')
            print(f'fm_{i+1} = {c_fm}')

if __name__ == '__main__':
    __main__()
