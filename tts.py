# import the playht SDK
from pyht import Client, TTSOptions

# Initialize PlayHT API with your credentials
client = Client("<YOUR_PLAY_HT_API_KEY>", "<YOUR_PLAY_HT_USER_ID>")

# configure your stream
options = TTSOptions(
    # this voice id can be one of our prebuilt voices or your own voice clone id, refer to the`listVoices()` method for a list of supported voices.
    voice="s3://voice-cloning-zero-shot/d9ff78ba-d016-47f6-b0ef-dd630f59414e/female-cs/manifest.json",

    # you can pass any value between 8000 and 48000, 24000 is default
    sample_rate=24_000,
  
    # the generated audio encoding, supports 'raw' | 'mp3' | 'wav' | 'ogg' | 'flac' | 'mulaw'
    format="mp3",

    # playback rate of generated speech
    speed=1,
)

# start streaming!
text = "Hey, this is Jennifer from Play. Please hold on a moment, let me just um pull up your details real quick."

# must use turbo voice engine for the best latency
for chunk in client.tts(text=text, voice_engine="PlayHT2.0-turbo", options=options):
    # Do whatever you want with the stream, you could save it to a file, stream it in realtime to the browser or app, or to a telephony system
    pass