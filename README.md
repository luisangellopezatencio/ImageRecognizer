# ImageRecognizer

This project is a web application built with **FastAPI** that uses a pre-trained **PyTorch (DenseNet-121)** model to classify images. It provides both a simple user interface to upload an image and a REST API endpoint for programmatic use. The model is trained on the ImageNet dataset and can recognize 1,000 different object classes.

## Features

- **Web Interface**: An easy-to-use page to upload an image and view the prediction.
- **REST API**: A `/predict` endpoint for programmatic image classification.
- **PyTorch Integration**: Uses `densenet121` pre-trained on ImageNet for high-accuracy predictions.
- **Performance Metrics**: Calculates and displays the inference time for each prediction.

## Tech Stack

- **Backend**: FastAPI
- **ML/AI**: PyTorch, Torchvision
- **Server**: Uvicorn
- **Templating**: Jinja2

## Setup and Installation (using Pixi)

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd ImageRecognizer
    ```

2.  **Install Pixi:**
    If you don't have Pixi installed, follow the instructions on the [official website](https://pixi.sh/latest/installation/).

3.  **Install Dependencies:**
    This project uses Pixi to manage dependencies. To install them, simply run the following command. It will create a dedicated environment and install all packages defined in the `pixi.toml` file.
    ```bash
    pixi install
    ```

## How to Run the Application

Start the development server using Pixi, which will run Uvicorn inside the managed environment:
```bash
pixi run uvicorn main:app --reload
```
The application will be available at `http://127.0.0.1:8000`.

## How to Use

### 1. Web Interface

1.  Open your browser and navigate to `http://127.0.0.1:8000`.
2.  Click **"Choose File"** to select an image from your computer.
3.  Click **"Submit"**.
4.  The prediction result and inference time will be displayed on the page.

### 2. API Endpoint

You can send a `POST` request to the `/predict` endpoint with an image file to get a JSON response.

**Example using cURL:**
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@static/images/dog.jpg;type=image/jpeg'
```

**Expected JSON Response:**
```json
{
    "inference_time": "210 ms",
    "predictions": {
        "class_id": "n02099601",
        "class_name": "golden_retriever"
    }
}
```

## API Routes

- `GET /`: Renders the main HTML page for uploading images.
- `POST /`: Handles the form submission from the main page and re-renders the page with the prediction result.
- `POST /predict`: The dedicated API endpoint that accepts an image file and returns a JSON object with the prediction details.
