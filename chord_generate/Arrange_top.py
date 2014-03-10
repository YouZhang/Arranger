# -*- coding: cp936 -*-

#judge the song (major or minor):
#depart the song's section into several part;
# Arranger_first_step:  match the chord with major 3 or minor 6 chord
# Arranger_second_step: adjust the chord arrange
# Arranger_third_step:  change the chord with sus4 or ...
# Arranger_Tuner:   base on the key,to change the Tone with other chord;

from Arrange_step_1 import Arranger_first_step;
from Arrange_step_2 import change_chord;
import chord_note;
import chord_data_new;


chord_note_dict = chord_data_new.chord_note_dict;
note_chord_dict = chord_data_new.note_chord_dict;
chord_press_dict = chord_data_new.chord_press_dict_all;
delta = chord_data_new.delta;
Tuner = chord_note.tone();

def change_tone(key,chord_list):
    chord_press_list = [];
    chord_name_list = [];
    for chord in chord_list:
        note = chord_note_dict[chord]
        # print note
        note_Tuner = Tuner.high_chord(note,delta[key]);
        # print note_Tuner
        chord_name = note_chord_dict[str(note_Tuner)];
        chord_press = chord_press_dict[chord_name];
        chord_press_list.append(chord_press);
        chord_name_list.append(chord_name);
        # print chord_name;
        # print chord_press;
    return chord_name_list,chord_press_list;

def Arranger(key,song):
    #Arranger_first_step(song)
    Arranged_chord_1,song_note,Tone,section =  Arranger_first_step(song);
    Arranged_chord_2 = change_chord(song_note,Arranged_chord_1,Tone);
    chord_name_list,chord_press_list = change_tone(key,Arranged_chord_2);
    return chord_name_list,chord_press_list,section;

def get_song(file_path):
    fd = open(file_path,'r+');
    song = fd.read();
    fd.close();
    # section = song.split(section_sep);
    return song

if(__name__ == '__main__'):
    key = 'C';
    # song_path = 'D:/matlab/sound_prj/ex_2/tab/tab/tab_tkzc.txt';
    song_path = 'D:/python/PyQt/prj/Arrange/midi/output/test.txt';
    # chord_name_list,chord_press_list,section = Arranger(key,song_path);
    song = get_song(song_path);
    chord_name_list,chord_press_list,section = Arranger(key,song);
    for i in range(len(section)):
        print section[i];
        print chord_name_list[i];
        print chord_press_list[i];
