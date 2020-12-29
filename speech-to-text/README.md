## Transcribing with Google’s Speech-to-Text API

### Using local file (<10 MB)
1. Enable Speech-to-Text API
Go to project in GCP
Search for “Speech-to-Text” in the search bar
2. Install Google Cloud SDK (if you haven’t already)
https://www.youtube.com/watch?v=k-8qFh8EfFA
3. Configure your machine to gcloud

`gcloud components update`				should run this regularly

`gcloud auth login`					to log into the system

`gcloud config set project ak8096-biasjudge-d38a`     Configure local setup

4. Create a service account key 

- In console, go to APIs&Services > Credentials 
- In Service Accounts section Click on the Service Account link 
- In Keys section, Add Key  > Create New Key > JSON (downloads JSON)
- Put the JSON somewhere where you can access it easily (don’t ever put this in code or 
public repos!!)
- In terminal: `export GOOGLE_APPLICATION_CREDENTIALS=`"[PATH OF JSON]" 
	Ex.  `export GOOGLE_APPLICATION_CREDENTIALS=/Users/sophiatsilerides/Desktop/1006/akxxxx-biasjudge-xxxx-xxxxxxxxxxxx.json`
5. pip install google-cloud-speech (if you haven’t already)
6. Transcribe

Have in the file you are cd’d into the .flac file you want to transcribe and the GoogleSpeech.py file from github
`python GoogleSpeech.py sample.flac num_speakers`

7. Disable API & delete service key & Delete bucket

### Using gcp file (>10 MB)
Same instructions as above but instead of referencing a local file, you must reference a file in a GCP bucket. So:

1. Create a bucket to store flac files
2. Give service account proper permissions 
- `gsutil iam ch serviceAccount:my-service-account@project.iam.gserviceaccount.com:objectAdmin gs://my-project/my-bucket`
3. Run with `python GoogleSpeech.py gs://cloud-samples-tests/speech/vr.flac num_speakers`
4. Disable API & delete service key & Delete bucket

### Conversion commands
#### Locally
- ffmpeg -i input.wav -codec:a libmp3lame -qscale:a 2 output.mp3	(.wav to .mp3)
- ffmpeg -i output.mp3 -ac 1 -ar 16000 sample.flac			(.mp3 to .flac)
#### On GCP
1. Copy mp3 files from Amazon S3 buckets to GCP bucket
- `curl -L https://s3.amazonaws.com/oyez.case-media.mp3/case_data/2019/18-877/18-877_20191105-argument.delivery.mp3 | gsutil cp - gs://BUCKET_NAME/file_name.mp3`
2. Install current versions of ffmpeg
- `sudo apt update`
- `sudo apt install ffmpeg`
3. Verify ffmpeg is installed
- `ffmpeg -version`
4. Create “local” directory
- `mkdir data`
5. Copy data files from bucket and place in “local” directory to work with (ie. convert, split, etc)
- `gsutil -m cp gs://BUCKET_NAME/*.mp3 ~/data/`
6. Create enviro variable for Cloud Shell instance dir path that points to downloaded files:
- `export DATA=~/data`
7. Change directory to the “data” folder
- `cd data`
8. Probe file for metadata (just to check file type; not a necessary step)
- `ffprobe $DATA/file_name.mp3`
9. Convert from mp3 to flac (channel 1 mono, 16 bits, sampling rate 16000Hz)
- `ffmpeg -i $DATA/file_name.mp3 -ac 1 -ar 16000 -sample_fmt s16 $DATA/output_file_name.flac`
9b.  Convert from mp3 to wav (channel 1 mono, 16 bits, sampling rate 16000Hz)
- `ffmpeg -i $DATA/test_audio.mp3 -acodec pcm_s16le -ac 1 -ar 16000 $DATA/test_audio.wav`
9c. Do it in batch 
- `for f in *.mp3; do ffmpeg -i "$f" -acodec pcm_s16le -ac 1 -ar 16000 "${f%.mp3}.wav"; done`

or

- `for f in *.mp3; do ffmpeg -i "$f" -acodec pcm_s16le -ac 1 -ar 16000 "${f%.mp3}.flac"; done`
10. Copy “local” files back to GCP
- `gsutil cp *.wav gs://BUCKET_NAME`

or

- `gsutil cp *.flac gs://BUCKET_NAME`
11. Copy “local” files back to GCP (created a separate folder for them)
- `gsutil cp split_file_name*.flac gs://BUCKET_NAME/folder_name`
12. Delete “local” files
- `rm -r data`

ffmpeg resource:
https://gist.github.com/protrolium/e0dbd4bb0f1a396fcb55

Audio pre-processing resource:
https://cloud.google.com/solutions/media-entertainment/optimizing-audio-files-for-speech-to-text


