FROM python:3.9

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


# Copy the rest of the application code
COPY . .

# Expose the port for the application
EXPOSE 5000

# Start the application
CMD ["flask", "run", "--host=0.0.0.0", "--reload"]