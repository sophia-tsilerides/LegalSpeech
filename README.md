# CDS-Capstone-2020

Credit: https://github.com/HarryVolek/PyTorch_Speaker_Verification for initial speech embedder steps and network creation

## Folder: SCOTUS

### Details
Prepping SCOTUS data for modeling. 

Credit: https://github.com/walkerdb/supreme_court_transcripts for oyez parsing functions in mp3-to-gcp/oyez_parser.ipynb

### Prerequisites 
You will need the case_summaries.json from https://github.com/walkerdb/supreme_court_transcripts/tree/master/oyez.

Most of our computing is done on an HCP that does not support the requests package and therefore some of the scripts have been split to run locally and transfer of necessary files are done manually. 

All the modules in HPC needed for this process are:
module purge 

module load ffmpeg/intel/3.2.2 

module load python3/intel/3.7.3 

module load rclone/1.38 

### Instructions
1. Extracting mp3 files and metadata from oyez API with **mp3_curl_commands.py**
- NOTE: Our HPC cluster does not support the requests package, so this step happens locally. 
- NOTE: This script extract cases for which there is only *one* mp3 file for the corresponding case. 
- Have case_summaries from walkerdb's github in the same directory as the mp3_curl_commands.py script
- Specify date range for cases you want in mp3_curl_commands.py (line 116)
- Run with `python mp3_curl_commands.py`
- Output is: shell script mp3_curl_cmds.sh that you can run in HPC to get case mp3 from oyez API && oyez_metadatajson which we need in step 5. 

2. Run **mp3_curl_cmds.sh** 
- NOTE: This was performed in HPC 
- Run with `sbatch mp3_curl_cmds.sh`

3. Convert mp3s to wav files with **mp3_to_wav_batch.sh**
- NOTE: This was performed in HPC 
- NOTE: You might want to create a wavs file to run the script in first. You can `mv audio_split.py wavs`, `mv mp3_to_wav_batch.sh wavs`, and `mv oyez_metadata.json wavs`.
- Install current versions of ffmpeg with `module load ffmpeg/intel/3.2.2`
- Run with `sbatch mp3_to_wav_batch.sh /path/to/files /path/to/dest` EXAMPLE: `sbatch mp3_to_wav_batch.sh /scratch/smt570/test/mp3s /scratch/smt570/test/wavs`

5. Audio Splitting with **audio_split.py**
- NOTE: This is run to convert the wav files into consumable format for our model
- Load the right modules in HPC with: 

`module purge `

`module load ffmpeg/intel/3.2.2 `

`module load python3/intel/3.7.3 `

- NOTE: Make sure you have in the directory with the script (1) the wav files you want to split (2) oyez_metadata.json file from step 1 (3) an empty SCOTUS file and 
- Run with `python audio_split.py`
- Also outputs sharing_commands.txt. 

## Folder: icsi_corpus

### Details
Preparing ICSI Meeting Corpus for modeling.

### Prerequisites 

Most of our computing is done on an HCP that does not support the requests package and therefore the script `get_icsi_data.py` is done locally, and files are transferred to the HPC cluster manually.

All the modules in HPC needed for this process are:
module purge 

module load python3/intel/3.7.3 

conda install -c auto pydub

conda install -c conda-forge pyyaml

module swap anaconda3  python/intel/2.7.12

module load librosa/intel/0.5.0

### Instructions

1.  Extract raw transcript and audio files with `get_icsi_data.py` locally. Transfer `icsi_data` folder, containing subfolders `raw_transcripts` and `raw_audio`    to HPC cluster.

2.  Run `create_icsi_dataset.py` to create speaker folders for every speaker encountered, located as './icsi_data/icsi_files'. Each speaker folder will contain [start_time end_time transcript_text] as .txt file, and corresponding audio files for audio segments as .wav.

3.  Run `del_small_files.py` to remove .wav files that are <40KB, as well as with their corresponding .txt files by running `del_small_files.py`. These audio files are too small to process; buffer is too short and it is likely one or less words spoken which will not be picked up by VAD.

4.  Place config folder in './icsi_data/'. Update config file to point to location of unprocessed data; should be: './icsi_data/icsi_files/'.

5.  Run `data_preprocess.py` to create `train_tisv` and `test_tisv` folders. Train/test will automatically split 90/10. During script run, note output of speaker # showing numpy files containing 0 length arrays. 

6.  If there are speakers with 0 length arrays, find out which speaker name (folder) it belongs to by running `check_file.py`.
    i.  For ICSI Corpus:
        a. speaker10.npy (speaker folder: fe905) - TRAIN
        b. speaker35.npy (speaker folder: me908) - TRAIN
        c. speaker0.npy  (speaker folder: me907) - TEST
        
7.  Remove these speaker names (folders) from the unprocessed data location, and remove corresponding numpy speaker files from processed data location.
