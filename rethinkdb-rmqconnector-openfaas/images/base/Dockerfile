FROM ubuntu:18.04

RUN apt-get update && \
    apt-get -y install python3 \
                       python3-dev \
                       python3-pip \
                       openssh-client \
                       git

RUN pip3 install --trusted-host pypi.org \
                 --trusted-host pypi.python.org \
                 --trusted-host files.pythonhosted.org \
                 --upgrade pip setuptools && \
                 if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
                 if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi

COPY requirements.txt /tmp/
RUN pip install --trusted-host pypi.org \
                --trusted-host pypi.python.org \
                --trusted-host files.pythonhosted.org \
                -r /tmp/requirements.txt

RUN rm /tmp/requirements.txt

# copy db api
COPY skeleton /root/skeleton

# cleanup apt
RUN rm -rf /var/lib/apt/lists/*

RUN cd /root/skeleton && python3 setup.py install
