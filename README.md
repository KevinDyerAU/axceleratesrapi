# Axcelerate API Webhook Service

A Flask-based webhook service that provides integration with the Axcelerate API for student management and assessment tracking.

## Overview

This service acts as a webhook endpoint for interacting with the Axcelerate API, providing functionality for:
1. Searching for students
2. Updating student assessments
3. Retrieving course enrolments

## Features

- Student lookup using Axcelerate's contact search API
- Assessment updates for training courses
- Course enrolment retrieval
- Secure authentication using API tokens
- RESTful API endpoints

## Setup and Configuration

### Prerequisites

- Python 3.8+
- Axcelerate API credentials (Web Service Token and API Token)

### Environment Variables

The following environment variables must be set in a `.env` file:

```bash
AXCELERATE_WEB_SERVICE_TOKEN=your_web_service_token
AXCELERATE_API_TOKEN=your_api_token
```

### Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file with your Axcelerate API credentials

## API Endpoints

### Root Endpoint

```
GET /
```

Returns a health check message.

### Student Lookup Endpoint

```
POST /axcelerate/student
```

Search for students in Axcelerate:

```json
{
    "search_term": "John Smith"
}
```

### Assessment Update Endpoint

```
POST /axcelerate/assessment
```

Update a student's assessment:

```json
{
    "enrolment_id": 12345,
    "outcome_code": "C",  # Assessment outcome code
    "status": "Completed",
    "comments": "Optional assessment comments"
}
```

### Course Enrolments Endpoint

```
GET /axcelerate/enrolments/<contact_id>
```

Retrieve all enrolments for a student:

```
GET /axcelerate/enrolments/12345
```

## Local Development

The Flask application runs on port 80 by default. Since port 80 requires administrative privileges, you may want to change the port number when running locally. You can modify the port in `main.py` or use the `PORT` environment variable:

```bash
PORT=5000 python main.py
```

## Deployment

The service is configured for deployment on Render. The `render.yaml` file contains the deployment configuration.

### Render Settings

When deploying on Render, add the following command to the "Start Command" setting:

```
gunicorn wsgi:app --timeout 240
```

## Error Handling

All endpoints return JSON responses with appropriate HTTP status codes:
- 200 OK - Successful operation
- 400 Bad Request - Invalid request parameters
- 500 Internal Server Error - API errors or processing failures

Error responses include an `error` field with a descriptive message:

```json
{
    "error": "Description of the error"
}
```

## Security

- All endpoints are secured using Axcelerate API tokens
- Tokens are loaded from environment variables
- Sensitive information is never logged or exposed in responses

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

    "elements": [
        {
            "type": "Title",
            "text": "Document Title",
            "metadata": {
                "page_number": 1,
                "coordinates": [...]
            }
        },
        {...}
    ],
    "metadata": {
        "bucket": "your-bucket",
        "key": "path/to/file.pdf",
        "file_size": 123456,
        "content_type": "application/pdf"
    }
}
```

### Available Parsing Strategies

The API supports several parsing strategies for document processing:

- `auto`: Automatically chooses the best strategy based on document characteristics (default)
- `fast`: Uses rule-based techniques for quick text extraction (not recommended for image-based files)
- `hi_res`: Uses advanced models to identify document layout and elements (recommended for high-quality processing)
- `ocr_only`: Uses OCR for image-based files
- `vlm`: Uses vision language models for image-based files (.bmp, .gif, .heic, .jpeg, .jpg, .pdf, .png, .tiff, .webp)

## Project Structure

```
fastunstructapi/
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── main.py
│   └── pipeline.py
├── requirements.txt
└── README.md
```

## Development

Run the development server:

```bash
python -m src.main
```

## Deployment

The application can be deployed using Gunicorn:

```bash
gunicorn -w 4 -k uvicorn.workers.UvicornWorker src.main:app
```

## Security

- All sensitive credentials are managed through environment variables
- No hardcoded credentials in the codebase
- Input validation is enforced
- Error handling is implemented

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.