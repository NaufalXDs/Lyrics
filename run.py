import time
import sys

def running_lyrics():
    
    # example ("lirik1", (tempo per character))
    lyrics = [
        ("Mengapa ku tancap gas dan melaju", 0.1),
        ("Padahal lampu kuning telah peringatkanku?", 0.2),
        ("Bahaya di depanku", 0.2),
        ("Hati-hati kecewa 'kan menunggu", 0.2),
        ("Lagu lama yang aku tahu", 0.2)
    ]

    delay_line = [0.4, 0.6, 0.6, 0.6, 0.6]
    
    print('''
          
        Lampu Kuning
          
          ''')
    
    for i, (line_music, delay_text) in enumerate(lyrics):
        for text in line_music:
            print(text, end="")
            sys.stdout.flush()
            time.sleep(delay_text)
        time.sleep(delay_line[i])
        print("")

    print("navdev/NaufalxDs")

running_lyrics()
    