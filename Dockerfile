FROM python:3.10

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y ffmpeg

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
