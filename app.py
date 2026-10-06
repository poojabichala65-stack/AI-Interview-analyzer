import streamlit as st

from video_analyzer import analyze_video
from audio_analyzer import transcribe_audio
from text_analyzer import analyze_text
from rag_engine import (
    read_resume,
    create_feedback
)


st.set_page_config(
    page_title="AI Interview Analyzer",
    page_icon="🎤",
    layout="wide"
)


st.title("🎤 AI Interview Analyzer")

st.write(
    "Multimodal Interview Analysis using "
    "Video + Audio + Text"
)


st.sidebar.header("Candidate Information")

candidate_name = st.sidebar.text_input(
    "Candidate Name"
)


resume = st.sidebar.file_uploader(
    "Upload Resume",
    type=["pdf"]
)


video = st.file_uploader(
    "Upload Interview Video",
    type=[
        "mp4",
        "mov",
        "avi",
        "mkv"
    ]
)


if video:

    st.video(video)


if st.button("🚀 Analyze Interview"):

    if video is None:

        st.error(
            "Please upload an interview video."
        )

        st.stop()


    with st.spinner(
        "Saving interview video..."
    ):

        video_path = (
            "uploads/interview.mp4"
        )

        with open(
            video_path,
            "wb"
        ) as file:

            file.write(
                video.getbuffer()
            )


    # VIDEO ANALYSIS

    st.header("🎥 Video Analysis")

    with st.spinner(
        "Analyzing video..."
    ):

        video_result = analyze_video(
            video_path
        )


    col1, col2, col3 = st.columns(3)


    col1.metric(
        "Frames",
        video_result["frames"]
    )


    col2.metric(
        "Face Detected",
        f'{video_result["face_detection"]}%'
    )


    col3.metric(
        "Face Frames",
        video_result["face_frames"]
    )


    # AUDIO ANALYSIS

    st.header("🎙️ Audio Analysis")

    with st.spinner(
        "Converting speech to text..."
    ):

        transcript = transcribe_audio(
            video_path
        )


    st.subheader("Interview Transcript")

    st.text_area(
        "Transcript",
        transcript,
        height=250
    )


    # TEXT ANALYSIS

    st.header("📝 Text Analysis")

    text_result = analyze_text(
        transcript
    )


    col1, col2, col3 = st.columns(3)


    col1.metric(
        "Total Words",
        text_result["word_count"]
    )


    col2.metric(
        "Filler Words",
        text_result["filler_words"]
    )


    col3.metric(
        "Filler %",
        f'{text_result["filler_percentage"]}%'
    )


    # RESUME

    resume_text = ""

    if resume:

        resume_text = read_resume(
            resume
        )


    # FEEDBACK

    st.header("🤖 AI Feedback")

    feedback = create_feedback(
        transcript,
        resume_text
    )


    for item in feedback:

        st.write(
            "• " + item
        )


    # FINAL SCORE

    st.header("📊 Interview Summary")


    communication_score = max(
        0,
        100 -
        text_result["filler_percentage"] * 2
    )


    video_score = video_result[
        "face_detection"
    ]


    overall_score = (
        communication_score +
        video_score
    ) / 2


    st.metric(
        "Overall Interview Indicator",
        f"{overall_score:.1f}/100"
    )
    


    st.success(
        "Interview analysis completed!"
    )