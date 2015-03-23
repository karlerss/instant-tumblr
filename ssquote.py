import sys
from HTMLParser import HTMLParser
import random
import subprocess
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from time import time
import random, string, re

testing = False

print u"Käivitan..."

movies = ['D:\Filmid\Sabrina 1954 720p BluRay X264-AMIABLE [EtHD]\Sabrina.1954.720p.BluRay.X264-AMIABLE.mkv',
          'D:\Filmid\Roman.Holiday.1953.720p.WEB-DL.H264-HDB [PublicHD] [PublicHD]\Roman.Holiday.1953.720p.WEB-DL.AAC2.0.H.264.mkv',
          'F:\Filmid\In.a.Lonely.Place.1950.720p.WEB-DL.H264-ViGi [PublicHD]\In.a.Lonely.Place.1950.720p.WEB-DL.AAC2.0.H.264-ViGi.mkv',
          'F:\Filmid\Persona.1966.Criterion.Collection.1080p.BluRay.x264-PublicHD\Persona.1966.Criterion.Collection.1080p.BluRay.x264-PublicHD.mkv',
          'F:\Filmid\Through.A.Glass.Darkly.1961.Criterion.Collection.1080p.WEB-DL.H264-PublicHD\Through.A.Glass.Darkly.1961.Criterion.Collection.1080p.WEB-DL.H264-PublicHD.mkv',
          'D:\Filmid\Roman.Holiday.1953.720p.WEB-DL.H264-HDB [PublicHD] [PublicHD]\Roman.Holiday.1953.720p.WEB-DL.AAC2.0.H.264.mkv',
          'D:\Filmid\Coffee.and.Cigarettes.2003.1080p.BluRay.X264-AMIABLE [PublicHD]\Coffee.and.Cigarettes.2003.1080p.BluRay.X264-AMIABLE.mkv',
          'D:\Filmid\Mala Noche [1985] Gus Van Sant\Mala Noche.1985.avi',
          'D:\Filmid\The.Temptation.Of.St.Tony.2009.LiMiTED.DVDRiP.XViD-HLS [NO-RAR] - [ www.torrentday.com ]\hls-stony.avi',
          'D:\Filmid\1962 - Lolita  - James Mason,Peter Sellers,Sue Lyon\Kubrick - Lolita (1962) James Mason,Peter Sellers,Sue Lyon(2h-29m).avi',
          'D:\Filmid\A Torinoi lo\A Torinoi lo.avi',
          'D:\Filmid\Contempt.1963.720p.BluRay.x264-CiNEFiLE\Contempt.1963.720p.BluRay.x264-CiNEFiLE.mkv',
          'D:\Filmid\Some Like It Hot 1959 BDRip 1080p DTS mutisub HighCode\Some Like It Hot 1959 BDRip 1080p DTS mutisub HighCode.mkv',
          'D:\Filmid\Who\'s.Afraid.of.Virginia.Woolf.1966.DVDRip.H264.AAC.Gopo\Who\'s.Afraid.of.Virginia.Woolf.1966.DVDRip.H264.AAC.Gopo.mp4',
          'D:\Filmid\Pierrot.le.fou.(1965).x264.aac.rus.sub.tRuAVC.mkv',
          'F:\Filmid\Only.Lovers.Left.Alive.2013.1080p.BluRay.x264.DTS-RARBG\Only.Lovers.Left.Alive.2013.1080p.BluRay.x264.DTS-RARBG.mkv',
          'F:\Filmid\The Good The Bad And The Ugly (1966) [1080p]\The.Good.the.Bad.and.the.Ugly.1966.1080p.BrRip.x264.YIFY.mp4',
          
          ]

def get_video_length(path):
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    process = subprocess.Popen(['ffmpeg', '-i', path], startupinfo=startupinfo, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
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

def str_rand(length):
   return ''.join(random.choice(string.lowercase) for i in range(length))

def makeRandFrame():
    videopath = random.choice(movies)
    length = get_video_length(videopath)
    offset = random.randint(0, length)
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    output = subprocess.Popen(["ffmpeg",
                    "-y",
                    "-ss", str(offset),
                    "-i", videopath,
                    "-vframes", "1",
                    "-vcodec",  "png", "img.png"], startupinfo=startupinfo).communicate()

def addTextToImg(text):
    table = {
          ord(u'õ'): u'ö',
          ord(u'Õ'): u'ö',
          ord(u'š'): u'sh'
        }
    #text = text.decode("utf8")
    text = text.translate(table)
    img = Image.open("img.png")
    W, H = img.size
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("mom.ttf", (H+W)/100)
    try:
        w, h = draw.textsize(text, font)
    except:
        w, h = 200, 30
    draw.rectangle( [(W-w)/2-3, (H-h)/2-3, (W-w)/2+w+3 , (H-h)/2+h+3], fill=(0,0,0))
    draw.text(((W-w)/2,(H-h)/2),text,(255,255,255), font=font)
    img.save("output/"+str(time()).replace(".", "")+'.png')


class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.MESSAGES = []
        self.inP = False

    def handle_starttag(self, tag, attrs):
        if tag.lower() == 'p':
            self.inP = True

    def handle_endtag(self, tag):
        if tag.lower() == 'p':
            self.inP = False
        
    def handle_data(self, data):
        if self.inP == True:
            self.MESSAGES.append(data)


if testing == False:
    print u"Laen sõnumeid..."
    html = open('messages.htm').read()
    html = html.decode('UTF-8')
    print html[0]
    parser = MyHTMLParser()
    parser.feed(html)

while True:
    n = input(u"mitu teeme?")
    i = 1
    while i <= n:
        try:
            msg = random.choice(parser.MESSAGES)
        except:
            msg = "Hello world! õäöü"
        if len(msg) > 10:
            makeRandFrame()
            addTextToImg(msg)
            print "Pilt valmis("+str(i)+")"
            i = i+1

