# Any_chord_trainer
A tiny, dependency-light Python script that fires endless random chords at you for recognition training
# 🎹 Chord Trainer

A tiny, dependency-light Python script that fires endless random chords at you, waits for you to guess the notes on your instrument, and then reveals the correct answer.  
Perfect for drilling jazz chords, classical harmony, or just getting faster at reading chord symbols.

---

## ✨ Features

- **Random chord generation**  
  Major, minor, diminished, augmented, sus2/4, 6, 7, maj7, m7, m(maj7), dim7, 9, 11, 13, plus `add` and `omit` options.

- **Two readability modes**  
  - *Easy mode* – symbols are split with pipes, e.g. `Cmaj7|add9|no5`.  
  - *Pro mode* – compact symbols, e.g. `Cmaj7add9no5`.

- **Flexible tonality system**  
  - “Baby mode” locks everything to **C** so you can focus on chord qualities.  
  - Full mode randomly chooses from 21 tonalities (sharps, flats, and enharmonic mixes).

- **Water reminder** *(optional)*  
  A background thread that gently nags you to drink water every 30 minutes so you stay hydrated while practicing.  
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
