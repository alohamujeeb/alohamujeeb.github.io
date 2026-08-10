---
hide:
  - navigation
  
tags:
  - ffmpeg
---

# ```ffmpeg``` command reference

Note:<br>
**<font color=red>I haven't personally tested all the commands or options listed below. They are collected here solely for my own reference when needed.</font>**

---
## 1. Basic info & inspection

| Command           | Purpose |
|-------------------|---------|
| `ffmpeg -version` | Displays the FFmpeg version, along with the libraries it was compiled with. Useful for verifying the installed version and checking codec support. |
| `ffmpeg -buildconf` | Shows the configuration options used to build FFmpeg (e.g., enabled/disabled features and libraries). Helpful for debugging or verifying build options. |

## 2. Probe a media file
| Command    | Purpose |
|------------|--------|
| `ffprobe <filename>` |  Displays general media information (format, duration, bitrate, etc.) of the input file. |
| `ffprobe -show_streams <filename>` | Shows detailed information about each media stream (audio, video, subtitle) in the file.|
| `ffprobe -show_format <filename>`.| `ffprobe -show_format input.mp4` | Outputs detailed format-level metadata (e.g., tags, duration, bit rate) of the file. |
| `ffprobe -show_streams input.mp4` | Displays all streams in the media file, including video, audio, and subtitles. Look for `codec_type=video` and `codec_type=audio` in the output. |
| `ffprobe -select_streams v -show_streams input.mp4` | Shows only the video stream(s) from the input file. |
| `ffprobe -select_streams a -show_streams input.mp4` | Shows only the audio stream(s) from the input file. |


To see details of a video stream only:<br>
```ffprobe -v error -select_streams v:0 -show_entries  stream=index,codec_name,codec_type,width,height,bit_rate -of default=noprint_wrappers=1 input.mp4```

To see details of a audio stream only:<br>
```ffprobe -v error -select_streams a:0 -show_entries stream=index,codec_name,codec_type,channels,sample_rate,bit_rate -of default=noprint_wrappers=1 input.mp4```

### 2.1 Find supported formats

=== "command"
	```console
	ffmpeg -formats
	```

=== "Expected output"
	```console
	File formats:
	 D. = Demuxing supported
	 .E = Muxing supported
	 --
	 DE mov             QuickTime / MOV
	 D  matroska        Matroska
	  E mp4             MP4 (MPEG-4 Part 14)
	```
	
	D: Can read (demux) this format (i.e., as input).<br>
	E: Can write (mux) this format (i.e., as output).<br>
	DE: Can both read and write the format.<br>
To check a specific format:<br>
```ffmpeg -formats | grep mp4```


---
## 3. Play/Preview (file/camera)
| Command                          | Purpose       |
|----------------------------------|---------------|
| `ffplay input.mp4`          | Plays the media file with both audio and video.               |
| `ffplay -an input.mp4`      | Plays the file **without audio** (`-an` = audio none).        |
| `ffplay -vn input.mp4`      | Plays the file **without video** (`-vn` = video none).        |
| `ffplay -loop 0 input.mp4`  | Plays in a loop (0: for infinite times)|
| `ffplay -loop 3 input.mp4`  | Plays in a loop 3 times|
| `ffplay -loop 2 -autoexit input.mp4`  | Autoexit at the end of loop count|
|`ffplay -ss [start_time] -to [end_time] input.mp4`|play from t1 to t2|
|`ffplay -ss [start_time] -t [duration] input.mp4`|play from t1 upto duration|
|`ffplay rtsp://ip/stream` | play from a rtsp server|
|`ffplay /dev/video0` | play from a camera (linux only)|


---
## 4. Re-encoding (Transcoding)

**Change video codec:**<br>
```console
ffmpeg -i input.mp4 -c:v libx264 -crf 23 -preset fast -c:a aac output.mp4
```

**Change audio codec:**<br>
```console
ffmpeg -i input.mkv -c:v copy -c:a libopus output.webm
```

### 4.1 Stream selection
```console
ffmpeg -i input.mkv -map 0:v:0 -map 0:a:1 -c copy output.mkv
```

---
## 5. Cutting & trimming

=== "command"
	```console
	a) cut->save
	ffmpeg -i input.mp4 -ss 00:01:00 -t 00:00:10 -c copy output.mp4
	
	b) cut->rencode->save
	ffmpeg -i input.mp4 -ss 60 -t 90 -c:v libx264 -c:a aac output.mp4

	```

