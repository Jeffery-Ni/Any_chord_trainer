# Any_chord_trainer
A tiny, dependency-light Python script that fires endless random chords at you for recognition training

# 🎹 Chord Recognition Trainer
A tiny, dependency-light Python script that fires endless random chords at you, waits for you to guess the notes of the chord (preferably training with a piano), and then reveals the correct answer.  
Perfect for drilling jazz chords, classical harmony, or just getting faster at reading chord symbols.

## ✨ Features

- **Random chord generation**  
  Major, minor, diminished, augmented, sus2/4, 6, 7, maj7, m7, m(maj7), dim7, 9, 11, 13, plus `modification`, `extention` and `omissions` options.

- **Two readability modes**  
  - *Easy mode* – symbols are split with pipes, e.g. `Cmaj7|add9|no5`.  
  - *Gibberish mode* – compact symbols, e.g. `Cmaj7add9no5` (I don't know how to output corner mark in command lines so good luck reading this).

- **Flexible tonality system**  
  - “Baby mode” locks everything to **C** so you can focus on chord qualities.  
  - Full mode randomly chooses from 21 tonality signs (sharps, flats, and mixed-sign ones).

- **Water reminder** *(optional)*  
  A background thread that GENTLY nags you to drink water every 20 minutes so you stay hydrated while practicing.  
  ➜ Disable by commenting out the two `wp.water_timer` lines.

- **Light external dependencies**  
  Uses only the Python standard library.
  ➜ The only additional module is `sounddevice` from `play_chord_test.py`, if play_the_chord option is false, you don't need any additional dependency
- **🎧 You can play the chord to see if you are right!! 🎧** *(optional)*  
  As stated above, this functions needs additionsl package

## 🚀 Quick Start

1. Clone or download this repo.
2. Open a terminal in the project folder.
3. Run:

```bash
python chord_trainer.py
```
## ⚒ Options and Modding
Currently, *getachord()* function, the main function of the code takes in 6 variables:

| Flag                 | Type | Default | Meaning                                |
| -------------------- | ---- | ------- | -------------------------------------- |
| `number_of_chords`   | int  | 1       | How many chords to generate at once    |
| `no_modification`    | bool | False   | Disable 9/11/13 modifications          |
| `no_extention`       | bool | False   | Disable add9 / add11 / add13           |
| `no_omissions`       | bool | False   | Disable `no3`, `no5`, `no7`, `no9`     |
| `easy_tonality_mode` | bool | False   | Lock tonality and chosen note to C    |
| `easy_reading_mode`  | bool | False   | Use or don't use pipe-separated symbols for clarity |
| 🎧🎧`play_the_chord`  | bool | False   | * This one uses additional module called "sounddevice" from play_chord_test.py |

*I actually forgot whats the default, I guess you can change it to whatever you need*

If the training is too hard for you with all of these options, turn some of them off with "True" to that variable
If you want to, you could also start modding and pulling this function:

```python
from chord_trainer import getachord
getachord(number_of_chords=1, no_modification=False, no_extention=False, no_omissions=False, easy_tonality_mode=False, easy_reading_mode=False, play_the_chord=False)

```
## 🕹 Example Session:
```text
--------------------------------------------------------------------------------------------------------------------------------------------
Welcome to the chord trainer!
This program will help you practice identifying and playing various chords.
You will be prompted to play a chord, and then the program will reveal the notes in that chord.
Let's get started!
--------------------------------------------------------------------------------------------------------------------------------------------
Ready to go? (y or n), if you don't say anything i'll continue: y
Chosen tonality this time: G (only influences the annotation, not the chord).
I'm feeling like a: F#m
Input anything to see the answer
you should play the following notes: ['F#', 'A', 'C#']
--------------------------------------------------------------------------------------------------------------------------------------------
Again? (y or n), if you don't say anything i'll continue: y
Chosen tonality this time: B (only influences the annotation, not the chord).
How about a: Fm(M9)11no5
Input anything to see the answer
you should play the following notes: ['F', 'G#', 'E', 'G', 'A#']
--------------------------------------------------------------------------------------------------------------------------------------------
Again? (y or n), if you don't say anything i'll continue: n
Fine, I'll go >:(
```
## 🤝 Contributing
Pull requests welcome!
Ideas: MIDI output, GUI, statistics tracking, or more chord symbols.

## 📜 Lisence
Published under GPL v3.0 lisence
