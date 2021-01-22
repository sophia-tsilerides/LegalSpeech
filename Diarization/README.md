# Diarization

## Details
Diarizing audio recordings from court proceedings.

The court proceedings diarized in this notebook are from the Supreme Court of the US, which provides a fully supervised dataset of transcribed and diarized proceedings to evaluate diarization performance.

The diarization process relies on Reference Dependent Speaker Verification (RDSV) and requires a database of reference audio for each judge (which is converted to multiple reference embeddings for each speaker). Reference embeddings are then compared against the embeddings at each time step of the full case embeddings. The judge with the highest similarity score at any given time step is inferred as the speaker.

## Prerequisites

`webrtcvad`

`resemblyzer`

`pyannote.audio 1.1`

## Reference Audio Instructions

Gather RTTM files from the training set to create reference audio for each judge. Functions stored within the notebook randomize which audio segments are selected for each judge. It is important that multiple references are gathered for each judge so as to capture them at different times of the day/mood, etc. and create a good representation of the judge.

Note: Method 1 was used in previous versions where we stored .wav and .txt files by judges' speaking segments and created embeddings for each of these segments separately. Going forward, use Method 2 which uses an RTTM file of diarized times and extracts the speaker's embedding from the full case embedding at the known times.

## Diarization Instructions

The diarization process requires:

1) A dictionary storing each judge as a key and their reference embeddings as the values. (Note that each judge will have multiple reference embeddings.)

2) A list of all judges in the case we wish to diarize.

3) Embeddings for the full case audio.

4) Times associated with each embedding from the full case audio.

