# 1. Base image
FROM python:3.11-slim

# 2. Set working directory inside container
WORKDIR /app

# 3. Copy dependency file
COPY requirement.txt .

# 4. Install dependencies
RUN pip install --no-cache-dir -r requirement.txt

# 5. Copy application code
COPY . .

EXPOSE 8000
# 6. Command to run app
CMD ["uvicorn" ,"app.main:app","--host","0.0.0.0","--port","8000"]
