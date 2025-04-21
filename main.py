import whisper 
import os
import pandas as pd
import re


def process_files():
	model = whisper.load_model("small") 
	audio_file_path = "/Users/jmontag/Desktop/bcog200/final_project/audio"
	output_path = "/Users/jmontag/Desktop/bcog200/final_project"
	audio_files = os.listdir(audio_file_path)

	whisper_df_list = []
	for audio_file in audio_files:
		if audio_file.endswith('.wav') or audio_file.endswith('.mp3'):
			print(f'Processing {audio_file}')
			audio_path = os.path.join(audio_file_path, audio_file)
			result = model.transcribe(audio_path, fp16=False)

			#Lists timestamps for each utterance
			#Had to look up how to get segment time stamps for Whisper
			segments = result.get("segments", [])
			rows = [{
			"start": round(seg["start"], 2),
			"end": round(seg["end"], 2),
			"utterance": seg["text"].strip()
			} for seg in segments]

			#Adds df into list 
			whisper_df = pd.DataFrame(rows)
			whisper_df_list.append(whisper_df)

			#Saves files as a csv
			file_name = os.path.splitext(audio_file)[0]
			csv_output_path = os.path.join(output_path, f'{file_name}_transcript.csv')
			whisper_df.to_csv(csv_output_path, index=False)
			print(f'Saved transcript to {csv_output_path}')

	return whisper_df_list

def load_expert_files():
	expert_file_path = '/Users/jmontag/Desktop/bcog200/final_project/expert_transcripts'
	expert_files = os.listdir(expert_file_path)
	expert_list = [pd.read_csv(os.path.join(expert_files, file_name)) for file_name in expert_files if file_name.endswith('.csv')]
	return expert_list

def clean_transcript(df):
    df['utterance'] = df['utterance'].apply(lambda x: re.sub('[^A-Za-z0-9]', ' ', str(x)).strip()) #used stackflow to get this part of the code
    df['word_count'] = df['utterance'].apply(lambda x: len(x.split()))
    df['unique_word_count'] = df['utterance'].apply(lambda x: len(set(x.split())))
    return df
	
def levenshtein_distance():
	pass

def main():
	whisper_dfs = process_files()
	exper_dfs = load_expert_files()
	whisper_dfs = [clean_transcript(df) for df in whisper_dfs]
	expert_dfs = [clean_transcript(df) for df in exper_dfs]
	word_count(cleaned_strings)
	unq_word_count(cleaned_strings)
	cleaned_strings = clean_transcript(df['utterance']).strip()

if __name__ == "__main__":
    main()