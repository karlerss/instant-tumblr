# instant-tumblr

##Introduction

This script generates content by combining facebook chat logs with movie screenshots.

See examples here: http://aegonlahkuda.tumblr.com/

##Requirements

This script requires:

- [Python 2.7.x](https://www.python.org/download/releases/2.7/)
- [ffmpeg](https://www.ffmpeg.org/download.html) for video processing
- Python imaging library (PIL) / Pillow: `pip install Pillow`
- The chat log (messages.htm) from your [facebook data](https://www.facebook.com/help/131112897028467/)

##Usage

1. Install requirements
2. Place the chat log file into script directory
3. Replace the paths in `movies` with your own
4. Start the program
5. Follow promts

##Troubleshooting

- For the `The _imagingft C module is not installed` error, download & install http://gnuwin32.sourceforge.net/packages/freetype.htm. Restart the computer.
