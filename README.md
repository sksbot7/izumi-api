# Eypz API

Welcome to the Eypz API! This API provides a simple and efficient way to stream images and videos. You can access various media resources via the following endpoints.

## Features

- **Image Streaming:** Access images directly through the API.
- **Video Streaming:** Stream videos seamlessly.

## Base URL

The base URL for the API is:

```
https://izumi-api.onrender.com/
```

## Endpoints

### Image Streaming

To stream an image, use the following endpoint:

```
GET /eypz/image.png
```

**Example:**
```
https://izumi-api.onrender.com/eypz/image.png
```

### Video Streaming

To stream a video, use the following endpoint:

```
GET /eypz/video.mp4
```

**Example:**
```
https://izumi-api.onrender.com/eypz/video.mp4
```

## Usage

You can access images and videos by sending a GET request to the respective endpoints. Simply copy and paste the example URLs into your browser or API client to view the media.

## Installation

```
pip install -r requirements.txt
```
```
python app.py
```
or you can use Dockerfile

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.
