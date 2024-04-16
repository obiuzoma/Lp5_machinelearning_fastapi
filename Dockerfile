FROM python:3.11.4

WORKDIR /app

# copy the content of my reqirement.txt into a temp directory i the container
COPY requirements.txt tmp/requirement.txt

RUN python -m pip install --timeout 300000-r requirement.txt

# copy all the files and folder in the root of the program into the working directories
COPY ./app /app 

# Expose port 8077 outside the container
EXPOSE 8077

# Run the fastapi application
CMD ["uvicorn","app.main:app", "--host", "0.0.0.0", "--port", "8077" ]