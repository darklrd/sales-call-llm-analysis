import os
from dotenv import load_dotenv
import openai
from call_csv_parser import CallCsvParser
from call_processor import CallProcessor
from transcript_analyser import TranscriptAnalyser
from transcript_english_translator import TranscriptEnglishTranslator

if __name__ == "__main__":
    load_dotenv()  # Read local .env file

    parser = CallCsvParser('data/call.csv')
    parser.ensure_transcript_column()
    rows = parser.read_rows()
    
    count = 0
    for row in rows:
        if True and int(row['call_duration']) > 5_000 and not row.get('transcript', '').strip():
            print(row)
            processor = CallProcessor(row)
            transcript = processor.process_call()
            parser.append_transcript(row, transcript)
            count += 1
            parser.write_rows(rows)
            if count == 100:
                break
        if True and row.get('transcript', '').strip() and not row.get('key_insights', '').strip():
            analyser = TranscriptAnalyser(os.environ['OPENAI_API_KEY'])
            analyser_text = analyser.analyse(row.get('transcript', '').strip())
            print(analyser_text)
            parser.append_key_insights(row, analyser_text)
            count += 1
            parser.write_rows(rows)
            if count == 200:
                break
        if True and row.get('transcript', '').strip() and not row.get('english_translation', '').strip():
            translator = TranscriptEnglishTranslator(os.environ['OPENAI_API_KEY'])
            try:
                analyser_text = translator.translate(row.get('transcript', '').strip())
            except openai.error.InvalidRequestError as e:
                if "maximum context length" in str(e):
                    analyser_text = translator.split_and_translate(row.get('transcript', '').strip())
                else:
                    raise
            print(analyser_text)
            parser.append_english_translation(row, analyser_text)
            count += 1
            parser.write_rows(rows)
            if count == 20:
                break
        #parser.write_rows(rows)

    

   
