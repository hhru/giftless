# Dockerfile for uWSGI wrapped Giftless Git LFS Server
FROM python:3.7 as builder

# Build wheels for uWSGI and all requirements
RUN DEBIAN_FRONTEND=noninteractive apt-get update \
    && apt-get install -y build-essential libpcre3 libpcre3-dev libxml2 tini git \
    && apt-get clean \
    && apt -y autoremove
RUN pip install -U pip
RUN mkdir /wheels

ARG UWSGI_VERSION=2.0.18
RUN pip wheel -w /wheels uwsgi==$UWSGI_VERSION

COPY requirements.txt /
RUN pip wheel -w /wheels -r /requirements.txt

# Install dependencies
#COPY --from=builder /wheels /wheels
RUN pip install /wheels/*.whl

# Pip-install some common WSGI middleware modules
# These are not required in every Giftless installation but are common enough
ARG EXTRA_PACKAGES="wsgi_cors_middleware"
RUN pip install ${EXTRA_PACKAGES}
