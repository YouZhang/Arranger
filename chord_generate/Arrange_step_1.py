# -*- coding: cp936 -*-

from __future__ import division
import string;
import chord_data_new;


__doc__ = '''
#judge the song (major or minor):
#depart the song's section into serval part;
# Arranger_first_step:  match the chord with major 3 or minor 6 chord
# Arranger_second_step: adjust the chord arrange
# Arranger_third_step:  change the chord with sus4 or ...
# Arranger_Tuner:   base on the key,to change the Tone with other chord;

@you can use the tab folder files to test this script;example:
    file_path = '../tab.txt'
    Arranged_chord_1,song_note,Tuning,section =  Arranger_first_step(file_path);
@there are some method will be not used in the script;
'''

beat_sep = ') (';
section_sep = ','

plus = chord_data_new.plus_chord_dict;  
maj = chord_data_new.maj_3_chord_dict; 
min = chord_data_new.min_3_chord_dict;
C = chord_data_new.C_chord_dict;
chords_dict = [plus,maj,min,C];
Threshold = 0.075

#format the '(0) (0) (0) (6 7)' => ['0', '7', '6']
def deal_seaction(note):
    plus_note = [];
    i = 0;
    while(i < len(note)):
        if(note[i] == '+' ):
            temp = note[i:i+2];
            plus_note.append(temp);
            i = i + 2;
        elif(note[i].isalnum()):
            plus_note.append(note[i]);
            i = i + 1;
        else:
            i = i + 1;
    note_list = list(set(plus_note));
    try:
        note_list.remove('0');
    except ValueError :
        note_list = note_list;
    return note_list    
    

#calculate the share of note
#input:section '(0) (0) (0) (6 7)'
def note_share_cal(section_note):
    share_in_section_list = [];      #share of the every note list
    note_list = deal_seaction(section_note)
    # note_list = section_note;
    # print note_list
    beat_note = section_note[1:-1].split(beat_sep);   #note in a beat
    beat_num = len(beat_note);                  #beat's number  
    for note in note_list:
        share_in_beat_list = [];         #share_in_beat_list
        for beat_note_i in beat_note:
            if('+' in beat_note_i):
                plus_num = beat_note_i.count('+');
                length = len(beat_note_i.replace(' ','')) - plus_num;
            else:
                length = len(beat_note_i.replace(' ',''));
            share_in_beat = beat_note_i.count(note)/length;
            share_in_beat_list.append(share_in_beat);
        share_in_section = sum(share_in_beat_list)/beat_num;
        share_in_section_list.append(share_in_section);
        
    return share_in_section_list,note_list;
    
#match the note with chord    
def match_note(section_note,chord_note,share):
    cnt = 0;
    match_rate = 0;
    for i in range(len(section_note)):
        if(section_note[i] in chord_note):
            match_rate = match_rate + share[i];
            cnt = cnt + 1;
    rate = cnt / len(chord_note)
    # match = match_rate/1.25 + rate/10     #second way
    match = match_rate;
    return match;

#calculate the match_chord_share_dict;
#num = 0,1,2,3___plus,maj,min,C
def cal_match_dict(section_note,share,num):
    match_dict = {};
    for chord_name,chord_note in chords_dict[num].items():
        match_rate = match_note(section_note,chord_note,share);
        match_dict[chord_name] = match_rate;
    return match_dict;
    
def match_chord(section,share,Tuning):
    section_note = deal_seaction(section)
    plus_Ture = '+' in section
    if(plus_Ture):
        match_dict = cal_match_dict(section_note,share,0);
    elif(Tuning == 1):
        match_dict = cal_match_dict(section_note,share,1);
    else:
        match_dict = cal_match_dict(section_note,share,2);
    match_dict = sorted(match_dict.items(), key = lambda x:x[1])
    l = len(match_dict);
    
    equal = (match_dict[l-1][1] - match_dict[l-2][1] <= Threshold)
    if(equal & ~plus_Ture ):
        match_dict = cal_match_dict(section_note,share,3);
        l = len(match_dict);
        # print match_dict;
        match_dict = sorted(match_dict.items(), key = lambda x:x[1])
    matched_chord = match_dict[-1][0];
    return matched_chord,section_note;

    
# song = '() () () (),'  
#judge the beginning of the music;
#judge the end of the music; 
def judge_maj_or_min(song):
    l = len(song);
    # print song[l-2]
    if(song[l-2] == '6'):
        Tuning = 0;
    else:
        Tuning = 1;
    return Tuning;

#depart the section into serveral chord;    !will be used
def depart_section(section_note):
    share = note_share_cal(section_note);
    print share;

  
def get_song(file_path):
    fd = open(file_path,'r+');
    song = fd.read();
    fd.close();
    section = song.split(section_sep);
    return song,section

# key = 'C' or 'D' or 'E'...no use
def Arranger(key):

    file_path = 'D:/matlab/sound_prj/ex_2/tab/tab/tab_kbg.txt'
    song,section = get_song(file_path);
    for section_num in range(len(section)):
        print section[section_num]
        share,note_list = note_share_cal(section[section_num])
        # print share
        chord_c = match_chord(section[section_num],share);
        Tuner = chord_note.tone();
        # print c;
        note_Tuner =  Tuner.high_chord(chord_data.chord_note_dict[chord_c],chord_data.delta[key])
        chord_Tuner = chord_data.note_chord_dict[str(note_Tuner)]
        print chord_Tuner;
        print chord_data.chord_press_dict[chord_Tuner];

#no use!
def Em2C_Am2F(matched_chord,section_note):
    section_note = ''.join(section_note);
    if(matched_chord == 'Em' and section_note == '35'):
        matched_chord = 'C';
    elif(matched_chord == 'Am' and section_note =='16'):
        matched_chord = 'F';
    return matched_chord;        
#no use!
def F2Dm_C2Em(matched_chord,section_note):
    section_note = ''.join(section_note);
    if(matched_chord == 'F' and '4' in section_note):
        matched_chord = 'Dm';
    return matched_chord; 
    

def Arranger_first_step(file_path):
    song_note = [];
    Arranged_chord_1 = [];
    song,section = get_song(file_path);
    Tuning = judge_maj_or_min(song);
    for section_num in range(len(section)):
        # print section[section_num]    #for test
        share,note_list = note_share_cal(section[section_num])
        # print share                   #for test
        matched_chord,section_note = match_chord(section[section_num],share,Tuning);
        matched_chord = Em2C_Am2F(matched_chord,section_note)
        Arranged_chord_1.append(matched_chord);
        song_note.append(note_list);
    return Arranged_chord_1,song_note,Tuning,section;
