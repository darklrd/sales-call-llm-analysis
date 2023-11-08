from google.cloud import storage

class StorageUploader:
    def __init__(self, bucket_name):
        self.storage_client = storage.Client()
        self.bucket_name = bucket_name

    def upload_blob(self, source_file_name, destination_blob_name):
        bucket = self.storage_client.bucket(self.bucket_name)
        blob = bucket.blob(destination_blob_name)
        with open(source_file_name, "rb") as audio_file:
            blob.upload_from_file(audio_file)
        print(f"Uploaded {source_file_name} to {destination_blob_name} in GCS.")
