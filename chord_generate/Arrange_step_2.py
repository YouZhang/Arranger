# -*- coding: cp936 -*-

#judge the song (major or minor):
#depart the song's section into serval part;
# Arranger_first_step:  match the chord with major 3 or minor 6 chord
# Arranger_second_step: adjust the chord arrange
# Arranger_third_step:  change the chord with sus4 or ...
# Arranger_Tuner:   base on the key,to change the Tone with other chord;

# @ use_method = changed_chord =  change_chord(song_note_lhc,chord_list_1_lhc,maj_or_min)
# ex. : ['C', 'C', 'G', 'Fmaj7', 'C', 'C', 'C', 'C', 'G', 'C', 'G', 'F', 'Cadd9']

###############################for  test ################################################################
maj_or_min = 0;
# chord_list_1 = ['C', 'C', 'G', 'Fmaj7','C', 'C', 'C', 'C', 'G', 'C', 'G', 'F', 'Cadd9']
song_note_kbg = (['1', '3', '2', '5'],['1', '3', '6'],['1', '2', '5', '7'],['3', '4'],['3'],['1', '5'],['1', '5', '4', '6'],['3', '2', '5', '4'],['1', '3', '2', '4'],['1', '3', '2'],['1', '2', '5', '6'],['1', '2', '5', '6'],['1', '3', '2', '5', '4'])
chord_list_1_kbg = ['C', 'C', 'G', 'C', 'C', 'C', 'G', 'Fmaj7', 'C', 'C', 'C', 'C', 'G', 'C', 'G', 'F', 'Cadd9'];
chord_list_kbg = ['Cadd9','Am7/F(A)', 'Em7', 'C', 'Cadd9', 'Am7/F(A)', 'G', 'Fmaj7', 'C', 'C', 'Am7/F(A)', 'Csus4', 'Dm7/G', 'Cadd9', 'Gadd9', 'Am7/F(A)', 'Cadd9']
song_note_kbg = [['1', '3', '2', '5'], ['1', '3', '6'], ['1', '3', '2', '7'], ['3', '5'], ['1', '3', '2', '5'], ['1', '3', '6'], ['1', '2', '5', '7'], ['3', '4'], ['3'], ['1', '5'], ['1', '5', '4', '6'], ['3', '2', '5', '4'], ['1', '3', '2', '4'], ['1', '3', '2'], ['1', '2', '5', '6'], ['1', '2', '5', '6'], ['1', '3', '2', '5', '4']];
chord_list_1_lhc = ['Am', 'D7sus2', 'Am', 'Am7', 'Am7', 'Am7', 'A7', 'Am7', 'Am', 'D7sus2', 'Am', 'Am', 'Am', 'Em', 'Am7'];
song_note_lhc = [['3', '6'], ['3', '2'], ['1', '2', '7'], ['6'], ['6'], ['5', '6'], ['3', '5', '+4'], ['3'], ['3', '5', '6'], ['3', '2'], ['1', '3', '2', '7', '6'], ['1', '3','7'], ['3', '6'], ['1', '2', '5', '7'], ['6']]
chord_list_1_tkzc =['Gadd9', 'Am', 'Em', 'Am', 'C', 'Dm', 'Am', 'B', 'E', 'Am', 'Em', 'Am', 'C', 'Csus4', 'D7sus2', 'Am', 'E', 'Am']
song_note_tkzc = [['7', '6'], ['1', '3', '7'], ['3', '7'], ['1', '5', '6'], ['3', '5'], ['1', '3', '4'], ['1', '3'], ['7', '+4'], ['+5', '7', '6'], ['1', '3', '7'], ['3', '7'],['1', '5', '6'], ['3', '5'], ['1', '4', '7'], ['1', '3', '2'], ['1', '7','4', '6'],['+5', '7'], ['3', '6']]
###############################################################################################



maj_chord = ['C','F','G'];
min_chord = ['Am','Dm','Em'];

C_change = {'2':'Cadd9','4':'Csus4','6':'Am7/F(A)'};
G_change = {'3':'Em7','4':'Dm7','6':'Gadd9'};
F_change = {'2':'D7sus2','3':'Fmaj7','5':'Am7/F(A)'};

