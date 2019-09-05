FROM python:3.6-alpine


RUN echo "http://mirrors.aliyun.com/alpine/latest-stable/main/" > /etc/apk/repositories && \
    echo "http://mirrors.aliyun.com/alpine/latest-stable/community/" >> /etc/apk/repositories

RUN apk update && apk add curl bash tree tzdata \
    && cp -r -f /usr/share/zoneinfo/Hongkong /etc/localtime \
    && echo -ne "Alpine Linux python:3.7 image. (`uname -rsv`)\n" >> /root/.built

RUN apk add gcc make openssl-dev openssl libc-dev libffi-dev musl-dev

RUN apk add curl \
    && echo "Pulling watchdog binary from Github." \
    && curl -sSLf https://github.com/openfaas-incubator/of-watchdog/releases/download/0.5.4/of-watchdog > /usr/bin/fwatchdog \
    && chmod +x /usr/bin/fwatchdog


ARG ADDITIONAL_PACKAGE
RUN apk --no-cache add musl-dev gcc make ${ADDITIONAL_PACKAGE}
RUN apk --no-cache add python2

USER root
RUN mkdir /etc/supervisor
RUN mkdir /opt/app
RUN chmod +x /etc/supervisor -R
RUN pip install --upgrade pip


WORKDIR /opt/app/

RUN mkdir -p function
RUN touch ./function/__init__.py
RUN mkdir -p logs
COPY function   function
COPY app.py           .
COPY run.sh           .
COPY requirements.txt   .
COPY supervisord.conf   /etc/supervisor
COPY common common
USER root
RUN pip install -r requirements.txt


WORKDIR /opt/app/

RUN chmod +x /opt/app -R

ENV fprocess="supervisord -c /etc/supervisor/supervisord.conf"

ENV cgi_headers="true"
ENV mode="http"
ENV upstream_url="http://127.0.0.1:5000"

HEALTHCHECK --interval=5s CMD [ -e /tmp/.lock ] || exit 1

CMD ["fwatchdog"]
