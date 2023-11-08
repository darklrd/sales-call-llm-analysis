import csv

class CallCsvParser:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_rows(self):
        with open(self.file_path, 'r') as file:
            reader = csv.DictReader(file)
            rows = [row for row in reader]
        return rows

    def ensure_transcript_column(self):
        rows = self.read_rows()
        if 'transcript' not in rows[0]:
            # Add 'transcript' key with an empty value to each row
            for row in rows:
                row['transcript'] = ''
                row['key_insights'] = ''
                row['english_translation'] = ''
            self.write_rows(rows)

    def append_transcript(self, row, transcript):
        row['transcript'] = transcript

    def append_key_insights(self, row, key_insights):
        row['key_insights'] = key_insights

    def append_english_translation(self, row, english_translation):
        row['english_translation'] = english_translation

    def write_rows(self, rows):
        with open(self.file_path, 'w', newline='') as file:
            fieldnames = list(rows[0].keys())
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for row in rows:
                writer.writerow(row)

