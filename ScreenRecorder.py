#_______________________________________________________________________Screen Recorder_____________________________________________________
#It will record the Audio seperately with .wav extension and video seperately with .mp4 extension
#After recording it will merger both Audio and video files using ffmpeg 

#Module used
import datetime
from PIL import ImageGrab
import numpy as np 
import cv2
from win32api import GetSystemMetrics
import pyaudio
import wave
import subprocess

def Recording():
    audio = pyaudio.PyAudio()
    stream = audio.open(format=pyaudio.paInt16,channels=1,rate=44100,input=True,frames_per_buffer=1024)
    frames=[]

    #fetching the systems resolution
    width = GetSystemMetrics(0)
    height = GetSystemMetrics(1)

    #Naming of the output files
    #NOTE: declare the correct paths where the video, audio and final recording files to be stored
    time_stamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    VideoFile_name = f'E:\\amFOSS\\JARVIS\\Recorded\\Screen\\VideoFile-{time_stamp}.mp4'
    AudioFile_name = f'E:\\amFOSS\\JARVIS\\Recorded\\Audio\\AudioFile-{time_stamp}.wav'
    OutputFileName = f'E:\\amFOSS\\JARVIS\\Recorded\\SCREENRECORDED\\VideoFile-{time_stamp}.mp4'

    #declaring the fourcc as mp4v
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    captured_video = cv2.VideoWriter(VideoFile_name, fourcc, 20.0, (width, height))

    #Recording starts
    while True:
        img = ImageGrab.grab(bbox=(0,0,width,height)) # Records the whole screen
        image_np = np.array(img) #store it into a numpy array
        date = stream.read(1024) #records the voice
        frames.append(date)
        Final_img = cv2.cvtColor(image_np,cv2.COLOR_BGR2RGB) #converts BGR to RGB color
        cv2.imshow('Screen Recorder',Final_img) #Recording screen using cv2
        captured_video.write(Final_img)
        date = stream.read(1024)
        frames.append(date)
        
        #Exit condition press "q" to stop recording
        if cv2.waitKey(10) == ord('q'):
            stream.stop_stream()
            stream.close()
            audio.terminate()
            break

    #opeing the audiofile and writing the binary date into it
    soundFile = wave.open(AudioFile_name,"wb")
    soundFile.setnchannels(1)
    soundFile.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    soundFile.setframerate(44100)
    soundFile.writeframes(b''.join(frames))
    soundFile.close()

    cv2.destroyAllWindows()
    captured_video.release()

    #merging the video file and audio fiile into one file by wring this command into the cmd
    cmd = f"ffmpeg -i {VideoFile_name} -i {AudioFile_name} -c:v copy -c:a aac {OutputFileName}"
    subprocess.call(cmd, shell=True)