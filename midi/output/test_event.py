import midi;
song_path = 'D:/matlab/sound_prj/sound_2_tab/aj.mid' ;
patten = midi.read_midifile(song_path);
# print patten
for track_index in range(len (patten)):         
    for event_index in range( len(patten [track_index])):
        event = patten[track_index][event_index ];
        print event