=== "Explaination"
	```console
	-i 	input.mp4	Specifies the input video file
	-ss Start time
	-t 	Duration
	-to end time
	```

---
## 6. Scaling & Filters
```console
ffmpeg -i input.mp4 -vf scale=1280:720 output.mp4
ffmpeg -i input.mp4 -vf "scale=640:360,fps=25" -c:v libx264 out.mp4

```
Applies a **video filter (-vf)** to resize the video to 1280x720 resolution (HD).<br>
(1280 pixels wide, 720 pixels tall)

--- 
## 7. Audio Operations

| Command  | Purpose      | Explanation  |
|----------|--------------|--------------|
| `ffmpeg -i input.mp4 -vn -acodec copy audio.aac`   | Extract audio   | Extracts the audio stream from a video file (`input.mp4`) without re-encoding and saves it as `audio.aac`. The `-vn` option disables video. |
| `ffmpeg -i input.wav -c:a libmp3lame output.mp3` | Convert audio format   | Converts a WAV audio file to MP3 using the `libmp3lame` codec. Good for compressing large audio files. |
| `ffmpeg -i input.mp3 -filter:a "volume=1.5" louder.mp3`   | Adjust audio volume   | Increases the volume of the input MP3 file by 1.5x and writes the result to `louder.mp3`. Uses an audio filter. |

### 7.1 various ways to use filters (-vf vs -f:a -f:v)

| Option        | Stream Type | Use Case     | Example     |
|---------------|-------------|--------------|-------------|
| `-vf` | Video | Apply basic video filter   | `-vf "scale=640:360"`    |
| `-filter:v` | Video  | Preferred for explicit video filters | `-filter:v "scale=640:360"`  |
| `-filter:a` | Audio  | Apply audio filter   | `-filter:a "volume=0.8"`  |

Example: **using audio and video filters in same command**<br>

### 7.2 Use video and audio filters togethar
```console
ffmpeg -i input.mp4 -filter:v "scale=1280:720" -filter:a "volume=1.5" output.mp4
```

### 7.3 List of filter parameters
???- "Video filter options <click to see details>"
	| Filter Name  | Brief Description    | Example Usage   |
	|--------------|------------|-----------|
	| scale        | Resize video                  | `-vf "scale=640:360"`                            |
	| crop         | Crop video                   | `-vf "crop=320:240:100:50"`                      |
	| rotate       | Rotate video                 | `-vf "rotate=PI/4"`                              |
	| hue          | Adjust hue/saturation        | `-vf "hue=s=0"` (desaturate)                     |
	| transpose    | Rotate/flip by 90°           | `-vf "transpose=1"` (rotate 90° clockwise)      |
	| overlay      | Overlay videos               | `-vf "overlay=10:10"`                            |
	| fade         | Fade in/out                  | `-vf "fade=t=in:st=0:d=5"` (fade in 5 seconds)  |
	| drawtext     | Draw text                   | `-vf "drawtext=text='Hello':x=10:y=10"`         |
	| eq           | Adjust brightness/contrast   | `-vf "eq=brightness=0.06:contrast=1.5"`         |
	| fps          | Change framerate             | `-vf "fps=30"`                                   |
	| mirror       | Flip horizontally            | `-vf "hflip"`                                    |
	| negate       | Invert colors               | `-vf "negate"`                                   |
	| delogo       | Remove logo                 | `-vf "delogo=x=20:y=20:w=100:h=77"`             |
	| vflip        | Flip vertically              | `-vf "vflip"`                                    |
	| hflip        | Flip horizontally            | `-vf "hflip"`                                    |
	| boxblur      | Apply blur                  | `-vf "boxblur=5:1"`                              |
	| unsharp      | Sharpen                    | `-vf "unsharp=5:5:1.0:5:5:0.0"`                  |
	| split        | Split stream                | `-vf "split=2[out1][out2]"`                      |
	| tile         | Mosaic from frames          | `-vf "tile=3x3"`                                 |
	| zoompan      | Zoom and pan               | `-vf "zoompan=z='zoom+0.001':d=1"`               |
	| setpts       | Speed control               | `-vf "setpts=0.5*PTS"` (2x speed)                 |
	| drawbox      | Draw rectangle              | `-vf "drawbox=x=10:y=20:w=100:h=50:color=red@0.5"` |
	| tblend       | Blend frames (motion blur) | `-vf "tblend=all_mode=average:all_opacity=0.7"`  |


