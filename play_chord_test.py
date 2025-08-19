import sounddevice as sd 
import numpy as np

SHARP_TO_FLAT = {
    "C#": "Db",
    "D#": "Eb",
    "F#": "Gb",
    "G#": "Ab",
    "A#": "Bb",
}
# ---------- helper functions ----------
NOTE_NAMES = ["C", "DB", "D", "EB", "E", "F",
              "GB", "G", "AB", "A", "BB", "B"]

def normalize_note(n):          # unifies expressions like "C#" and "Db"
    name = n[:-1].upper()
    octv = n[-1]
    return (SHARP_TO_FLAT.get(name, name) + octv)

# def normalize_note(n):
#     n = n.upper()
#     oct_idx = next(i for i, ch in enumerate(n) if ch.isdigit())
#     name = n[:oct_idx]          
#     octv = n[oct_idx:]
#     name = SHARP_TO_FLAT.get(name, name)
#     return name[0] + octv    


def note_to_freq(note):
    name = normalize_note(note)
    pitch = name[:-1].upper()
    octv = int(name[-1])
    semitone = NOTE_NAMES.index(pitch)
    n = 12 * (octv - 4) + semitone - 9
    return 440.0 * (2 ** (1/12)) ** n

def make_sine(f, duration=0.25, sr=44100, amp=0.3):
    t = np.linspace(0, duration, int(sr*duration), False)
    return amp * np.sin(2*np.pi*f*t)

# ---------- arpeggio and then chord ----------
def play_arpeggio_then_chord(notes, arp_duration=0.25, chord_duration=1.0,
                             sample_rate=44100):
    notes = sorted(notes, key=note_to_freq)
    freqs = [note_to_freq(n) for n in notes]

    # arp
    arp_parts = [make_sine(f, arp_duration, sr=sample_rate) for f in freqs]
    arp_wave = np.concatenate(arp_parts)

    # chord
    chord_wave = sum(make_sine(f, chord_duration, sr=sample_rate) for f in freqs)
    chord_wave = np.clip(chord_wave, -1, 1)

    # put together
    full_wave = np.concatenate([arp_wave, chord_wave])
    sd.play(full_wave, samplerate=sample_rate)
    sd.wait()  

# ---------- example ----------
if __name__ == "__main__":
    _keep = play_arpeggio_then_chord( ['C4', 'E4', 'G4', 'B5', 'D5', 'F5', 'A5'])
    # _keep variable keeps PlayObject from getting garbage collected
    # This is a workaround for the issue where the sound stops playing immediately or stops immediately after the function returns.
    input("debug fake input: ")
