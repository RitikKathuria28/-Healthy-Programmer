from pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        input_of_user = input()
        if input_of_user == stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")




if __name__ == '__main__':
    init_water = time()
    init_eye = time()
    init_exercise = time()
    water_secs = 40*60
    eye_secs = 30*60
    exercise_secs = 45*60

    while True:
        if time()-init_water > water_secs:
            print("water drinking time Enter 'drankcompl to stop the alarm'")
            musiconloop("water.mp3", "drank")
            init_water = time()
            log_now("drank water at")

        if time() - init_eye > eye_secs:
            print("Eye exercise time, Enter 'done' to stop the alarm")
            musiconloop("eye.mp3", "done")
            init_eye = time()
            log_now("eye exercise at")

        if time() - exercise_secs > exercise_secs:
            print("Exercise time Enter 'completed' to stop the alarm'")
            musiconloop("exercise.mp3", "completed")
            init_exercise = time()
            log_now("Exercise at")






