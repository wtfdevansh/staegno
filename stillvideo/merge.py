import cv2
import os
from moviepy.editor import *
import numpy as np

def merge(frame_no,framewData,url):

  
    cap = cv2.VideoCapture(url)

    fps = int(cap.get(cv2.CAP_PROP_FPS))

 

    frames = []

    current_frame = 0

    while cap.isOpened():
        ret , frame = cap.read()

        if not ret:
            break

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        if current_frame == frame_no:
            frame_rgb = cv2.cvtColor(framewData, cv2.COLOR_RGB2BGR)
            frames.append(frame_rgb)
        
        else:
            frames.append(frame_rgb)


        current_frame += 1
    
    cap.release()

    clip = ImageSequenceClip(frames, fps=fps)


    clip.write_videofile("assests\outputVideos\output.mp4", codec="libx264")


       






    



