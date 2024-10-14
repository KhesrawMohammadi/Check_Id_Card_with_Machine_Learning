
# Check ID Card with Machine Learning

## Overview

This project is designed to check the authenticity of an ID card image by comparing it with a stored original image using machine learning techniques. It leverages `opencv`, `Pillow`, and `skimage` libraries for image processing and similarity comparison. This project was created in Django to handle image uploads and comparisons.

## Features

- Users can upload an image file (ID card photo).
- The app resizes and processes both the uploaded image and a reference original image.
- It calculates the similarity between the uploaded and original images using Structural Similarity Index (SSIM).
- Highlights differences between the two images.
- Provides a similarity score and visual comparison with generated difference images.

## Technologies Used

- **Backend**: Django
- **Image Processing**: `OpenCV`, `Pillow`
- **Similarity Measurement**: `scikit-image` (SSIM)
- **Frontend**: HTML, Tailwind CSS

## Setup and Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/KhesrawMohammadi/Check_Id_Card_with_Machine_Learning.git
    cd Check_Id_Card_with_Machine_Learning
    ```

2. **Create a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install required packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Django server**:
    ```bash
    python manage.py runserver
    ```

5. **Access the application**:
    Open a web browser and go to `http://127.0.0.1:8000/` to use the ID card checking portal.

## Usage

- **Upload**: Go to the upload portal and upload the ID card image.
- **Compare**: The system will compare it with the reference image stored in `media/OriginalId/` directory.
- **View Results**: You will get a similarity score, and the system will generate images with highlighted differences.

## File Structure

- `main_app/views.py`: Contains logic for handling file uploads, image processing, and comparison.
- `templates/index.html`: The main HTML page for uploading and viewing results.
- `media/uploads/`: Directory where uploaded files are saved.
- `media/OriginalId/`: Contains the original ID card image used for comparison.
- `media/GeneratedIds/`: Stores the generated images with differences and other processed results.

## License

This project is licensed under the **GNU General Public License v3.0 (GPL-3.0)**. You may freely use, modify, and distribute the code in accordance with the terms of the license.

For more information, please visit [GPL-3.0 License](https://www.gnu.org/licenses/gpl-3.0.html).

## Contributing

Feel free to open issues or submit pull requests if you'd like to contribute to this project. Your help is always appreciated!

## Author

- [Khesraw Mohammadi](https://github.com/KhesrawMohammadi)

## Acknowledgements

Special thanks to the open-source community for providing the tools and libraries that made this project possible.
