---
date: 
  created: 2026-05-01
  posted:  2025-05-01
author:
  name: Mujeeb
  description: Creator
readtime: 15

categories: 
  - Multimedia
  - Video
tags:
   - H264
   - H265
   - Video Encoding
   - I frame
   - B frame
   - P frame
   - Key frame
---

# Video Encoding – Part 2 (Video Codecs)

In the previous section [Video Encoding Part-1](2026-04-29-video_encoding_p1.md), we looked at how individual images are represented and compressed using formats like BMP, PNG, and JPEG. . However, video is not just a collection of independent images—it leverages compression both **within each frame (spatial compression)** and **across frames (temporal compression)** by exploiting similarities between consecutive frames.
<!-- more -->

---
## 1. Sequence of images and video encoding

- A video is a sequence of such images (called **frames**) that are stored or transmitted one after another.

- As discussed in the previous article, an image is captured (for example from a camera) as a **raw frame**, which can be very large in size. To make it practical for storage and transmission, it is compressed into formats like **JPEG**.


- As a **first step**, each frame is compressed using image compression techniques (similar to JPEG).

- However, **video encoding goes a step further**; Instead of treating every frame independently, it compares each frame with its adjacent frames and encodes only the differences between them.

- This process—called **video encoding**, and it significantly reduces the amount of data, often by more than 10×, compared to sending individually compressed images for every frame.

- Video encoding is usually a **computational** intense process; And depending on the parameters chosen, the process can take significant processor and system resources. 

- Video codecs typically use a combination of:
    <br>- Intra-frame compression (within a frame, similar to JPEG)
    <br>- Inter-frame compression (between frames, using **motion and differences**)


---
## 2. Video encoding algorithms

- There are various algorithms used to perform this inter-frame compression, such as **H.264, H.265**, etc.

- Each algorithm offers different trade-offs:
    <br>- Some prioritize better visual quality
    <br>- Some prioritize faster encoding/decoding speed
    <br>- Some aim for higher compression efficiency (smaller file size at similar quality)

- In addition to the algorithm itself, several encoding parameters also impact the final output:
    <br>- **Bitrate**: controls how much data is used per second (higher = better quality, larger size)
    <br>- **Frame rate (FPS)**: affects smoothness and bandwidth
    <br>- **Resolution**: higher resolution increases data size
    <br>- **Keyframe interval** (I-frame frequency): impacts seeking, latency, and compression efficiency

--- 
## 3. Frame types (I,P,B)

- Video codecs do not treat all frames equally. Instead, they use different frame types to reduce redundancy and improve compression efficiency.

- The three main frame types are:

<br> **I-frames (aka Key frame)** (Intra-coded frames): a fully self-contained video frame that is encoded independently, without referencing any other frames, and acts as a complete image in the video stream.
    
```
- Fully self-contained frames; 
- Similar to a standalone image (like JPEG)
- Do not depend on any other frame
- Used as reference points for decoding and seeking
```

<br> **P-frames** (Predicted frames): A video frame that stores only the differences from a previous. It depends on I-frame for its reconstruction because it is a difference frame.
    
```
- Store only the difference from previous frames
- Depend on past I-frames or P-frames
- Require less data than I-frames
- Common in normal video playback
```
    
<br> **B-frames** (Bidirectional frames): a video frame that is reconstructed using information from both previous and next reference frames (I-frames or P-frames), allowing for higher compression efficiency.


```
- Use information from both previous and next frames
- Achieve the highest compression efficiency
- More complex to encode/decode
- May increase latency slightly
```

**By combining these frame types, video codecs significantly reduce file size while maintaining visual quality.**

---
## 4. Codecs vs Containers

### Codec (a compression and decompression technique)
- A video codec is about "how video frames are encoded are decoded". 

- Examples are: H.264, H.265 etc.

- A codec compresses frames and generates I, P, and B frames


### Container
- A container is a file format that stores video frames (i.e. coded output), audio stream, subtitles, metadata

- Example: MP4, MKV, AVI (older containers)

- In other words, code is algorithm to compress video frames into I,P,B frames; Container is how the frames and other infromation like audio etc. is to be stored in file.

---
## 5. Video resolutions (CIF, QCIF, HD, FHD, etc.)
These are early standardized low-resolution video formats used in video conferencing and surveillance systems when bandwidth was very limited.

- Video resolution defines the spatial size of each frame, i.e., how many pixels make up a single image in a video stream.

- Earlier formats like QCIF and CIF were designed for video conferencing and surveillance when bandwidth and processing power were very limited

- Modern formats like HD and Full HD (FHD) are used for high-quality streaming and display systems.

### Video resolution comparison (QCIF → 8K)

| Format | Resolution (W × H) | Total Pixels | Aspect Ratio | Era / Use Case |
|--------|--------------------|--------------|--------------|-----------------|
| QCIF   | 176 × 144          | ~25K         | 11:9         | Very low-bandwidth video calls, early mobile video |
| CIF    | 352 × 288          | ~101K        | 11:9         | Early video conferencing, CCTV systems |
| 4CIF   | 704 × 576          | ~405K        | 11:9         | Improved surveillance, broadcast systems |
| SD (480p) | 720 × 480       | ~345K        | 4:3 / 16:9   | DVD, legacy TV systems |
| HD (720p) | 1280 × 720      | ~921K        | 16:9         | Basic HD streaming |
| FHD (1080p) | 1920 × 1080   | ~2.07M       | 16:9         | Standard streaming, video conferencing |
| 2K (QHD) | 2560 × 1440      | ~3.69M       | 16:9         | High-end monitors, gaming, streaming |
| 4K (UHD) | 3840 × 2160      | ~8.29M       | 16:9         | Ultra HD streaming, cinema-grade content |
| 8K (UHD) | 7680 × 4320      | ~33.18M      | 16:9         | Experimental / premium displays, professional production |



---
## 6. Audio codecs

- Audio data can also be compressed, similar to video, to reduce storage size and bandwidth usage during transmission.

- Unlike video, which is a 2D signal (X and Y axes), audio is a 1D time-domain signal, so its compression algorithms are different and operate over time rather than spatial dimensions.

- Common audio codecs include formats like AAC and MP3, which exploit redundancy in sound signals and human hearing perception.

- Audio compression is outside the scope of this article and will be covered in a separate discussion.


---
## 7. Audio and video synchronization

- Audio and video are kept in sync using timestamps (PTS) attached to both streams.

- Each video frame and audio chunk has a time reference that tells the player when to play it.

- During playback, the player aligns audio and video on a common timeline.

- If one stream arrives earlier (common in streaming), the player uses a buffer to wait and match timing.

- The goal is simple: **lips, sound, and motion should match** naturally during playback.

- This topic is not covered in this article; it is mentioned for the sake of curious readers.


