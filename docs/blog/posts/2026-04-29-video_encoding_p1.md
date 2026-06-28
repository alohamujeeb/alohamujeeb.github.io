---
date: 
  created: 2026-04-29
  posted:  2025-04-30
author:
  name: Mujeeb
  description: Creator
readtime: 15

categories: 
  - Multimedia
  - Video
tags:
  - YUV
  - JPEG
  - PNG
  - JPG
  - RGB
  - BMP
---

# <font color='green'>Video Encoding – Part 1 (Image Formats)</font>

In this article, we look at how images are actually represented in digital systems—from raw sensor data to common formats like RGB, YUV, JPEG, and PNG.
Before we even talk about video, we need to understand how a single frame is stored, because video is just a sequence of these frames.

<!-- more -->
This is where image formats become the foundation of everything in video encoding.

---
## 1. Rraw image representation (BMP)

- An image is fundamentally a grid of pixels, where each pixel stores visual information about a single point in the scene. These pixels are either grayscale (black & white) or color (RGB) depending on how the image is represented.

- In a grayscale image, each pixel stores a single value (typically 1 byte) representing intensity, ranging from black to white.

- In a color image, each pixel stores three values corresponding to the intensities of the primary colors Red, Green, and Blue (RGB).

- Therefore, the total uncompressed image size is typically W × H × 1 for grayscale and W × H × 3 for RGB images.

- A common file format used to store this raw pixel data directly is BMP, which stores pixel values with minimal or no compression, making it large in size but simple in structure.


### BMP size table

| Resolution | Pixels (W×H)      | Format     | Channels | Bytes per pixel | Total size |
|------------|-------------------|------------|----------|------------------|------------|
| 360p       | 640 × 360         | Grayscale  | 1        | 1 byte           | 230,400 bytes (~225 KB) |
| 360p       | 640 × 360         | RGB        | 3        | 3 bytes          | 691,200 bytes (~675 KB) |
| 720p       | 1280 × 720        | Grayscale  | 1        | 1 byte           | 921,600 bytes (~900 KB) |
| 720p       | 1280 × 720        | RGB        | 3        | 3 bytes          | 2,764,800 bytes (~2.64 MB) |
| 1080p      | 1920 × 1080       | Grayscale  | 1        | 1 byte           | 2,073,600 bytes (~2.0 MB) |
| 1080p      | 1920 × 1080       | RGB        | 3        | 3 bytes          | 6,220,800 bytes (~5.9 MB) |
| 2K         | 2560 × 1440       | Grayscale  | 1        | 1 byte           | 3,686,400 bytes (~3.5 MB) |
| 2K         | 2560 × 1440       | RGB        | 3        | 3 bytes          | 11,059,200 bytes (~10.5 MB) |
| 4K         | 3840 × 2160       | Grayscale  | 1        | 1 byte           | 8,294,400 bytes (~7.9 MB) |
| 4K         | 3840 × 2160       | RGB        | 3        | 3 bytes          | 24,883,200 bytes (~23.7 MB) |

Note: some extra information is also added called the header (if stored in a file such as .bmp)

---
## 2. Compressed image (JPEG and PNG)
Raw images are very large in size because they store pixel data directly without compression. This makes them expensive in terms of both storage and transmission bandwidth, especially for high-resolution images.

- To solve this, images are typically compressed using standard encoding algorithms that reduce file size while preserving visual quality.

- Some of the most common image compression formats are **JPEG** and **PNG**.

- JPEG is a lossy compression format and is commonly used for both color (RGB) and grayscale images, making it highly efficient for natural photographs.

- PNG is a lossless compression format and supports RGBA images, meaning it can store Red, Green, Blue, and Alpha (transparency) channels without losing any information.


### JPEG Image Size Comparison (Lossy Compression)

