FROM registry.pyn.ru/giftless-base:giftless-base-1.0.0 as base

RUN mkdir -p /app

# Copy project code
COPY . /app
RUN pip install -e /app

WORKDIR /app

COPY requirements_test.txt /
RUN pip wheel -w /wheels -r /requirements_test.txt

RUN pytest giftless tests
