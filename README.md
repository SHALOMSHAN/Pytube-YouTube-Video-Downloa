# Pytube YouTube Video Downloader

## Introduction

Pytube is a Python library for downloading YouTube videos. It provides a simple and easy-to-use interface to download YouTube videos by using the YouTube video's URL. Pytube offers various features like downloading videos in different resolutions and formats, downloading only the audio or video streams of the video, and downloading only a part of the video by specifying the start and end time.

Pytube is an open-source library and is available on PyPI, the Python Package Index, which makes it easy to install and use in your Python projects. Pytube uses Python's built-in libraries like 'urllib' and 'http.client' for the HTTP requests, and it uses the 'lxml' library for parsing the HTML content of YouTube pages.

With Pytube, you can download YouTube videos programmatically and use them in your projects. This can be useful for tasks like creating a video dataset for machine learning or downloading videos for offline viewing.

## Installing Dependencies

  ```
    pip install pytube
  ```

## Scripts Explained

There are 2 following simple projects in it.

- 0-basic-download-script
- 1-multi-download-script



### basic-download-script

This simple project has two scripts in it, those can be used to download videos with and without resolutions.

#### To download videos

```python
import pytube

link = input("Enter the link: ")

print("Downloading....")

pytube.YouTube(link).streams.first().download()

print("The video has been downloaded!")
```

#### To download videos with resolutions

```python
import pytube

link = input("Enter the link: ")

res_data = input("Please enter the resolution: ")

print("Downloading....")

pytube.YouTube(link).streams.filter(res=res_data).first().download()

print("The video has been downloaded!")
```

### multi-download-script

This project is aimed to download multiple videos at once with a text file, we have to enter all of the urls of the videos that we need to download in the "download-list-file.txt" file that is exist in this folder.

```Python
import os
import pytube


with open("download-list-file.txt") as main_file:
	for line in main_file:
		print("Downloading...")
		pytube.YouTube(line).streams.filter(res='240p').first().download()


print("All videos have been downloaded")
```

Any Questions? | Conduct Me
---

* [Linkedin Profile](https://www.linkedin.com/in/shalomshan-selvakumar-423aaa1aa/)
* [Facebook Page](https://web.facebook.com/selvakumar.shalomshan)
* [Twitter Profile](https://mobile.twitter.com/SHALOMSHANS)
* [Instagram Profile](https://www.instagram.com/shalomshanselvakumar/)
* [Youtube Channel](https://www.youtube.com/channel/UCeQfTqz1hxhe_Lt37I2JLDg)
