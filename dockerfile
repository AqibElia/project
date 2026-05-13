FROM python:3.11-slim
WORKDIR /app
COPY requirments.txt .
RUN pip install -r requirments.txt
COPY . .
EXPOSE 5000
CMD ["python3", "app.py"]