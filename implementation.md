Implementation and Breakdown of Code
- A process__audio_files function to load in and transcribe 10 minute clips of audio files through Whisper that will save them into a csv file.
    This has been completed and is shown in main.py.
- A load_expert_files function that will load in the corresponding 10 minute clips of human coded files and will save them into a csv file like the Whisper csv files.
    Implemented
- A clean_transcript function that will remove any punctation and symbols from the text
    Implemented
- A word_count function that will calculate the total number of words per utterance.
    Implemented.
- A unique_words function that will calculate the total number of unique words per utterance.
    Implemented.
- A levenshthein_distance function that will calculate the levenshtein distance which is the number of differences between the human and Whisper utterances.
    Still pending.
- A process_csv_files function that will process all csv files using the functions described above and will save each calculation as a column in a new integrated csv file.
    Still pending.
- A word_error function that will calculate word error rates by taking the levenshtein distance per utterance and dividing it by the total number of words in the utterance. This will be the main measure for reliability. 
    Still pending.