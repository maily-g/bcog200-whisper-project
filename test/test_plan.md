This folder is used to test the accuracy of each function for this project. It ensures reliable processing of Whisper against human-coded transcripts, accurate measures of language-level factors.

A basic short 30-second recording alongside its associated human-coded transcript can be used to test functions in the code. 
The process_audio_files function can be tested with the 30-second clip. The human-coded transcript will be used to test the load_expert_files function.
The output from this latter function will save a csv file.  

The test string "This is a test" is used to test the word_count and  unique_words functions. It can also be used to test the levenshtein_distance
function. The output should be 0 in the case of the test string. 

A test script (i.e., test.py) will run the full code on test files and check that:
-Whisper transcript CSV is generated correctly
-Human transcript CSV is outputed from the original file provided
-Per-utterance word counts and unique words are added to the csv files
-Transcript pairs are aligned by timestamp or index
-Levenshtein distance is calculated per pair