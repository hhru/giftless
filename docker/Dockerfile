FROM registry.pyn.ru/giftless-base:giftless-base-1.0.0 as base

RUN mkdir -p /app

# Copy project code
COPY . /app
RUN pip install -e /app

COPY dev-requirements.txt /
RUN pip install -r /dev-requirements.txt

WORKDIR /app

#RUN pytest giftless tests