| Resolution | Pixels (W×H) | Format     | Channels | Size Formula        | Raw RGB Size | JPEG Size (typical) |
|------------|-------------|------------|----------|---------------------|--------------|----------------------|
| 360p       | 640×360     | Grayscale  | 1        | W × H × 1           | 230 KB       | 30 – 100 KB         |
| 360p       | 640×360     | RGB        | 3        | W × H × 3           | 675 KB       | 50 – 150 KB         |
| 720p       | 1280×720    | Grayscale  | 1        | W × H × 1           | 900 KB       | 100 – 300 KB        |
| 720p       | 1280×720    | RGB        | 3        | W × H × 3           | 2.64 MB      | 200 – 600 KB        |
| 1080p      | 1920×1080   | Grayscale  | 1        | W × H × 1           | 2.07 MB      | 200 – 700 KB        |
| 1080p      | 1920×1080   | RGB        | 3        | W × H × 3           | 5.93 MB      | 400 KB – 1.5 MB     |
| 2K         | 2560×1440   | Grayscale  | 1        | W × H × 1           | 3.5 MB       | 400 KB – 1.5 MB     |
| 2K         | 2560×1440   | RGB        | 3        | W × H × 3           | 10.5 MB      | 800 KB – 3 MB       |
| 4K         | 3840×2160   | Grayscale  | 1        | W × H × 1           | 7.9 MB       | 1 – 4 MB            |
| 4K         | 3840×2160   | RGB        | 3        | W × H × 3           | 23.7 MB      | 2 – 8 MB            |


### PNG Image Size Comparison (Lossless Compression)

| Resolution | Pixels (W×H) | Format     | Channels | Size Formula        | Raw RGB Size | PNG Size (lossless range) |
|------------|-------------|------------|----------|---------------------|--------------|----------------------------|
| 360p       | 640×360     | Grayscale  | 1        | W × H × 1           | 230 KB       | 150 – 500 KB              |
| 360p       | 640×360     | RGB        | 3        | W × H × 3           | 675 KB       | 200 – 600 KB              |
| 360p       | 640×360     | RGBA       | 4        | W × H × 4           | 900 KB       | 250 – 800 KB              |
| 720p       | 1280×720    | Grayscale  | 1        | W × H × 1           | 900 KB       | 500 KB – 1.5 MB           |
| 720p       | 1280×720    | RGB        | 3        | W × H × 3           | 2.64 MB      | 800 KB – 2.5 MB           |
| 720p       | 1280×720    | RGBA       | 4        | W × H × 4           | 3.52 MB      | 1 – 3 MB                  |
| 1080p      | 1920×1080   | Grayscale  | 1        | W × H × 1           | 2.07 MB      | 1 – 4 MB                  |
| 1080p      | 1920×1080   | RGB        | 3        | W × H × 3           | 5.93 MB      | 1.5 – 5.5 MB              |
| 1080p      | 1920×1080   | RGBA       | 4        | W × H × 4           | 7.91 MB      | 2 – 7 MB                  |
| 2K         | 2560×1440   | Grayscale  | 1        | W × H × 1           | 3.5 MB       | 2 – 7 MB                  |
| 2K         | 2560×1440   | RGB        | 3        | W × H × 3           | 10.5 MB      | 3 – 10 MB                 |
| 2K         | 2560×1440   | RGBA       | 4        | W × H × 4           | 14.0 MB      | 4 – 12 MB                 |
| 4K         | 3840×2160   | Grayscale  | 1        | W × H × 1           | 7.9 MB       | 5 – 18 MB                 |
| 4K         | 3840×2160   | RGB        | 3        | W × H × 3           | 23.7 MB      | 7 – 25 MB                 |
| 4K         | 3840×2160   | RGBA       | 4        | W × H × 4           | 31.6 MB      | 10 – 30 MB                |

---
## 3. Typical size reduction

- JPEG → big reduction, loses detail
- PNG → small/moderate reduction, preserves detail


| Format | Size vs RAW | What it means |
|--------|------------|---------------|
| JPEG   | ~10× to 30× smaller | Lossy compression (removes visual detail) |
| PNG    | ~1× to 5× smaller (sometimes larger than RAW) | Lossless compression (preserves all data) |

---
## 4. Typical uses of JPEG and PNG

JPEG is used when you want small file size for natural images.

