import requests

class AudioDownloader:
    def __init__(self, url):
        self.url = url

    def download(self, destination_path):
        response = requests.get(self.url)
        with open(destination_path, "wb") as audio_file:
            audio_file.write(response.content)
        print(f"Downloaded audio from {self.url} to {destination_path}")
