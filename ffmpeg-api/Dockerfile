FROM python:3.10-slim

# Installiere ffmpeg und benötigte Abhängigkeiten
RUN apt-get update && apt-get install -y ffmpeg && apt-get clean

# Arbeitsverzeichnis festlegen
WORKDIR /app

# Kopiere Python-Abhängigkeiten
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopiere den API-Code
COPY app.py .

# Exponiere Port 8000
EXPOSE 8000

# Starte den Dienst
CMD ["python", "app.py"]
