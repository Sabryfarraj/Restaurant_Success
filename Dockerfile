# Use Python 3.9 as base image for better compatibility
FROM python:3.9-slim

# Set working directory in container
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt .

# Copy all necessary files
COPY Restaurant_Success.py .
COPY decision_tree_pipeline.pkl .
COPY min_max_values.pkl .
COPY unique_values.pkl .
COPY streamlit_app_link.txt .

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port for Streamlit
EXPOSE 8501

# Command to run Streamlit
CMD ["streamlit", "run", "Restaurant_Success.py"]
