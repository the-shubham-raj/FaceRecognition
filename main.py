import cv2

from face_recognition.face_detector import FaceDetector
from face_recognition.face_trainer import FaceTrainer
from face_recognition.face_recognizer import FaceRecognizer

if __name__ == "__main__":
    print("Choose an option:\n1. Detect Faces\n2. Train Faces\n3. Recognize Faces")
    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        detector = FaceDetector()
        cap = cv2.VideoCapture(0)

        while True:
            ret, img = cap.read()
            if not ret:
                break

            faces = detector.detect_faces(img)
            img = detector.draw_faces(img, faces)
            cv2.imshow("Face Detection", img)

            if cv2.waitKey(1) & 0xFF == 27:
                break

        cap.release()
        cv2.destroyAllWindows()

    elif choice == "2":
        user_id = input("Enter User ID: ")
        trainer = FaceTrainer()
        trainer.collect_faces(user_id)
        trainer.train_faces()

    elif choice == "3":
        recognizer = FaceRecognizer()
        recognizer.recognize_faces()

    else:
        print("Invalid choice. Exiting.")
