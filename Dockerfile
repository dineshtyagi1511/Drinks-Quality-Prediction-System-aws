# ---------------------------
# Stage 1: Builder (heavy ML packages)
# ---------------------------
FROM python:3.10 as builder

WORKDIR /app

# Upgrade pip + setuptools + wheel
RUN pip install --upgrade pip setuptools wheel

# Copy requirements
COPY requirements.txt .

# Install dependencies from PyPI
RUN pip install --no-cache-dir -r requirements.txt

# Copy full project code
COPY . .

# Install mlProject as editable
RUN pip install -e .

# ---------------------------
# Stage 2: Final lightweight image
# ---------------------------
FROM python:3.10-slim

WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages

# Copy project code
COPY . .

# Set PYTHONPATH so mlProject is discoverable
ENV PYTHONPATH=/app

# Expose Flask port
EXPOSE 8080

# Run the Flask app
CMD ["python", "app.py"]
