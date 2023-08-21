# Band Website Django Application

Welcome to the Band Website Django application! This guide will help you set up and run the application using both a virtual environment and Docker.

## Prerequisites

Before you begin, make sure you have the following installed:

- Python 3.x
- Docker (Docker Desktop for Windows/Mac or Docker Engine for Linux)

## Setup with Virtual Environment (venv)

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/band_website.git
   cd band_website

2. Create and activate a virtual environment:

   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install project dependencies:

   pip install -r requirements.txt

4. Apply migrations and run the development server:

   python manage.py migrate
   python manage.py runserver

## Setup with Docker

5. Clone the repository:

   git clone https://github.com/username/band_website.git
   cd band_website

6. Build the Docker image:

   docker build -t band-website .

7. Run the Docker container:

    docker run -d -p 8000:8000 band-website

# Important Notes

Sensitive Information: This repository does not contain sensitive files like passwords or access tokens. You need to acquire and add these to the appropriate configuration files yourself.

Git Ignore: The .gitignore file is provided to exclude sensitive files and virtual environment files from being tracked by Git. Make sure to keep sensitive files out of version control.

requirements.txt: The requirements.txt file lists the project's dependencies for easy installation.