- Photos (phone camera images)
- Web images (blogs, websites)
- Social media uploads
- Storage of large photo libraries

PNG is used when you need perfect quality preservation.

- UI graphics (icons, buttons)
- Logos
- Text in images (screenshots)
- Diagrams / charts
- images with transparency (alpha channel)

**Even though PNG is lossless (as raw BMP image), in most cases, it is much smaller is size.**

---
## 5. YUV format (alternate to RGB)

- YUV is a way to represent images where color is split into:

	Y = Luma (brightness)
	U = Chrominance (blue difference)
	V = Chrominance (red difference)

- So instead of storing **R G B** per pixel, we store
	**Y + U + V**
	

### What each channel (YUV) means?

- Y (luma): brightness / grayscale structure of the image
- U: how “blue-ish” or “yellow-ish” the color is
- V: how “red-ish” or “green-ish” the color is

Note: Brightness is separated from color.

### Why use YUV instead of RGB

- In RGB, Every pixel is stored as R, G, B
- But human vision does NOT perceive all three equally
- **Problem:** RGB mixes brightness + color together in each channel, which is inefficient for compression and video.

- Human vision is very sensitive to brightness (detail, edges) and less sensitive to fine color changes

- So instead of:
	R G B (all equally important)
	<br>We get:"
		<br>**Y (important structure)**
		<br>U,V (color info)

---
## 6. YUV advantages
We use YUV instead of RGB because it separates brightness from color, matching human vision and enabling much more efficient compression—especially in video systems; Following are more details.


### i) Compression becomes easier
We can reduce color resolution:

- keep full Y
- reduce U and V (e.g. YUV420) (to be convered in more details later)

### ii) Video becomes efficient
Most video codecs assume:

- brightness matters most
- color can be compressed more

**(more on video codecs in part of this series)**


### iii) Better signal separation

Processing becomes easier:

- sharpening → apply to Y only
- color correction → apply to U/V only

---
## 7. Images from camera (YUV420 vs MJPG)

- A camera when connected to a computer provides video as a sequence of images (frames) at a fixed frame rate such as 30 fps, 15 fps, etc.

- These frames are independent images (in most camera output modes), meaning each frame is captured and transmitted separately; Not heavily interdependent like in encoded video formats (e.g., H.264) which will be described in part 2 of this series.

- Most cameras (not all) support two main types of image streams at this stage (before video encoding happens)
	
	<br>i) **YUV420:** a modified form of the YUV color representation (i.e., not RGB). It stores brightness (Y) at full resolution and color components (U and V) at reduced resolution, making it efficient for real-time processing and video pipelines.
	
	<br>ii) **MJPEG (Motion JPEG):** where each frame is a JPEG-compressed image (typically RGB for color cameras). Each frame is compressed independently using the JPEG algorithm.


###  YUV420 vs MJPEG from camera

- Imagine that a camera is providing images: (1000×1000, 30 fps, 1 sec)

| Format | Type | Lossy? | Representation | Size per frame | Size per second | Key idea |
|--------|------|--------|----------------|----------------|-----------------|----------|
| YUV420 | Raw video format | ❌ No (representation only) | Y + U/2 + V/2 (chroma subsampled) | ~1.5 MB | ~45 MB | Fixed bandwidth, no compression |
| MJPEG  | Compressed video stream | ✅ Yes | JPEG per frame (RGB compressed) | ~0.2 – 1.0 MB | ~6 – 30 MB | Compression depends on image content |

- depending on our application, we read input either in YUV420 or MJPEG 

- Some camera may have only one format.

Note: See an article [video for linux (v4l2)](https://alohamujeeb.com/programming/media-streaming/v4l.html) for more details

--- 
## 8. What is next?
- In the next article in this series, we will move from image representation to video conversion, covering how individual image frames are combined into a continuous stream.

- We'll see how formats like YUV and MJPEG fit into real video pipelines. 

- We will also look at the core concepts behind video encoding along with some practical, system-level considerations.

---
## Some references

- [Video for Linux (v4l2)](https://alohamujeeb.com/programming/media-streaming/v4l.html)



