import subprocess
import re
import random
from time import time

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


class Video:
    def __init__(self, text, video_path, thread=0):
        self.video_path = video_path
        self.text = text
        self.offset = None
        self.thread = thread

    def start(self):
        self.make_rand_frame()
        self.add_text_to_img(self.text)

    def get_video_length(self):
        startupinfo = subprocess.STARTUPINFO()
        process = subprocess.Popen(['ffmpeg', '-i', self.video_path], startupinfo=startupinfo, stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT)
        stdout, stderr = process.communicate()
        pattern = re.compile(r'Duration: ([\w.-]+):([\w.-]+):([\w.-]+),')
        match = pattern.search(stdout)
        if match:
            hours = match.group(1)
            minutes = match.group(2)
            seconds = match.group(3)
        else:
            hours = minutes = seconds = 0
        total = 0
        total += 60 * 60 * int(hours)
        total += 60 * int(minutes)
        return total

    def make_rand_frame(self):
        length = self.get_video_length()
        self.offset = random.randint(0, length)
        startupinfo = subprocess.STARTUPINFO()
        output = subprocess.Popen(["ffmpeg",
                                   "-y",
                                   "-ss", str(self.offset),
                                   "-i", self.video_path,
                                   "-vframes", "1",
                                   "-vcodec", "png", "tmp/" + str(self.thread) + ".png"],
                                  startupinfo=startupinfo).communicate()
        return

    def add_text_to_img(self, text):
        img = Image.open("tmp/" + str(self.thread) + ".png")
        W, H = img.size
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("mom.ttf", (H + W) / 100)
        try:
            w, h = draw.textsize(text, font)
        except:
            w, h = 200, 30
        draw.rectangle([(W - w) / 2 - 3, (H - h) / 2 - 3, (W - w) / 2 + w + 3, (H - h) / 2 + h + 3], fill=(0, 0, 0))
        draw.text(((W - w) / 2, (H - h) / 2), text, (255, 255, 255), font=font)
        img.save("out/" + str(self.thread) + str(time()).replace(".", "") + '.png')
