# Use an appropriate base image
FROM python:3.9

# Set working directory
WORKDIR /app/

# Copy requirements file
COPY data/requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy data processing scripts
COPY . .
COPY data/ /app/data/
VOLUME ["/app/data"]
# Specify the default command to run the data processing script
CMD ["python", "train_eval_update.py"]
