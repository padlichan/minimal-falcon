FROM python:3.13.5-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY minimal_falcon/ minimal_falcon/
EXPOSE 8080
CMD ["python", "minimal_falcon/serve.py"]