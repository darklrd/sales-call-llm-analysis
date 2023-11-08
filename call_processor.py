import os
import time
from audio_downloader import AudioDownloader
from audio_converter import AudioConverter
from storage_uploader import StorageUploader
from speech_to_text import SpeechToText
from dotenv import load_dotenv

load_dotenv()

BUCKET_NAME = os.getenv('BUCKET_NAME')
AUDIO_FILE_MP3 = os.getenv('AUDIO_FILE_MP3', 'data/audio.mp3')
AUDIO_FILE_FLAC = os.getenv('AUDIO_FILE_FLAC', 'data/audio.flac')
SPEECH_TO_TEXT_PROJECT = os.getenv('SPEECH_TO_TEXT_PROJECT')

class CallProcessor:
    def __init__(self, row):
        self.row = row
        self.url = row['recording_url']

    def process_call(self):
        downloader = AudioDownloader(self.url)
        downloader.download(AUDIO_FILE_MP3)

        AudioConverter.mp3_to_flac(AUDIO_FILE_MP3, AUDIO_FILE_FLAC)

        uploader = StorageUploader(BUCKET_NAME)
        uploader.upload_blob(AUDIO_FILE_FLAC, 'audio.flac')

        time.sleep(5)  # Wait before transcription (as earlier)

        transcriber = SpeechToText(SPEECH_TO_TEXT_PROJECT)
        transcription = transcriber.transcribe(f"gs://{BUCKET_NAME}/audio.flac")
        return transcription
