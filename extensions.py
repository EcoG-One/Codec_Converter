# Source - https://stackoverflow.com/a
# Posted by mortalis, modified by community. See post 'Timeline' for change history
# Retrieved 2025-11-17, License - CC BY-SA 4.0

import subprocess, re

ffmpeg = r'C:\Users\EcoG\PycharmProjects\Codec_Converter\ffmpeg\bin\ffmpeg.exe'

LINE_PATTERN = r' +\S+ +(\S+)'
EXT_PATTERN = r'Common extensions: (.+)\.'

# Get demuxers
output = subprocess.getoutput([ffmpeg, '-hide_banner', '-demuxers'])
lines = output.split('\n')[4:]

demuxers = {}
for line in lines:
    demuxer = re.findall(LINE_PATTERN, line)[0]

    info = subprocess.getoutput(
        [ffmpeg, '-hide_banner', '-h', f'demuxer={demuxer}'])
    exts = re.findall(EXT_PATTERN, info)
    if exts:
        demuxers[demuxer] = exts[0].split(',')

# Get muxers
output = subprocess.getoutput([ffmpeg, '-hide_banner', '-muxers'])
lines = output.split('\n')[4:]

muxers = {}
for line in lines:
    muxer = re.findall(LINE_PATTERN, line)[0]

    info = subprocess.getoutput(
        [ffmpeg, '-hide_banner', '-h', f'muxer={muxer}'])
    exts = re.findall(EXT_PATTERN, info)
    if exts:
        muxers[muxer] = exts[0].split(',')

# Write extensions
file_name = 'ffmpeg_extensions.txt'
f = open(file_name, 'w')

exts = set()
for ext in demuxers.values():
    [exts.add(x.strip()) for x in ext]
for ext in muxers.values():
    [exts.add(x.strip()) for x in ext]
for ext in sorted(exts):
    f.write(ext + '\n')

f.close()

print('Extensions written to file: ' + file_name)
