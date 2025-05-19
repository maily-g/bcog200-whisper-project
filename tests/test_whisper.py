import pandas as pd
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scripts.analysis import clean_transcript, align_and_evaluate
    
def test_clean_transcript():
    df = pd.DataFrame({'utterance': ["hello world!", "Nice to meet you"],
                       'start': [0, 1],
                       'end': [1, 2]})
    cleaned = clean_transcript(df, output_path=".", key="0", file_type="test")
    assert cleaned['word_count'].tolist() == [2, 4]
    assert cleaned['unique_word_count'].tolist() == [6, 6]

def test_align_and_evaluate():
    whisper_df = pd.DataFrame({'utterance': ["nice job"],
                               'start': [0],
                               'end': [5]})
    expert_df = pd.DataFrame({'utterance': ["nice", "job"],
                               'start': [1, 2],
                               'end': [2, 3]})
    aligned = align_and_evaluate(whisper_df, expert_df)
    assert aligned.iloc[0]['WER'] is not None 
    assert "nice job" in aligned.iloc[0]['expert_utterance']

def test_reuse_utterances():
    whisper_df = pd.DataFrame({'utterance': ["nice job"] * 4,
                               'start': [0, 10, 20, 30],
                               'end': [5, 15, 25, 35]})
    expert_df = pd.DataFrame({'utterance': ["nice job"] * 4,
                               'start': [1, 11, 21, 31 ],
                               'end': [2, 12, 22, 32 ]})
    aligned = align_and_evaluate(whisper_df, expert_df)
    used = aligned["whisper_utterance"].value_counts().get("nice job", 0)
    assert used == 2 
    
    