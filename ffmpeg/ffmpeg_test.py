# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 22:43:09 2018

@author: CARE-DESK-04
"""

import ffmpeg


if __name__ == "__main__":
    name_folder = "D:/TV/Encode"
    name_file = "input.ts"
    file = name_folder + "/" + name_file
    
    
    stream = ffmpeg.input(file)  
    stream = ffmpeg.output(stream, name_folder + "/Images/output%05d.png") 
    ffmpeg.run(stream)

