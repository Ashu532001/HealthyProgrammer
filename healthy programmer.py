from pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()

    while True:
        user_input = input()
        if user_input == stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__ == '__main__':
    init_water = time()
    init_eyes = time()
    init_excercise = time()
    watersec = 60*60
    eyesec = 2*60*60
    excersec = 45*60

    while True:
        if time() - init_water > watersec:
            print("it's time to drink water enter drank to stop the alarm")
            musiconloop("water.mp3", "drank")
            init_water = time()
            log_now("drank water at")

        if time() - init_eyes > eyesec:
            print("it's time to do eye excercise enter doneeyex to stop the the alarm")
            musiconloop("background.wav", "doneeyex")
            init_eyes = time()
            log_now("eye excercise done at ")

        if time() - init_excercise > excersec:
            print("it's time to do physical activity enter donephy to stop the the alarm")
            musiconloop("physical.mp3", "donephy")
            init_excercise = time()
            log_now("physical activity done at ")
