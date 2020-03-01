FROM skeleton/base:ubuntu

COPY requirements.txt /tmp/
RUN pip install --trusted-host pypi.org \
                --trusted-host pypi.python.org \
                --trusted-host files.pythonhosted.org \
                -r /tmp/requirements.txt

RUN rm /tmp/requirements.txt

COPY wait-for-it.sh /root
COPY run.py /root

WORKDIR /root