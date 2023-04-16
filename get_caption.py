from youtube_transcript_api import YouTubeTranscriptApi

transcript_list = YouTubeTranscriptApi.list_transcripts("qwogNykaAH8")

with open("captions.txt", "w") as f:
    for i, transcript in enumerate(transcript_list):
        for tr in transcript.fetch():
            f.write(f"{tr['text']}\n")

