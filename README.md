# Real-Time Face Recognition System

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg?style=flat-square)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.0+-green.svg?style=flat-square)](https://opencv.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A robust and efficient real-time face recognition system implemented using OpenCV and Python.  This project provides functionality for face detection, training, and recognition, making it suitable for various applications such as security systems, attendance tracking, and personalized user interfaces.

## Overview

This project showcases a complete face recognition pipeline, from detecting faces in a video stream to recognizing individuals based on a trained model.  It leverages the power of OpenCV for image processing and provides a modular design for easy extension and customization.

## Features

*   **Real-time Face Detection:**  Accurate and fast face detection using Haar cascades.
*   **Face Training:**  Simple and intuitive interface for collecting face samples and training the recognition model.
*   **Face Recognition:**  Real-time recognition of trained faces with clear identification.
*   **Modular Design:**  Well-organized code with separate modules for detection, training, and recognition.
*   **Easy to Use:**  Simple command-line interface for selecting different functionalities.

## Project Structure

The project is organized as follows:



## Getting Started

### Prerequisites

*   Python 3.7+
*   OpenCV (cv2)
*   Other dependencies (install with `pip install -r requirements.txt`)

### Installation

1.  Clone the repository:

    ```
    git clone https://github.com/the-shubham-raj/FaceRecognition.git

2.  Create a virtual environment (recommended):

    ```
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  Install the required packages:

    ```
    pip install opencv-python
    # Add any other dependencies here if needed
    ```

### Usage

1.  Run the `main.py` script:

    ```
    python main.py
    ```

2.  Choose an option from the menu:

    *   `1`: Detect Faces (real-time face detection)
    *   `2`: Train Faces (collect face samples and train the model)
    *   `3`: Recognize Faces (real-time face recognition)

    Follow the on-screen prompts for each option.

## Key Components

*   **`face_detector.py`**: Implements the `FaceDetector` class, which uses Haar cascades to detect faces in an image.
*   **`face_trainer.py`**: Implements the `FaceTrainer` class, which collects face samples, trains the face recognition model (using `cv2.face.LBPHFaceRecognizer_create()`), and saves the trained model to `trainer.yml`.
*   **`face_recognizer.py`**: Implements the `FaceRecognizer` class, which loads the trained model, recognizes faces in real-time, and displays the recognized names.
*   **`main.py`**: The main script that provides the command-line interface for interacting with the system.

## Training the Model

To train the model, select option `2` from the main menu.  You will be prompted to enter a User ID.  The system will then capture face samples from your webcam and store them in the `dataset` directory under a subdirectory with your specified User ID.  After collecting sufficient samples, the model will be trained and saved to `trainer.yml`.

## Future Enhancements

*   **Deep Learning Integration:** Integrate a deep learning-based face detection and recognition model for improved accuracy and robustness.
*   **Mask Detection:** Add functionality to detect faces wearing masks.
*   **Emotion Recognition:** Extend the system to recognize emotions from facial expressions.
*   **Database Integration:** Store recognized faces in a database for persistence and improved management.
*   **Cloud Deployment:**  Deploy the system to a cloud platform for remote access and scalability.
*   **Code Optimization:** Improve performance through code profiling and optimization techniques.
*   **Unit Tests:** Implement comprehensive unit tests to ensure code quality and reliability.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome!  Please feel free to submit pull requests or open issues to suggest improvements or report bugs.
