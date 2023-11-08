from google.cloud import speech_v2
from google.api_core import client_options

class SpeechToText:
    def __init__(self, project_id):
        self.location = 'asia-southeast1'
        self.api_endpoint = f"{self.location}-speech.googleapis.com"
        self.client_options_var = client_options.ClientOptions(api_endpoint=self.api_endpoint)
        self.client = speech_v2.SpeechClient(client_options=self.client_options_var)
        self.project_id = project_id
        

    def transcribe(self, gcs_uri):
        
        diarization_config = speech_v2.SpeakerDiarizationConfig(
            min_speaker_count=2,
            max_speaker_count=6,
        )
        
        config = speech_v2.RecognitionConfig(
            auto_decoding_config=speech_v2.AutoDetectDecodingConfig(),
            language_codes=["te-IN","en-IN"],
            model="chirp",
            features=speech_v2.RecognitionFeatures(
                enable_word_time_offsets=False,
                enable_automatic_punctuation=True,
                # diarization_config=diarization_config,
            ),
        )

        file_metadata = speech_v2.BatchRecognizeFileMetadata(uri=gcs_uri)
        request = speech_v2.BatchRecognizeRequest(
            recognizer=f"projects/{self.project_id}/locations/{self.location}/recognizers/_",
            config=config,
            files=[file_metadata],
            recognition_output_config=speech_v2.RecognitionOutputConfig(
                inline_response_config=speech_v2.InlineOutputConfig(),
            ),
        )

        operation = self.client.batch_recognize(request=request)
        print("Waiting for operation to complete...")
        response = operation.result(timeout=600)
        print(response.results[gcs_uri].transcript)

        transcript = ""
        for result in response.results[gcs_uri].transcript.results:
            if result.alternatives:
                transcript += result.alternatives[0].transcript + " \n\n"
            # else:
            #     print("No transcription alternatives found.")
        return transcript

        return response.results[gcs_uri].transcript