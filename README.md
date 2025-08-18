# Any_chord_trainer
A tiny, dependency-light Python script that fires endless random chords at you for recognition training
# 🎹 Chord Trainer

A tiny, dependency-light Python script that fires endless random chords at you, waits for you to guess the notes on your instrument, and then reveals the correct answer.  
Perfect for drilling jazz chords, classical harmony, or just getting faster at reading chord symbols.

---

## ✨ Features

- **Random chord generation**  
  Major, minor, diminished, augmented, sus2/4, 6, 7, maj7, m7, m(maj7), dim7, 9, 11, 13, plus `modification`, `extention` and `omissions` options.

- **Two readability modes**  
  - *Easy mode* – symbols are split with pipes, e.g. `Cmaj7|add9|no5`.  
  - *Pro mode* – compact symbols, e.g. `Cmaj7add9no5`.

- **Flexible tonality system**  
  - “Baby mode” locks everything to **C** so you can focus on chord qualities.  
  - Full mode randomly chooses from 21 tonalities (sharps, flats, and enharmonic mixes).

- **Water reminder** *(optional)*  
  A background thread that GENTLY nags you to drink water every 20 minutes so you stay hydrated while practicing.  
  ➜ Disable by commenting out the two `wp.water_timer` lines.

- **No external dependencies**  
  Uses only the Python standard library.

---

## 🚀 Quick Start

1. Clone or download this repo.
2. Open a terminal in the project folder.
3. Run:

```bash
python chord_trainer.py
```
---
## ⚒ Modding
Currently, *getachord* function, the main function of the code takes in 6 variables:

| Flag                 | Type | Default | Meaning                                |
| -------------------- | ---- | ------- | -------------------------------------- |
| `number_of_chords`   | int  | 1       | How many chords to generate at once    |
| `no_modification`    | bool | False   | Disable 9/11/13 modifications          |
| `no_extention`       | bool | False   | Disable add9 / add11 / add13           |
| `no_omissions`       | bool | False   | Disable `no3`, `no5`, `no7`, `no9`     |
| `easy_tonality_mode` | bool | False   | Lock tonality to C                     |
| `easy_reading_mode`  | bool | False   | Use or don't use pipe-separated symbols for clarity |

If you want to, you could also start modding and pulling this function:

```python
from chord_trainer import getachord
getachord(number_of_chords=1, no_modification=False, no_extention=False, no_omissions=False, easy_tonality_mode=False, easy_reading_mode=False)
```
---
## 🕹 example session:

--------------------------------------------------
Welcome to the chord trainer!
--------------------------------------------------
Ready to go? (y or n): y
Chosen tonality this time: A (only influences the annotation, not the chord).
Let's play a: F#m9|add13|no5
Input anything to see the answer
you should play the following notes: ['F#', 'A', 'E', 'G#', 'D#']
--------------------------------------------------
Again? (y or n):
---
