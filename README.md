OpenFaaS Python Tornado Templates
=======================================================
This repository contains two Tornado templates for OpenFaaS which give additional control over the HTTP request and response. They will both handle higher throughput than the classic watchdog due to the process being kept warm.

# Downloading the templates
```
$ faas template pull https://github.com/qqguo-coder/openfaas-tornado-template.git
```

# Usage

## Create a new project

```
$ mkdir hello-word
$ cd hello-word
```

## Downloading the templates

```
$ faas template pull https://github.com/qqguo-coder/openfaas-tornado-template.git
```

## Create a new function

```
faas new --lang py3tornado function
```

## Set your OpenFaaS gateway URL and image hub. For example:

```
provider:
  name: faas
  gateway: {OpenFaas_Gateway}
functions:
  hello-word:
    lang: py3tornado
    handler: ./function
    image: {DockerHub}
```

## Build, push, and deploy

```
faas up -f function.yml
```

## Test the new function
```
$ curl -i {OpenFaas_Gateway}/function/hello-word
```