Am_change = {'2':'D7sus2','4':'Fsus4','5':'Am7/F(A)'};
Dm_change = {'1':'Dm7','3':'Fmaj7','5':'Fsus4','7':'Dm6'};
Em_change = {'1':'C/E','2':'Em7','4':'Fmaj7'};



def change_chord(song_note,chord_list_1,maj_or_min):
    if(maj_or_min):
        #do major chord change
        chord_list_1= change_maj_chord(song_note,chord_list_1);
    else:
        #do minor chord change;
        chord_list_1= change_min_chord(song_note,chord_list_1);
    return chord_list_1  
    
def change_min_chord(song_note,chord_list_1):
    for i in range(len(song_note)):
        matched_chord = chord_list_1[i]
        if(matched_chord == 'Am' or matched_chord == 'Am7'):
            for note,chord in Am_change.items():
                if(note in song_note[i]):
                    chord_list_1[i] = Am_change[note]
                    
        elif(matched_chord == 'Dm'):
            for note,chord in Dm_change.items():
                if(note in song_note[i]):
                    chord_list_1[i] = Dm_change[note]
        elif(matched_chord == 'Em'):
            for note,chord in Em_change.items():
                if(note in song_note[i]):
                    chord_list_1[i] = Em_change[note]
    return chord_list_1

def change_maj_chord(song_note,chord_list_1):
    for i in range(len(song_note)):
        matched_chord = chord_list_1[i]
        if(matched_chord == 'C'):
            for note,chord in C_change.items():
                if(note in song_note[i]):
                    chord_list_1[i] = C_change[note]
                    
        elif(matched_chord == 'G'):
            for note,chord in G_change.items():
                if(note in song_note[i]):
                    chord_list_1[i] = G_change[note]
        elif(matched_chord == 'F'):
            for note,chord in F_change.items():
                if(note in song_note[i]):
                    chord_list_1[i] = F_change[note]
    return chord_list_1

    
#find the common chord position    
def find_common_chord(chord_list):
    common_pos = [];
    common_pos_list = [];
    for i in range(len(chord_list)-2):
        if(chord_list[i] == chord_list[i+1]):
            common_pos.append(i);
        elif(common_pos != [] ):
            common_pos.append(i);
            common_pos_list.append(common_pos)
            common_pos = [];
    return common_pos_list
    
# def change_common_chord(common_pos_list,chord_list):
    # for pos in common_pos_list:
        # for i in range(lend(pos)):
            # chord = chord_list[i];
#####################################################################            
#change the chord from C=>Am
#change the chorf from Am => C; !!no use

# def change_chord(chord,maj_or_min):
    # if(maj_or_min == 0):
        # if(chord == 'Am'):
            # changed_chord = 'F';
        # elif(chord == 'Em'):
            # changed_chord = 'G';
        # elif(chord == 'Dm'):
            # changed_chord = 'F';
    # else:
        # if(chord == 'C'):
            # changed_chord = 'Am';
        # elif(chord == 'F'):
            # changed_chord = 'Dm';
        # elif(chord == 'G'):
            # changed_chord = 'Em';
    # return changed_chord;
    
# def change_common_chord(common_list,chord_list)  !!no use        
def analysis_chord_1(chord_list_1,maj_or_min):
    # chord_list_1 = change_common_chord(chord_list_1);
    if(maj_or_min == 1):
        maj_cnt = 0;
        for i in range(len(chord_list_1)):
            chord = chord_list_1[i]
            if(chord in maj_chord):
                maj_cnt = maj_cnt + 1;
                if(maj_cnt == 3):
                    chord_list_1[i] = change_chord(chord,maj_or_min);
                    maj_cnt = 0;
            else:
                maj_cnt = 0;
        min_cnt = 0;
    else:
        for i in range(len(chord_list_1)):
            chord = chord_list_1[i]
            if(chord in min_chord):
                min_cnt = min_cnt + 1;
                if(min_cnt == 3):
                   chord_list_1[i] = change_chord(chord,maj_or_min);
                   min_cnt = 0;
            else:
                min_cnt = 0;
    return chord_list_1
####################################################################
