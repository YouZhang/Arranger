# -*- coding: cp936 -*-
#the num represent the note
import chord_note
import random
class chord_pic():
        
    first_string = ('3','4','+4','5','+5');
    second_string = ('7','1','+1','2','+2');
    third_string = ('5','+5','6','+6','7');
    forth_string = ('2','+2','3','4','+4');
    fifth_string = ('6','+6','7','1','+1');
    sixth_string = ('3','4','+4','5','+5');
    strings = (first_string,second_string,third_string,forth_string,fifth_string,sixth_string);
    
    string_1 = '╓───┬───┬───┬───┐';
    string_2 = '╟───┼───┼───┼───┤';
    string_3 = '╟───┼───┼───┼───┤';
    string_4 = '╟───┼───┼───┼───┤';
    string_5 = '╟───┼───┼───┼───┤';
    string_6 = '╙───┴───┴───┴───┘';
       
    list1 = list(string_1);
    list2 = list(string_2);
    list3 = list(string_3);
    list4 = list(string_4);
    list5 = list(string_5);
    list6 = list(string_6);
    list_all = [list1,list2,list3,list4,list5,list6];
    

        
    def paint_dot(self,pos,list):
        
        if(pos == []):
            list[4:6] = '×';
        elif(pos[0] == 1):
            list[4:6] = '●';
        elif(pos[0] == 2):
            list[12:14] = '●';
        elif(pos[0] == 3):
            list[20:22] = '●';
        elif(pos[0] == 4):
            list[28:30] = '●';
        string_painted = ''.join(list);    
        print string_painted;
        
    #make sure the chord_note'pos   
    def pos_check(self,chord_in,str_index):
        pos = [];
        for chord_note in chord_in:
            try:
                pos_temp = self.strings[str_index].index(chord_note);
                pos.append(pos_temp);
            except ValueError:
                pos = pos;
        return pos;
    
        
    #generate_the chord_pic
    def pic_gen(self,chord_in):
        pos = [];
        for i in range(6):
            pos.append(self.pos_check(chord_in,i));
        print pos;
        
        for i in range(6):
            self.paint_dot(pos[i],self.list_all[i]);
        
    
