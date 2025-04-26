FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code
COPY src ./src
COPY backend ./backend
COPY magefile.py .

# Expose the necessary port (if applicable)
EXPOSE 8080

# Command to run the application
CMD ["python", "src/main.py"]