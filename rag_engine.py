from pypdf import PdfReader


def read_resume(pdf_file):

    reader = PdfReader(pdf_file)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text

    return text


def create_feedback(
    transcript,
    resume
):

    feedback = []

    if len(transcript.split()) < 50:

        feedback.append(
            "Try to provide more detailed answers."
        )

    if "python" in transcript.lower():

        feedback.append(
            "Python experience was mentioned."
        )

    if "project" in transcript.lower():

        feedback.append(
            "The candidate discussed project experience."
        )

    if not feedback:

        feedback.append(
            "Practice giving structured answers."
        )

    return feedback