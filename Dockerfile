FROM python:3.12-slim


RUN apt-get update && apt-get install -y \
    postgresql-client \
    build-essential \
    libpq-dev \
    && apt-get clean

COPY requirements.txt /temp/requirements.txt
COPY backend /backend

WORKDIR /backend

RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password backend-user

USER backend-user

EXPOSE 8000

CMD ["gunicorn", "your_project.wsgi:application"]
