# YouTube Downloader

This is a simple YouTube Downloader application built using Python's Tkinter library for the graphical interface and the **Pytube** and **MoviePy** libraries for downloading and converting YouTube videos. The downloader allows users to download either the audio (as MP3) or the video from a YouTube link and choose the destination folder for the download.

## Features

- **Download YouTube Videos**: Download the highest quality video available.
- **Download MP3**: Extract the audio from a YouTube video and save it as an MP3 file.
- **Custom Download Location**: Users can choose where to save the downloaded files.
- **User-Friendly Interface**: A simple GUI for ease of use, with clear status updates.

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- **Python 3.6+**
- **pip** (Python package installer)
- **ffmpeg** (for audio conversion, needed by MoviePy):
  - You can install `ffmpeg` by following instructions [here](https://ffmpeg.org/download.html).

## Installation

1. **Clone this repository**:

   ```bash
   git clone https://github.com/bsaygili/yt-downloader-pyhton.git
   cd yt-downloader-pyhton   
   ```

2. **Install required libraries**:

   Run the following command to install the required Python libraries:

   ```bash
   pip install -r requirements.txt
   ```


3. **Install ffmpeg**:
   - Download and install **ffmpeg** from [ffmpeg.org](https://ffmpeg.org/download.html).
   - After installation, ensure `ffmpeg` is added to your system's PATH.

## Usage

1. Run the application using the following command:

   ```bash
   python script.py
   ```

2. **Choose Download Options**:
   - Enter the YouTube URL in the text box.
   - Select whether you want to download the **MP3** (audio only) or the **Video**.
   - Click **Choose Download Folder** to select the folder where you want the file to be saved.

3. **Download**:
   - Click the **Download** button, and the status label will update to reflect the progress.
   - Once the download and conversion (if MP3) are complete, you will see a success message.

## Example

### Downloading an MP3

1. Enter the URL of the YouTube video you want to download.
2. Select **MP3** as the download option.
3. Choose a folder where the MP3 file will be saved.
4. Click **Download**.

### Downloading a Video

1. Enter the URL of the YouTube video you want to download.
2. Select **Video** as the download option.
3. Choose a folder where the video file will be saved.
4. Click **Download**.

## Troubleshooting

Here are common issues and their fixes:

### 1. **`get_throttling_function_name: couldn't find match` Error**

This is a common issue when YouTube changes its internal API. Follow these steps:

- **Solution**: [here](https://stackoverflow.com/a/71903013)


### 2. **Unsupported YouTube URL**

- **Solution**: Make sure the YouTube URL is correctly formatted. Only standard YouTube video URLs are supported (e.g., `https://www.youtube.com/watch?v=video_id`).

### 3. **No Download Folder Selected**

- **Solution**: If you get an error saying no folder is selected, ensure you choose a valid download folder by clicking **Choose Download Folder** before starting the download process.

## Contributing

Feel free to submit issues or pull requests to improve the project. Contributions are welcome!

---
