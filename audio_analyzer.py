import whisper


model = whisper.load_model("base")


def transcribe_audio(video_path):

    result = model.transcribe(video_path)

    text = result["text"]

    return text