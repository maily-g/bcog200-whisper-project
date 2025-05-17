import os
import pandas as pd
import re
from collections import Counter

def load_files(path):
    '''
    This function reads in and loads all csv files from a directory into a dictionary of dataframes. 

    Args: 
        path(str): directory path to the location of csv files

    Returns:
        dict: dictionary mapping file base names to dataframes
    '''
    files = os.listdir(path)
    df_dict = {os.path.splitext(f)[0]: pd.read_csv(os.path.join(path, f)) for f in files if f.endswith('.csv')}
    return df_dict

def clean_transcript(df, output_path, key, file_type=None):
    '''
    Cleans transcripts on the dataframes and computes total word and unique word counts.

    Args:
        df(pd.DataFrame): dataframe containing 'utterance', 'start', and 'end' columns
        output_path(str): directory to save the cleaned files
        key(str): file ID for naming the file output
        role(str, optional): labels the output file based on the type of file; 'whisper' or 'expert'

    Returns:
        pd.DataFrame: cleaned dataframes with added counts 
    '''
    df['utterance'] = df['utterance'].apply(lambda x: re.sub(r'[^A-Za-z0-9]', ' ', str(x)).lower().strip())
    df['word_count'] = df['utterance'].apply(lambda x: len(x.split()))
    all_words = " ".join(df['utterance'].dropna().astype(str).str.lower())
    df['unique_word_count'] = len(set(all_words))
    os.makedirs(output_path, exist_ok=True)
    df.to_csv(os.path.join(output_path, f'{key}_{file_type}_final.csv'), index=False)
    return df

def levenshtein_distance(u1, u2):
    '''
    Function that computes word-level Levenshtein Distance (LD) between two strings.

    Args: 
        u1(str): First utterance
        u2(str): Second utterance
    
    Returns: 
        int: word-level LD 
    '''
    #this function uses third-party code from stack overflow modified to fit this project
    u1_words = str(u1).split()
    u2_words = str(u2).split()

    len_u1 = len(u1_words)
    len_u2 = len(u2_words)

    dist = [[0] * (len_u2 + 1) for i in range(len_u1 + 1)]

    for i in range(len_u1 + 1):
        dist[i][0] = i
    for j in range(len_u2 + 1):
        dist[0][j] = j
    for i in range(1, len_u1 + 1):
        for j in range(1, len_u2 + 1):
            cost = 0 if u1_words[i - 1] == u2_words[j - 1] else 1
            dist[i][j] = min(dist[i-1][j] + 1, dist[i][j-1] + 1, dist[i-1][j-1] + cost)

    return dist[len_u1][len_u2]

def align_and_evaluate(whisper_df, expert_df):
    '''
    This function aligns whisper and expert utterances by overlapping start and end times and computes 
    word error rates (WER) for each pair of utterances.

    Args:
        whisper_df(pd.DataFrame): whisper trasncript with 'utterance', 'start', and 'end' columns
        expert_df(pd.DataFrame): expert transcript with 'utterance', 'start', and 'end' columns 

    Returns:
        pd.DataFrame: merged dataframe with WER and LD scores
    '''
    results = []
    whisper_df = whisper_df[['utterance', 'start', 'end']].dropna()
    expert_df = expert_df[['utterance', 'start', 'end']].dropna()
    matched_indices = set()
    whisper_counts = Counter()

    for idx, whisper_row in whisper_df.iterrows():
        whisper_text = whisper_row['utterance']
        whisper_start, whisper_end = whisper_row['start'], whisper_row['end']

        # does not match repeated Whisper utterances that had more than 2 instances
        if whisper_counts[whisper_text] >= 2:
            continue
        whisper_counts[whisper_text] += 1

        overlaps = expert_df[(expert_df['end'] > whisper_start) & (expert_df['start'] < whisper_end)]
        matched_indices.update(overlaps.index)

        expert_text = " ".join(overlaps['utterance'])
        expert_wc = len(expert_text.split())

        ld = levenshtein_distance(expert_text, whisper_text) 
        wer = ld / expert_wc if expert_text and expert_wc > 0 else None

        results.append({
            "whisper_start": whisper_start,
            "whisper_end": whisper_end,
            "expert_utterance": expert_text,
            "whisper_utterance": whisper_text,
            "levenshtein_distance": ld,
            "WER": wer,
            "expert_word_count": expert_wc,
        })

    # Appends the unmatched expert utterances that did not align with whisper
    for i, row in expert_df.iterrows():
        if i not in matched_indices:
            utt = row['utterance']
            wc = len(utt.split())
            uwc = len(set(utt.split()))
            results.append({
                "whisper_start": None,
                "whisper_end": None,
                "expert_utterance": utt,
                "whisper_utterance": None,
                "levenshtein_distance": None,
                "WER": None,
                "expert_word_count": wc,
            })

    return pd.DataFrame(results)

def main():
    whisper_path = os.path.join("transcripts", "whisper_transcripts")
    expert_path = os.path.join("transcripts", "expert_transcripts", "cleaned")
    cleaned_output_path = os.path.join("cleaned_individual")

    whisper_dict = load_files(whisper_path)
    expert_dict = load_files(expert_path)
    match_files = set(whisper_dict) & set(expert_dict)

    for key in sorted(match_files):
        whisper_df = clean_transcript(whisper_dict[key], cleaned_output_path, key, file_type='whisper')
        expert_df = clean_transcript(expert_dict[key], cleaned_output_path, key, file_type='expert')
        aligned_df = align_and_evaluate(whisper_df, expert_df)
        merged_path = os.path.join(cleaned_output_path, f"merged_{key}.csv")
        aligned_df.to_csv(merged_path, index=False)
        print(f"Completed file: {key}")

if __name__ == "__main__":
    main()
