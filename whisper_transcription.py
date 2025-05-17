import whisper 
import os
import pandas as pd

def process_files(input_path, output_folder):
	'''
	Processes audio files through Whisper and saves the transcripts as csv files in a folder.

	Args:
		input_path(str): path to the folder containing .wav or .mp3 files
		output_folder(str): path to where the csv files will be saved to
	'''
	model = whisper.load_model("large") 
	audio_files = os.listdir(input_path)
	os.makedirs(output_folder, exist_ok = True)

	for audio_file in audio_files:
		if audio_file.endswith('.wav') or audio_file.endswith('.mp3'):
			print(f'Processing {audio_file}')
			audio_path = os.path.join(input_path, audio_file)
			result = model.transcribe(audio_path, fp16=False, language="en")

			#Lists timestamps for each utterance
			#Had to look up how to get segment time stamps for Whisper
			segments = result.get("segments", [])
			rows = [{
			"start": round(seg["start"], 2),
			"end": round(seg["end"], 2),
			"utterance": seg["text"].strip()
			} for seg in segments]

			whisper_df = pd.DataFrame(rows)
			file_name = os.path.splitext(audio_file)[0]
			csv_output_path = os.path.join(output_folder, f'{file_name}.csv')
			whisper_df.to_csv(csv_output_path, index=False)
			print(f'Saved transcript to {csv_output_path}')

def main():
    input_path = os.path.join("audio")
    output_folder = os.path.join("transcripts", "whisper_transcripts")
    whisper_dfs = process_files(input_path, output_folder)


if __name__ == "__main__":
    main()