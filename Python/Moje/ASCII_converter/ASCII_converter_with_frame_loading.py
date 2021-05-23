from os import system
from threading import Thread
from PIL import Image #pip install pillow
import cv2 #pip install opencv-python
import moviepy.editor as mp#pip install ffmpeg moviepy
from playsound import playsound
import time

ascii_chars = ['$', '@', 'B', '%', '8', '&', 'W', 'M', '#', '*', 'o', 'a', 'h', 'k', 'b', 'd', 'p', 'q', 'w', 'm', 'Z', 'O', '0', 'Q', 'L', 'C', 'J', 'U', 'Y', 'X', 'z', 'c', 'v', 'u', 'n', 'x', 'r', 'j', 'f', 't', '/', '\\', '|', '(', ')', '1', '{', '}', '[', ']', '?', '-', '_', '+', '~', '<', '>', 'i', '!', 'l', 'I', ';', ':', ',', '"', '^', '`', '.', ' ']

def convert_image(image):
    # resize image so that it fits in terminal
    w, h = image.size 
    new_w = 100
    new_h = int(new_w * (h/w) * 0.55)
    new_image = image.resize((new_w, new_h))
    #turn image into grayscale
    image = new_image.convert('L')
    #turn into ASCII
    pixels = image.getdata()
    chars = ''.join([ascii_chars[pixel//4] for pixel in pixels])
    #turn into rows to create final image
    return "\n".join([chars[index:(index+new_w)] for index in range(0, len(chars), new_w)])

def question(text, answers):
    x = ''
    while x not in answers:
        x = input(text)
    return x

def music():
    playsound('my_result.mp3')

def main():
    file_format = question('Do you want to convert a (V)ideo or a (P)icture? ', ['V', 'P'])
    path = input('Input image path: ')
    if file_format == 'P':
        print(convert_image(Image.open(path)))
    else:
        my_clip = mp.VideoFileClip(path)
        my_clip.audio.write_audiofile(r'my_result.mp3')
        vidcap = cv2.VideoCapture(path)
        nframes = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)
        success, frame = vidcap.read()
        frames = []
        while success:
            system('cls')
            print(len(frames), '/', nframes, 'loaded' )
            frames.append(convert_image(Image.fromarray(frame)))
            success, frame = vidcap.read()
        
        input('press any key to begin')
        thread = Thread(target = music)
        thread.start()
        for i, frame in enumerate(frames):
            system('cls')
            print(frame)
            time.sleep(1/50)

            
main()