import os 
import pandas as pd

def clean_expert_transcripts(input_path):
	'''
	Function that removes rows of utterances that contain no speech for csv files in a specified directory.

	Args:
		input_path(str): path to expert transcript directory
	'''
	output_folder = os.path.join(input_path, "cleaned")
	os.makedirs(output_folder, exist_ok = True)

	for filename in os.listdir(input_path):
		if not filename.endswith(".csv"):
			continue 

		file_path = os.path.join(input_path, filename)
		df = pd.read_csv(file_path)


		df["utterance"] = df["utterance"].astype(str).str.strip()
		df = df[~df["utterance"].isin(["", "0"])]

		cleaned_path = os.path.join(output_folder, filename)
		df.to_csv(cleaned_path, index = False)
		print(f"Saved new file to: {cleaned_path}")

def main():
    input_path = os.path.join("transcripts", "expert_transcripts")
    clean_expert_transcripts(input_path) 

if __name__ == "__main__":
    main()
