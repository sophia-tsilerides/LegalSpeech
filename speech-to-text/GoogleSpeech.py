#!/usr/bin/env python

# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Google Cloud Speech API using the REST API for async
batch processing.

How to use:
    python GoogleSpeech.py Filename.flac num_speakers
    python GoogleSpeech.py gs://cloud-samples-tests/speech/vr.flac num_speakers

Base code from github.com/googleapis
Adjustments by Sophia 
"""

import argparse
import io
import os

# TODO: Enable data logging for price discount; (Data logging is disabled for this project for Google Cloud Speech API) 
#       Speech Adaptation: https://cloud.google.com/speech-to-text/docs/context-strength, https://cloud.google.com/speech-to-text/docs/speech-adaptation

# [START speech_transcribe_async]
def transcribe_file(speech_file, num_speakers):
    """Transcribe the given audio file asynchronously."""

    # Imports the Google Cloud client library
    #from google.cloud import speech
    from google.cloud import speech_v1p1beta1 as speech


    # Instantiates a client
    client = speech.SpeechClient()

    # The name of the audio file to transcribe
    file_name = os.path.join(os.path.dirname(__file__), "resources", "audio.raw")
    
    # Loads the audio into memory
    with io.open(speech_file, "rb") as audio_file:
        content = audio_file.read()
    
    # Construct a recognition metadata object
    metadata = speech.RecognitionMetadata()
    metadata.interaction_type = speech.RecognitionMetadata.InteractionType.DISCUSSION
    metadata.recording_device_type = (
        speech.RecognitionMetadata.RecordingDeviceType.OTHER_INDOOR_DEVICE
    )
    metadata.audio_topic = "court trial hearing" 
    metadata.original_mime_type = "audio/mp3"

    audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.FLAC,
        sample_rate_hertz=16000,
        language_code="en-US",
        enable_automatic_punctuation=True,
        enable_speaker_diarization=True,
        diarization_speaker_count=num_speakers,
        # Enhanced models cost more than standard models. 
        use_enhanced=True,
        model="video",
        enable_word_time_offsets=True,

        )

    # Detects speech in the audio file -- short audio file
    print("Waiting for operation to complete...")
    response = client.recognize(config=config, audio=audio)
    result = response.results[-1]

    words_info = result.alternatives[0].words

    # Printing out the output:
    for word_info in words_info:
        print(
            u"word: '{}', speaker_tag: {}, start_time:{}, end_time:{}".format(word_info.word, word_info.speaker_tag, word_info.start_time.total_seconds(), word_info.end_time.total_seconds())
        )
    
# [END speech_transcribe_async]


# [START speech_transcribe_async_gcs]
def transcribe_gcs(gcs_uri, num_speakers):
    """Asynchronously transcribes the audio file specified by the gcs_uri."""

    # Imports the Google Cloud client library
    #from google.cloud import speech
    from google.cloud import speech_v1p1beta1 as speech


    # Instantiates a client
    client = speech.SpeechClient()
    
    # Construct a recognition metadata object
    metadata = speech.RecognitionMetadata()
    metadata.interaction_type = speech.RecognitionMetadata.InteractionType.DISCUSSION
    metadata.recording_device_type = (
        speech.RecognitionMetadata.RecordingDeviceType.OTHER_INDOOR_DEVICE
    )
    metadata.audio_topic = "court trial hearing" 
    metadata.original_mime_type = "audio/mp3"

    audio = speech.RecognitionAudio(uri=gcs_uri)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.FLAC,
        sample_rate_hertz=16000,
        language_code="en-US",
        enable_automatic_punctuation=True,
        enable_speaker_diarization=True,
        diarization_speaker_count=num_speakers,
        # Enhanced models cost more than standard models. 
        use_enhanced=True,
        model="video",
        enable_word_time_offsets=True,

    )

    # Detects speech in the audio file -- long audio file
    operation = client.long_running_recognize(config=config, audio=audio)

    print("Waiting for operation to complete...")
    response = operation.result(timeout=300)

    # Writing results to txt
    case_file = open("{}.txt".format(gcs_uri.split('/')[-1][:-5]), "a")
    for result in response.results:
        alternative = result.alternatives[0]
        case_file.write("Transcript: {} \n".format(alternative.transcript))
        case_file.write("Confidence: {} \n".format(alternative.confidence))

        for word_info in alternative.words:
            word = word_info.word
            start_time = word_info.start_time
            end_time = word_info.end_time
            speaker_tag = word_info.speaker_tag

            case_file.write(
                f"Word: {word}, start_time: {start_time.total_seconds()}, end_time: {end_time.total_seconds()}, speaker_tag: {speaker_tag} \n"
            )
    case_file.close()

    print("Dirized and transcribed {}".format(gcs_uri.split('/')[-1]))

# [END speech_transcribe_async_gcs]

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'path', help='File or GCS path for audio file to be recognized')
    parser.add_argument(
        'num_speakers', help='diarization_speaker_count')
    args = parser.parse_args()

    if args.path.startswith("gs://"):
        transcribe_gcs(args.path, int(args.num_speakers))
    else:
        transcribe_file(args.path, int(args.num_speakers))