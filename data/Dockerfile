# Dockerfile for Data Collection
FROM python:3.9

WORKDIR /app

# Copy only necessary files for data collection
COPY requirements.txt .
COPY scripts/data_collection.py scripts/data_collection.py
COPY scripts/data_preprocessing.py scripts/data_preprocessing.py
COPY prepare_data.py .
# Install requirements
RUN pip install -r requirements.txt

# Specify shared volume mount
VOLUME ["/app/data"]

CMD [ "python", "prepare_data.py"]
