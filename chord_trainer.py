import water_prompt as wp # This is a separate module that contains the water reminder functionality, TURN THIS OFF IF YOU DON'T WANT IT
import threading
t = threading.Thread(target=wp.water_timer, daemon=True)
t.start()


import random as rd
import shutil
width = shutil.get_terminal_size().columns


import play_chord_test as pct



def getachord(number_of_chords=1, no_modification=False, no_extention=False, no_omissions=True, easy_tonality_mode=True, easy_reading_mode=False, play_the_chord=True):
    sharp_sign_tonality = ['C', 'G', 'D', 'A', 'E','e','b','f#','c#']
    flat_sign_tonality = ['F', 'Bb', 'Eb', 'Ab','d','g','c','f']
    mixed_sign_tonality = ['g#','eb/d#','bb','Db', 'Gb/F#', 'B']
    notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    alternative_notes = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']

    
    notes_dictionary = {
    'C': 0,
    'C#': 1,
    'D': 2,
    'D#': 3,
    'E': 4,
    'F': 5,
    'F#': 6,
    'G': 7,
    'G#': 8,
    'A': 9,
    'A#': 10,
    'B': 11
            }
    
    alternative_notes_dictionary = {
    'C': 0,
    'Db': 1,
    'D': 2,
    'Eb': 3,
    'E': 4,
    'F': 5,
    'Gb': 6,
    'G': 7,
    'Ab': 8,
    'A': 9,
    'Bb': 10,
    'B': 11
}

    basic_quality_without_7th = {'': [1,5,8], 
                                 'm':[1,4,8], 
                                 'dim': [1,4,7], 
                                 'aug': [1,5,9],
                                 'sus2': [1,3,8],
                                 'sus4': [1,6,8]} # Major is ommited

    basic_quality_with6 = {'6' or 'M6' or 'maj6' or 'Δ6': [1,5,8,10], 
                            'm6' or 'min6' or '-6': [1,4,8,10]}

    basic_quality_with_7th = {'M7' or 'maj7' or 'Δ7': [1,5,8,12],
                              '7': [1,5,8,11], 
                              'm(M7)' or 'min(maj7)' or '-(Δ7)':[1,4,8,12], 
                              'm7' or 'min7' or '-7': [1,4,8,11], 
                              '∅7': [1,4,7,11],
                              'dim7' or '°7':[1,4,7,10],
                              'aug7' or '+7':[1,5,9,11]}
    
    basic_quality_with_9th = {'M9' or 'maj9' or 'Δ9':[1,5,8,12,15], 
                              '9':[1,5,8,11,15], 
                              'm(M9)' or 'min(maj9)' or '-(Δ9)':[1,4,8,12,15], 
                              'm9' or 'min9' or '-9':[1,4,8,11,15], 
                              '∅9':[1,4,7,11,15],
                              'dim9' or '°9': [1,4,7,10,15],
                              'aug9' or '+9': [1,5,9,11,15]} 



    modifications = {
                    ' 9':[12,15],
                    ' 11':[12,15,18], 
                    ' 13':[12,15,18,22],
                    '':[]} # 6th is not

    extensions = {
                  ' add9':[15],
                  ' add11': [18],
                  ' add13': [22],
                  '':[]}

    omittions = {
                 ' no9':[15],
                 ' no7':[12, 11],
                 ' no5':[8], 
                 ' no3':[5,4], 
                 '':[],
                 }

    UI_phrase = ["I want you to give me a", "How about a", "Try a", 
                 "Let's play a", "Can you give me a", "What do you think of a", 
                 "How about we play a", "I'm feeling like a", "Let's try a"]
    
    if not easy_tonality_mode:
        random_tonality = rd.choice(sharp_sign_tonality + flat_sign_tonality + mixed_sign_tonality)
    else:
        random_tonality = "C" # BABY MODE, AND TO DEBUG
    print(f"Chosen tonality this time: {random_tonality}"" (only influences the annotation, not the chord).")

    for _ in range(number_of_chords):
        if random_tonality in sharp_sign_tonality:
            random_note = rd.choice(notes)
        if random_tonality in flat_sign_tonality:
            random_note = rd.choice(alternative_notes)
        elif random_tonality in mixed_sign_tonality:
            random_note = rd.choice(notes + alternative_notes)

        if easy_tonality_mode:
            random_note = "C" # BABY MODE, AND TO DEBUG

        random_quality = rd.choice(list(basic_quality_without_7th.keys()) + list(basic_quality_with_7th.keys()) + list(basic_quality_with_9th.keys()) + list(basic_quality_with6.keys()))
        
        if random_quality in basic_quality_without_7th or random_quality in basic_quality_with6 or random_quality in basic_quality_with_7th:
            va=0
            vb=2
            candidates = [basic_quality_without_7th, basic_quality_with6, basic_quality_with_7th]
            target_dict = next(d for d in candidates if random_quality in d)
        if random_quality in basic_quality_with_9th:
            va=1
            vb=1
            target_dict = basic_quality_with_9th

        #print("debug: target_dict:",target_dict)

        temp_extension = list(extensions.keys())
        if no_extention:
            random_extension = rd.choice(temp_extension[3:])
        else:
            random_extension = rd.choice(temp_extension[va:])


        temp_modification = list(modifications.keys())
        if no_modification:
            random_modification = rd.choice(temp_modification[3:])
        else:
            random_modification = rd.choice(temp_modification[va:])

        result = rd.choice(['temp_extension', 'temp_modification'])

        temp_omittions = list(omittions.keys())
        if no_omissions:
            random_omission = rd.choice(temp_omittions[4:])
        else:
            random_omission = rd.choice(temp_omittions[vb:])

        chosen_UI_phrase = rd.choice(UI_phrase)
        if result == 'temp_extension':
            #print("debug: extension")
            # chord_components = target_dict[random_quality] + extensions[random_extension] - omittions[random_omission]
            to_remove = set(omittions[random_omission])
            chord_components = [
                x for x in target_dict[random_quality] + extensions[random_extension]
                if x not in to_remove
                ]
            #print("debug: extension", chord_components)
            if easy_reading_mode:
                printed_chord = f"{random_note}{random_quality}|{random_extension}|{random_omission}"
            else:
                printed_chord = f"{random_note}{random_quality}{random_extension}{random_omission}"
            
            print(f"{chosen_UI_phrase}: {printed_chord}")

        if result == 'temp_modification':
            #print("debug: modification")
            #chord_components = target_dict[random_quality] + modifications[random_modification] - omittions[random_omission]
            to_remove = set(omittions[random_omission])
            chord_components = [
                x for x in target_dict[random_quality] + modifications[random_modification]
                if x not in to_remove
                ]
            #print("debug: modification", chord_components)
            if easy_reading_mode:
                printed_chord = f"{random_note}{random_quality}|{random_modification}|{random_omission}"
            else:
                printed_chord = f"{random_note}{random_quality}{random_modification}{random_omission}"
            
            print(f"{chosen_UI_phrase}: {printed_chord}")


        if ("6" or "7" or "9" in random_quality) and (random_modification):  # if the chord already has a 7th, mod will not have a 7th note
            print("entering this stage, debug: current chord_components:", chord_components)
            if 12 in chord_components:
                chord_components.remove(12)
                #print("debug: removed 12")
        else:
            pass
        if (random_quality in ["dim", "aug"] and not any(x in random_quality for x in ["6", "7", "9"])) and random_modification:
            if "dim" in random_quality:
                chord_components.add(10)
            if "aug" in random_quality:
                chord_components.add(11)    



        random_modification = ""
        random_note_value = notes_dictionary.get(random_note) or alternative_notes_dictionary.get(random_note)
        chord_components = [x + random_note_value for x in chord_components]
        sorted_chord_components = sorted(chord_components)
        #print("debug: sorted_chord_components", sorted_chord_components)
        clean_chord_components = list(dict.fromkeys(sorted_chord_components))
        #print("debug: clean_chord_components", clean_chord_components)
        cleaned_chord_components = [
                  x - 24 if x > 24 else
                  x - 12 if x > 12 else
                  x for x in clean_chord_components
                                   ]
        #print("debug: cleaned_chord_components", cleaned_chord_components)
        
        
        if random_tonality in sharp_sign_tonality:
            print_notes = [notes[i-1] for i in cleaned_chord_components]
        if random_tonality in flat_sign_tonality:
            print_notes = [alternative_notes[i-1] for i in cleaned_chord_components]
        elif random_tonality in mixed_sign_tonality:
            temp_list=rd.choice([notes, alternative_notes])
            print_notes = [temp_list[i-1] for i in cleaned_chord_components]

        input("Input anything to see the answer")
        played_notes = []
        for i in range(len(clean_chord_components)):
            base = 4
            numb_oct = ( clean_chord_components[i] -1 )// 12 
            played_notes.append(print_notes[i]+f'{base + numb_oct}')

        print("you should play the following notes:", print_notes)
        
        print("debug: played_notes", played_notes)
        if play_the_chord:
            pct.play_arpeggio_then_chord(played_notes) 
        #time.sleep(3)# let the chord play





if __name__ == "__main__":
    
    print('-' * width)
    print("Welcome to the chord trainer!")
    print("This program will help you practice identifying and playing various chords.")
    print("You will be prompted to play a chord, and then the program will reveal the notes in that chord.")
    print("Let's get started!")
    print('-' * width)
    counter = 0
    #time.sleep(0.3)
    try:
        while True:
             if counter == 0:
                feedback = input("Ready to go? (y or n), if you don't say anything i'll continue: ")
             else:
                feedback = input("Again? (y or n), if you don't say anything i'll continue: ")

             if feedback.lower() in ['yes', 'y', '', 'yeah', 'sure', 'ok', 'okay', 'go', 'let\'s go', 'let us go', 'let us begin', 'let\'s begin', 'let\'s start', 'let us start', 'let\'s do it', 'let us do it', 'let\'s play', 'let us play']:   
                getachord()
                print('-' * width)
                counter += 1
             else:
                print("Fine, I'll go >:(")
                exit()
    except Exception as e:
        import traceback
        traceback.print_exc()
        input("press enter to quit")
