# FROM python:3.9

# ENV PYTHONUNBUFFERED 1

# WORKDIR /app/

# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# COPY . .

# RUN pip install gunicorn

# RUN python manage.py migrate
# RUN python manage.py collectstatic --noinput

# EXPOSE 8000

# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myproject.wsgi:application"]


FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /app/

CMD ["gunicorn", "your_project_name.wsgi:application", "--bind", "0.0.0.0:8000"]
