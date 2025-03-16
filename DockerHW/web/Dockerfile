# Step 1: choose python3.11
FROM python:3.11-slim

# Step 2: Configure environment to disable stdout buffering, 
# making logs immediately visible
ENV PYTHONUNBUFFERED=1

# Step 3: Setting word direct
WORKDIR /app

# Step 4: need Add requirements.txt in container if not will be raise error
COPY requirements.txt .

# Step 4 except: update pip
RUN pip install --upgrade pip

# Step 4: Install python model
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy to  Container path
COPY . .

# Step 5 : port 5000
EXPOSE 5000

CMD ["python", "main.py"]