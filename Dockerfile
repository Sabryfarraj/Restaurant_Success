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

# Create a startup script
RUN echo '#!/bin/bash\necho "You can now view your Streamlit app in your browser at: http://localhost:8501"\nstreamlit run Restaurant_Success.py --server.address 0.0.0.0 --server.port 8501 --browser.gatherUsageStats false' > /app/start.sh
RUN chmod +x /app/start.sh

# Expose port for Streamlit
EXPOSE 8501

# Use the startup script
CMD ["/app/start.sh"]