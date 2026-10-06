import cv2
import mediapipe as mp


def analyze_video(video_path):

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        return {
            "face_detection": 0,
            "frames": 0,
            "face_frames": 0
        }

    mp_face = mp.solutions.face_detection

    detector = mp_face.FaceDetection(
        model_selection=0,
        min_detection_confidence=0.5
    )

    total_frames = 0
    face_frames = 0

    while True:

        success, frame = cap.read()

        if not success:
            break

        total_frames += 1

        rgb = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        result = detector.process(rgb)

        if result.detections:
            face_frames += 1

    cap.release()
    detector.close()

    if total_frames == 0:
        face_percentage = 0
    else:
        face_percentage = (
            face_frames / total_frames
        ) * 100

    return {
        "face_detection": round(face_percentage, 2),
        "frames": total_frames,
        "face_frames": face_frames
    }