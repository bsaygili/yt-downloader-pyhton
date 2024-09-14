from tkinter import *
import tkinter as tk
from tkinter import filedialog
from pytube import YouTube
import os
from moviepy.editor import AudioFileClip
from tkinter import messagebox

class Downloader():
    def __init__(self, master):
        self.master = master
        self.master.title("YouTube Downloader")
        self.master.geometry("600x450+500+200")
        self.master.config(bg="#f0f0f0")
        self.master.resizable(False, False)

        # Download location variable
        self.download_folder = None

        # Title Label
        title_label = Label(self.master, text="YouTube Downloader", font=('Arial', 24, 'bold'), bg="#f0f0f0", fg="#333")
        title_label.pack(pady=20)

        # URL Entry Frame
        url_frame = Frame(self.master, bg="#f0f0f0")
        url_frame.pack(pady=10)

        # URL Label
        label_url = Label(url_frame, text="Enter YouTube URL:", font=('Arial', 14), bg="#f0f0f0")
        label_url.grid(row=0, column=0, padx=10)

        # URL Entry
        self.url_entry = Entry(url_frame, width=40, font=('Arial', 14), bd=2, relief=SUNKEN)
        self.url_entry.grid(row=0, column=1, padx=10)
        self.url_entry.focus()

        # Choose Location Button
        location_button = Button(self.master, text="Choose Download Folder", font=('Arial', 12, 'bold'), bg="#2196F3", fg="white", width=25, 
                                 cursor="hand2", relief=FLAT, activebackground="#1e88e5", command=self.choose_location)
        location_button.pack(pady=10)

        # Download Type (MP3 or Video)
        self.download_choice = StringVar(value="mp3")

        download_type_frame = Frame(self.master, bg="#f0f0f0")
        download_type_frame.pack(pady=10)

        label_type = Label(download_type_frame, text="Download Format:", font=('Arial', 14), bg="#f0f0f0")
        label_type.grid(row=0, column=0, padx=10)

        mp3_radio = Radiobutton(download_type_frame, text="MP3", variable=self.download_choice, value="mp3", font=('Arial', 12), bg="#f0f0f0")
        mp3_radio.grid(row=0, column=1, padx=10)

        video_radio = Radiobutton(download_type_frame, text="Video", variable=self.download_choice, value="video", font=('Arial', 12), bg="#f0f0f0")
        video_radio.grid(row=0, column=2, padx=10)

        # Download Button
        download_button = Button(self.master, text="Download", font=('Arial', 16, 'bold'), bg="#4CAF50", fg="white", width=20, 
                                 cursor="hand2", relief=FLAT, activebackground="#45a049", command=self.download)
        download_button.pack(pady=20)

        # Status Label
        self.status_label = Label(self.master, text="Status: Waiting...", font=('Arial', 14), bg="#f0f0f0", fg="#333")
        self.status_label.pack(pady=10)

    def choose_location(self):
        """Opens a dialog for the user to choose the download folder."""
        self.download_folder = filedialog.askdirectory()
        if self.download_folder:
            self.status_label.config(text=f"Download Folder: {self.download_folder}", fg="blue")

    def download(self):
        url = self.url_entry.get()
        
        # Check if URL is empty
        if not url.strip():
            messagebox.showwarning("Input Error", "Please enter a YouTube URL.")
            return

        # Check if a download folder is chosen
        if not self.download_folder:
            messagebox.showwarning("Folder Error", "Please choose a download folder.")
            return

        # Get download choice (MP3 or Video)
        download_format = self.download_choice.get()

        self.status_label.config(text="Status: Downloading...", fg="blue")
        self.master.update()  # Update the UI immediately

        try:
            yt = YouTube(url)

            if download_format == "mp3":
                # Download and convert to MP3
                audio_stream = yt.streams.filter(only_audio=True).first()
                audio_file = audio_stream.download(output_path=self.download_folder)

                # Convert to mp3 using moviepy
                mp3_file = audio_file.replace('.mp4', '.mp3')
                clip = AudioFileClip(audio_file)
                clip.write_audiofile(mp3_file)
                clip.close()

                # Delete the .mp4 file after conversion
                os.remove(audio_file)

                self.status_label.config(text="Status: Downloaded and converted to MP3 successfully!", fg="green")
            else:
                # Download Video
                video_stream = yt.streams.get_highest_resolution()
                video_stream.download(output_path=self.download_folder)

                self.status_label.config(text="Status: Video downloaded successfully!", fg="green")

            self.url_entry.delete(0, tk.END)
        except Exception as e:
            self.status_label.config(text=f"Status: Download failed. Error: {str(e)}", fg="red")
            self.url_entry.delete(0, tk.END)

if __name__ == "__main__":
    master = tk.Tk()
    app = Downloader(master)
    master.mainloop()