???- "Audio filter options <click to see details>"

	| Filter Name    | Brief Description    | Example Usage    |
	|----------------|------|------------|
	| volume         | Adjust audio volume | `-af "volume=2.0"` (double volume)             |
	| aecho          | Add echo effect    | `-af "aecho=0.8:0.9:1000:0.3"`                 |
	| aresample      | Resample audio     | `-af "aresample=44100"`                         |
	| pan            | Remap audio channels   | `-af "pan=stereo|c0=c0|c1=c0"` (mono to stereo)|
	| atrim          | Trim audio       | `-af "atrim=start=5:end=10"`    |
	| lowpass        | Low-pass filter    | `-af "lowpass=f=3000"`        |
	| highpass       | High-pass filter    | `-af "highpass=f=300"`       |
	| bass           | Boost bass frequencies    | `-af "bass=g=10"`      |
	| treble         | Boost treble frequencies   | `-af "treble=g=5"`      |
	| equalizer      | Apply graphic equalizer    | `-af "equalizer=f=1000:t=q:w=1:g=5"`   |
	| silenceremove  | Remove silence      | `-af "silenceremove=1:0:-50dB"`  |
	| compand        | Compress dynamic range   | `-af "compand=attacks=0:decays=1000"`  |
	| pan            | Channel mixing     | `-af "pan=mono|c0=.5*c0+.5*c1"`   |
	| aphaser        | Phaser effect    | `-af "aphaser"`                                 |
	| aformat        | Convert audio format   | `-af "aformat=sample_fmts=s16:channel_layouts=stereo"` |
	| silencedetect  | Detect silence (analysis)    | `-af "silencedetect=n=-50dB:d=1"` (analysis only) |
	| showwaves | Visualize waveform (video filter) | `-vf "showwaves=s=640x120"` (audio visualizer) |
	| loudnorm   | Loudness normalization  | `-af "loudnorm"`   |

---
## 8. Subtitles

| Command   | Purpose    | Explanation   |
|-----------|------------|---------------|
| `ffmpeg -i input.mp4 -vf subtitles=subtitle.srt output.mp4` | Burn subtitles into video         | Adds the subtitles from `subtitle.srt` directly onto the video frames of `input.mp4` and saves the result as `output.mp4`. Uses a video filter. |
| `ffmpeg -i input.mkv -map 0:s:0 subs.srt`  | Extract subtitle stream   |0 refers to the first input file (input.mkv in this case)<br> selects subtitle streams <br>0: picks the first subtitle stream <br> So 0:s:0 = first subtitle stream of first input. |

---
## 9. Stream/play to/from a network

| Purpose                   | Command         |
|---------------------------|-----------------|
| Stream to RTMP server      | `ffmpeg -re -i input.mp4 -c copy -f flv rtmp://server/app/stream` |
| Receive from RTSP server   | `ffmpeg -i rtsp://ip/stream -c copy out.mp4`    |
| Concatenate (restream) RTSP input to another RTSP output | `ffmpeg -i rtsp://source-ip/source-stream -c copy -f rtsp rtsp://destination-ip/destination-stream` |
| Play from RTSP server (change IP and port)     | `ffplay rtsp://<ip:8554>/stream`   |


---
## 10. Screenshots & Thumbnails

**Single frame extraction**<br>
```console
ffmpeg -ss 00:00:10 -i input.mp4 -frames:v 1 shot.png
```

**Thumbnail strip**<br>
```console
ffmpeg -i input.mp4 -vf fps=1 thumb_%04d.png
```

- extact 1 frame every seconds
- then create multiple files (one file per frame)
- the output filenames are numbered with zero-padding according to %04d
	thumb_0001.png
	thumb_0002.png
	thumb_0003.png

```console
ffmpeg -i input.mp4 -vf "select=not(mod(n\,30)),scale=320:180,tile=5x5" -frames:v 1 thumb_strip.png
```

- This extracts frames (e.g., every 30th frame),
- scales them,
- arranges them in a 5x5 grid,
- and saves all thumbnails in one image thumb_strip.png.








