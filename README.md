# Image Classification API with Deep Learning

This project provides a RESTful API for image classification using a deep learning model. It is built with FastAPI, TensorFlow, and SQLAlchemy, and is designed to be modular, scalable, and production-ready.

## Features
- **Image Classification:** Predicts whether an image belongs to a specific class using a pre-trained ResNet50 model.
- **REST API:** Exposes endpoints for predictions, secured with JWT authentication.
- **Database Integration:** Stores prediction results and metadata in a SQL database.
- **Logging:** Structured logging with log rotation for debugging and monitoring.
- **Docker Support:** Containerized for easy deployment.
- **CI/CD:** GitHub Actions for automated testing and deployment.
- **Unit and Integration Tests:** Comprehensive test suite for reliability.
- **API Documentation:** Automatically generated OpenAPI documentation.

## Prerequisites
- Python 3.9+
- Docker (optional, for containerized deployment)
- TensorFlow 2.x
- FastAPI
- SQLite (or any other supported database)

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/image-classifier.git
cd image-classifier
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables
Create a `.env` file in the root directory and add the following variables:
```
DATABASE_URL=sqlite:///./image_classifier.db
SECRET_KEY=supersecretkey
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
MODEL_PATH=models/image_classifier.h5
LOG_LEVEL=INFO
```

## Usage

### Run the Application Locally
```bash
uvicorn app:app --host 0.0.0.0 --port 80
```

### Run with Docker
```bash
docker-compose up --build
```

### Access the API
Open your browser or use a tool like curl or Postman.

The API will be available at `http://localhost:80`.

## API Endpoints

### 1. Authentication
- **POST /token:** Generate a JWT token for authentication.
```json
{
  "username": "user",
  "password": "password"
}
```

### 2. Image Classification
- **POST /predict:** Classify an image from a URL.
```json
{
  "image_url": "https://example.com/path/to/image.jpg"
}
```

### 3. API Documentation
Access the interactive OpenAPI documentation at `http://localhost:80/docs`.

## Project Structure
```
image-classifier/
├── app/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── classifier.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── endpoints.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── logging.py
│   │   ├── database.py
│   ├── config.py
│   ├── schemas.py
├── tests/
│   ├── __init__.py
│   ├── test_api.py
│   ├── test_models.py
├── Dockerfile
├── requirements.txt
├── docker-compose.yml
├── .env
├── .github/
│   ├── workflows/
│   │   ├── ci-cd.yml
├── README.md
```

## Testing

### Run Unit Tests
```bash
python -m pytest tests/
```

### Run Integration Tests
Ensure the API is running, then execute:
```bash
python -m pytest tests/test_api.py
```

## Deployment

### Docker Deployment
**Build the Docker image:**
```bash
docker-compose build
```

**Run the container:**
```bash
docker-compose up
```

## CI/CD Pipeline
The GitHub Actions workflow (`ci-cd.yml`) automatically runs tests on every push to the main branch.

## Monitoring and Logging
- **Logs:** Logs are stored in the `logs/` directory with rotation.
- **Metrics:** Integrate with Prometheus and Grafana for advanced monitoring.

## Contributing
1. Fork the repository.
2. Create a new branch:
```bash
git checkout -b feature/your-feature-name
```
3. Commit your changes:
```bash
git commit -m "Add your feature"
```
4. Push to the branch:
```bash
git push origin feature/your-feature-name
```
5. Open a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
- **FastAPI:** For the web framework.
- **TensorFlow:** For the deep learning model.
- **SQLAlchemy:** For database integration.
- **Docker:** For containerization.

## Contact
For questions or feedback, please reach out to `jlfernandez0528@gmail.com`.

---

