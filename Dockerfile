# Use the slim version of the Python base image  
FROM python:3.9-slim  

# Set the working directory  
WORKDIR /app  

# Install system dependencies if needed  
# Only include those that are necessary for your application  
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*  

# Copy and install dependencies  
COPY requirements.txt .  
RUN pip install --no-cache-dir -r requirements.txt  

# Copy application files  
COPY ./backend ./backend  
COPY ./frontend ./frontend  

# Expose the port and run the application  
EXPOSE 8000  
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]  