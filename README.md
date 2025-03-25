# bBiometrics - Behavioral Biometric Authentication System

bBiometrics is a desktop security application that uses behavioral biometrics to authenticate users. It monitors keyboard dynamics and mouse movement patterns to create a unique behavioral profile for each user, providing an additional layer of security beyond traditional password authentication.

## Features

- Behavioral Biometric Authentication:
  - Keystroke dynamics analysis
  - Mouse movement pattern recognition
  - Login time pattern monitoring
- Security Features:
  - Suspicious login detection
  - Time-based access control
  - Continuous authentication
  - Behavioral pattern matching
- Local data storage with SQLite

## Download

Download the latest version from the [Releases](../../releases) page.

## System Requirements

- Windows 10 or later
- 100MB free disk space
- 4GB RAM recommended
- Administrator privileges for installation

## Usage

1. Download and run the executable
2. The application runs in the background, monitoring behavioral patterns
3. Alerts appear when suspicious activity is detected

## Security and Privacy

- All behavioral data is stored locally
- No internet connection required
- Data is encrypted at rest

### Requirements

- Python 3.8 or higher
- Dependencies listed in `requirements.txt`:
  - pynput >= 1.7.6 (For keyboard and mouse monitoring)
  - numpy >= 1.21.0 (For numerical operations and data analysis)
  - pandas >= 1.3.0 (For data manipulation and analysis)
  - scikit-learn >= 1.0.2 (For pattern recognition)
  - python-dateutil >= 2.8.2 (For datetime handling)
  - pywin32 >= 228 (Windows only)
  - pyinstaller >= 5.13.0 (For creating executable)

### Project Structure

```
bBiometrics/
├── src/
│   ├── collectors/     # Activity collection modules
│   │   ├── keyboard.py
│   │   ├── mouse.py
│   │   └── login.py
│   ├── ml/            # Machine learning components
│   ├── ui/            # User interface components
│   └── main.py        # Application entry point
├── data/              # Data storage directory
├── requirements.txt   # Project dependencies
└── .gitignore        # Git ignore rules
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Privacy Note

This tool collects system activity data for analysis purposes. Please ensure you comply with local privacy laws and regulations when using this tool, especially in workplace environments.

## Acknowledgments

- Built with PyQt6 for the user interface
- Uses pynput for system activity monitoring 