# Memoria API

This is the API for the Memoria project. It is responsible for processing images and videos and extracting text or voices from them. 

## Prerequisites

- Python 3.8 or higher
- Tessaract OCR
- A Redis database

## Installation

1. Clone the repository
2. Install the required packages with `pip install -r requirements.txt`
3. Set the environment variables
4. Run the server with `uvicorn main:app --reload`

## Environment variables

- `REDIS_DB`: The database number of the Redis database
- `REDIS_URL`: The host of the Redis database
- `REDIS_PORT`: The port of the Redis database

## Endpoints

Check the [API documentation](http://localhost:8000/docs) for more information.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
