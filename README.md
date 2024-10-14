
# Check ID Card with Machine Learning

This project is a web-based application that allows users to upload ID card images and compare them against a stored original image to detect tampering. The application uses Python, Django, OpenCV, and Machine Learning techniques to process and compare the images, highlighting differences using the Structural Similarity Index (SSIM).

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- Upload an ID card image for comparison.
- Compare the uploaded image with a stored original ID card image.
- Detects tampering using Structural Similarity Index (SSIM).
- Highlights the differences between the original and uploaded image.
- Generates comparison results and provides a similarity score.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/KhesrawMohammadi/Check_Id_Card_with_Machine_Learning.git
   cd Check_Id_Card_with_Machine_Learning
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Migrate the database:**

   ```bash
   python manage.py migrate
   ```

5. **Run the Django development server:**

   ```bash
   python manage.py runserver
   ```

6. **Access the application:**

   Open your browser and go to `http://127.0.0.1:8000/` to use the application.

## Usage

1. **Upload ID Card Image:**
   - Navigate to the homepage and upload an ID card image (JPEG or PNG format).
   
2. **View Comparison Results:**
   - The app will compare the uploaded image with the original ID card image stored in the system.
   - If differences are detected, the app will highlight the tampered regions of the image.
   - The similarity score will be displayed, and comparison images (highlighted differences, thresholded images, etc.) will be generated.

## Folder Structure

```bash
├── Check_Id_Card_with_Machine_Learning/      # Root directory of the Django project
│   ├── main_app/                             # Main application folder
│   │   ├── templates/                        # HTML templates
│   │   ├── static/                           # Static files (CSS, JS, etc.)
│   │   └── views.py                          # View handling for image upload and comparison
│   └── settings.py                           # Django settings
├── media/
│   ├── OriginalId/                           # Original stored images (ID card)
│   ├── GeneratedIds/                         # Generated images showing tampering detection
│   └── uploads/                              # Uploaded images from users
└── README.md                                 # This README file
```

## Contributing

Contributions are welcome! If you'd like to contribute, follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a Pull Request.

## License

This project is licensed under the GPL License. See the [LICENSE](LICENSE) file for more details.
