# TomatoTimer

TomatoTimer is a simple Pomodoro-style timer built using Python's Tkinter library. It allows users to set a timer for work and break intervals, helping them focus on tasks using the Pomodoro technique. The application provides visual cues for work and break periods and tracks completed work sessions with checkmarks.

## Features

- **Work Timer**: Set work intervals (default: 25 minutes).
- **Break Timer**: Short breaks (default: 5 minutes) and long breaks (default: 20 minutes) after every 4th work session.
- **Visual Timer Display**: Countdown timer displayed in the UI.
- **Progress Tracking**: Track the number of work sessions with checkmarks.
- **Responsive UI**: Simple and clean interface with interactive buttons.

## Getting Started

### Prerequisites

To run the TomatoTimer app, ensure you have Python installed on your system. This app uses the Tkinter library, which is usually bundled with Python, so no additional installation is necessary.

### Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/tomato-timer.git
   ```

2. Navigate to the project folder:
   ```bash
   cd tomato-timer
   ```

3. Run the application:
   ```bash
   python tomato_timer.py
   ```

### File Structure

- `tomato_timer.py`: Main application file containing the UI and timer logic.
- `README.md`: Project documentation file.
- `tomato.png`: Image used in the UI (tomato image).
- `constants.py`: (Optional) File for storing all constant values like timer durations, colors, etc.
- `ui.py`: (Optional) UI setup and update logic.
- `timer.py`: (Optional) Timer functionality and logic for countdown, start, reset, etc.

### How It Works

- The timer starts when you click the "Start" button.
- The app alternates between work sessions and break intervals.
- After every work session, a checkmark is added to track progress.
- When the timer ends, the app automatically starts the next session (work or break).
- You can reset the timer anytime by clicking the "Reset" button.

### Customization

You can modify the following constants in the code to adjust the timer settings:

- **WORK_MIN**: Work interval in minutes (default: 25).
- **SHORT_BREAK_MIN**: Short break interval in minutes (default: 5).
- **LONG_BREAK_MIN**: Long break interval in minutes (default: 20).
- **PINK, RED, GREEN, YELLOW**: UI colors.

### Example

```python
WORK_MIN = 30
SHORT_BREAK_MIN = 10
LONG_BREAK_MIN = 25
```

### Screenshots

![image](https://github.com/user-attachments/assets/f3dd6dc2-e0ec-4e5e-98e1-afde2349aa9c)

## Contributing

1. Fork this repository.
2. Create a branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
