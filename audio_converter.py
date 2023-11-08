import subprocess

class AudioConverter:
    @staticmethod
    def mp3_to_flac(input_path, output_path):
        # command = ["ffmpeg", "-y", "-i", input_path, "-vn", output_path]
        command = ["ffmpeg", "-y", "-i", input_path, "-vn", "-acodec", "flac", "-ar", "16000", "-af", "acompressor=threshold=0.089:detection=peak:ratio=9:makeup=9", output_path]
        subprocess.run(command)
        print("Converted MP3 to FLAC format.")
