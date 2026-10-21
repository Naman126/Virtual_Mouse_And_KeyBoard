# Virtual Mouse and Keyboard Using Hand Gestures 🖐️

A computer vision project that allows users to control their computer's mouse and keyboard using hand gestures captured through a webcam. The project uses Python, OpenCV, and MediaPipe to detect hand landmarks and translate gestures into computer actions.

## 🚀 Features

- **Virtual Mouse Control:** Move the mouse cursor by moving your index finger.
- **Left and Right Click:** Perform mouse clicks using specific hand gestures.
- **Double Click:** Trigger a double-click through gesture recognition.
- **Virtual Keyboard:** Type using an on-screen keyboard controlled by finger movements.
- **Screenshot Capture:** Capture and save screenshots using a hand gesture.
- **Real-Time Hand Tracking:** Detect and display hand landmarks through a webcam.
- **Visual Feedback:** Display detected actions and highlighted virtual keys on the video feed.

## 🛠️ Technologies Used

- **Python** — Core programming language.
- **OpenCV** — Webcam access, image processing, and visual feedback.
- **MediaPipe** — Real-time hand landmark detection.
- **NumPy** — Mathematical calculations for angles and distances.
- **PyAutoGUI** — Mouse movement, keyboard input, and screenshots.
- **pynput** — Mouse click control.

## 📁 Project Structure

```text
virtual-mouse-keyboard-gestures/
├── hand.py          # Main application and gesture recognition
├── track.py         # Angle and distance calculations
├── README.md        # Project documentation
└── .gitignore       # Files excluded from Git
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/virtual-mouse-keyboard-gestures.git
cd virtual-mouse-keyboard-gestures
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

Activate it on macOS or Linux:

```bash
source .venv/bin/activate
```

On Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
python -m pip install opencv-python mediapipe numpy pyautogui pynput
```

### 4. Run the application

```bash
python hand.py
```

Allow camera access when prompted. The application will open a webcam window and display the virtual keyboard.

Press **Q** while the webcam window is active to exit.

## 🖐️ How It Works

1. The webcam captures live video.
2. MediaPipe detects hand landmarks in each frame.
3. The application calculates finger angles and distances.
4. Gesture rules identify the intended mouse or keyboard action.
5. PyAutoGUI and pynput execute the corresponding computer actions.
6. OpenCV displays the hand landmarks, virtual keyboard, and action feedback.

## 💻 System Requirements

- Python with compatible versions of OpenCV and MediaPipe.
- A working webcam.
- A computer running macOS, Windows, or Linux, subject to operating-system permissions and library compatibility.
- Permission to control the mouse and keyboard through automation tools.

**macOS users:** Grant camera access and, if requested, Accessibility permissions to the terminal or application running the script.

## 🔮 Future Improvements

- Add more keyboard keys and special characters.
- Improve gesture accuracy and reduce accidental clicks.
- Add adjustable sensitivity and customizable gestures.
- Support additional gestures and multi-hand interactions.
- Develop a graphical settings interface.

## 🎓 Project Information

Developed as an academic project focused on computer vision, human-computer interaction, and gesture-based automation.

## 📄 License

No license has been specified yet. Add an appropriate open-source license if you intend to allow others to reuse or modify the project.
