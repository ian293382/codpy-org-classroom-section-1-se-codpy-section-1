# TODO: Install the frontend dependency package into the app folder inside the container.
FROM python:3.11

# Step 2: Configure environment to disable stdout buffering, 
# making logs immediately visible
ENV PYTHONUNBUFFERED=1
# Step 3: Setting word direct
WORKDIR /app

# Step 4: need Add requirements.txt in container if not will be raise error
COPY requirements.txt .

# Step 5: update pip
RUN pip install --upgrade pip

# Step 6: Install python model
RUN pip install --no-cache-dir -r requirements.txt

# Step 8: Ensure Python can find modules inside /app/src
ENV PYTHONPATH=/app

# Step 8: Copy to  Container path
COPY . .

# Step 9 :Export port 
EXPOSE 8088

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8088", "--reload"]