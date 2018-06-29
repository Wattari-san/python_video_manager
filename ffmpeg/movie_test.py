# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 22:43:09 2018

@author: CARE-DESK-04
"""
import os
import glob
import cv2
import ffmpeg
import subprocess
import numpy as np

Folder = "D:/TV/Encode/"
#Folder = "C:/Users/CARE-DESK-04/Desktop/Video2018/"

THRESH = 55.55679398148148 # threshold 

ESC_KEY = 27     # Escキー
INTERVAL= 1      # 待ち時間

WINNAME = "test"
#cv2.namedWindow(WINNAME)

class edit():
    index = -1
    
    def __init__(self, source, target):
        edit.index += 1
        self.source = source
        self.target = target
        self.scenes = []
        self.cut_frames = []
        self.c = [1, 2, 3, 4]
    
    def print_data(self):
        keys = self.__dict__.keys()
        values = self.__dict__.values()
       
        print("Index: ", self.index)
        for key in keys:
            
            print(key, ": ",self.__dict__[key])
        print("\n")

# Mean Square Error
def MSE(pic): 
    return np.mean(np.square(pic))

# Mean Absolute Error
def MAE(pic): 
    return np.mean(np.abs(pic))

# フォルダ内ファイルリストの取得
def listup_files(path):
    files = [os.path.abspath(p) for p in glob.glob(path)]
    return files

# ターゲットのファイル名に変換
def target_names(source_list, s=17, e=-3):
    target_list = []
    for source in source_list:
        target_list.append(os.path.basename(source)[s:e] + ".mp4")
    
    return target_list

def create_cmd():
    cmds = []
    for i in range(2):
        if i==0:
            cmd = "@echo off"
        if i==1:
            cmd = "empty.exe *"
        cmds.append(cmd)
    return cmds

def create_bat(cmds, name, folder):
    bat_text = ""
    for cmd in cmds:
        bat_text += cmd + "\n"
    
    print(bat_text)
        
    os.remove(folder + name)
    bat_file = open(folder + name, "a")
    bat_file.write(bat_text)
    bat_file.close()
    return

if __name__ == "__main__":
    
    
    source_list = listup_files(Folder + "*.ts")
    target_list = target_names(source_list)

    source = source_list[1]
    video = cv2.VideoCapture(source) 
    fps    = video.get(cv2.CAP_PROP_FPS)
    height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
    width  = video.get(cv2.CAP_PROP_FRAME_WIDTH)
    framenum = video.get(cv2.CAP_PROP_FRAME_COUNT);
    print(framenum)
    
    frame_cnt = 1
    while(video.isOpened()):
        
        # Capture frame-by-frame
        ret, frame = video.read()
        
        if ret==False:
            break
        
        print(frame_cnt)
        
        
#        # Our operations on the frame come here
#        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        cv2.imshow('frame', frame)
            
        frame_cnt += 1
        
                
        key = cv2.waitKey(1) # quit when esc-key pressed      
        if key == ESC_KEY:
            break    
        
        
            


    picsize = (64, 36)
    frame_cnt = 0
       
    
#    clips = []
#    for i in range(3):
#        c = edit("file", i)
#        c.print_data()
#        clips.append(c)
        

# Release everything if job is finished
video.release()
#out.release()
cv2.destroyAllWindows()


    
#    stream = ffmpeg.input(file)
#    
#    stream = ffmpeg.output(stream, "output.mp4", t=10, ss=10)
#    
#    ffmpeg.run(stream)

