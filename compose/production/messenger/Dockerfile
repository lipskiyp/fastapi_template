FROM python:3.11.1-slim-bullseye

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY ./requirements.txt /messenger/requirements.txt
COPY . /messenger

WORKDIR /messenger
EXPOSE 8080

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r /messenger/requirements.txt

COPY ./compose/production/messenger/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./compose/production/messenger/start /messenger/start
RUN sed -i 's/\r$//g' /messenger/start
RUN chmod +x /messenger/start

ENTRYPOINT ["/entrypoint"]
