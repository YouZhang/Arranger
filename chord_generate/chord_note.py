#coding = utf-8
import string;
import os


do = '1';
ri = '2';
mi = '3';
fa = '4';
so = '5';
la = '6';
si = '7';

class tone():
    # fall a semitone
    def low_semi(self,note):
        if(note == fa):
            note_out = mi;
        elif(note== do):
            note_out = si;
        elif('+' in note):
            note_out = note[1];
        elif('-' in note):
            note_temp = int(note[1]) - 1;
            note_out = str(note_temp);
        else:
            note_out = '-' + note;
        return note_out;
    
    # raise a semitone
    def high_semi(self,note):
        if(note == mi):
            note_out = fa;
        elif(note== si):
            note_out = do;
        elif('+' in note):
            note_temp = int(note[1]) + 1;
            note_out = str(note_temp);
        elif('-' in note):
            note_out = note[1];
        else:
            note_out = '+' + note;
        return note_out;
    
    #raise the tone with n semitone;
    def high_tone(self,note,n):
        note_out = note;
        for i in range(n):
            note_out = self.high_semi(note_out)
        return note_out;
        
    #fall the tone with n semitone;
    def low_tone(self,note,n):
        note_out = note
        for i in range(n):
            note_out = self.low_semi(note_out)
        return note_out;
    
    #rasie chord 
    def high_chord(self,chord_in,n):
        for i in range(len(chord_in)):
            chord_in[i] = self.high_tone(chord_in[i],n);
        return chord_in; 
        
    #fall chord    
    def fall_chord(self,chord_in,n):
        for i in range(len(chord_in)):
            chord_in[i] = self.low_tone(chord_in[i],n);
        return chord_in;    
            
class chord_gen(tone):
    
    C = ['1','3','5'];
    D = ['2','+4','6'];
    E = ['3','+5','7'];
    F = ['4','6','1'];
    G = ['5','7','2'];
    A = ['6','+1','3'];
    B = ['7','+2','+4'];
    
    # min chord generate    
    def gen_min(self,chord_in):
        chord_min = chord_in;
        note_low = self.low_semi(chord_in[1]);
        chord_min[1] = note_low;
        return chord_min;
        
    # aug chord generate
    def gen_aug(self,chord_in):
        chord_aug = chord_in;
        note_high = self.high_semi(chord_in[2]);
        chord_aug[2] = note_high;
        return chord_aug;
        
    # dim chord generate
    def gen_dim(self,chord_in):
        chord_dim = chord_in;
        note_low = self.low_semi(chord_in[2]);
        chord_dim[2] = note_low;
        return chord_dim;
        
    # sus4 chord generate    
    def gen_sus4(self,chord_in):
        chord_sus4 = chord_in;
        note_high = self.high_semi(chord_in[1]);
        chord_sus4[1] = note_high;
        return chord_sus4;
     
    # 6 chord generate  
    def gen_6(self,chord_in):
        chord_6 = chord_in;
        note_temp = self.high_tone(chord_in[2],2);
        chord_6.append(note_temp);
        return chord_6;
        
    # 7 chord generate  
    def gen_7(self,chord_in):
        chord_7 = chord_in;
        note_temp = self.high_tone(chord_in[2],3);
        chord_7.append(note_temp);
        return chord_7;
    
    # major7 chord generate 
    def gen_maj7(self,chord_in):
        chord_maj7 = chord_in;
        note_temp = self.high_tone(chord_in[2],4);
        chord_maj7.append(note_temp);
        return chord_maj7;
        
    # add9 chord generate     
    def gen_add9(self,chord_in):
        chord_add9 = chord_in;
        note_temp = self.high_tone(chord_in[2],7);
        chord_add9.append(note_temp);
        return chord_add9;
        
    # maj9 chord generate    
    def gen_maj9(self,chord_in):
        chord_maj9 = chord_in;
        self.gen_maj7(chord_maj9);
        self.gen_add9(chord_maj9);
        return chord_maj9;
     
    # 9 chord generate  
    def gen_9(self,chord_in):
        chord_9 = chord_in;
        self.gen_7(chord_9);
        self.gen_add9(chord_9);
        return chord_9;
        
    # add11 chord generate       
    def gen_add11(self,chord_in):
        chord_add11 = chord_in;
        note_temp = self.high_tone(chord_in[1],1);
        chord_add11.append(note_temp);
        return chord_add11;
 
        

       
