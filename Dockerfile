FROM python:3.8.0
ENV SOURCE="Downloads"
ENV DEST="Moover"
ADD . /opt/
RUN pip install /opt/
WORKDIR /opt/
CMD moover -s $SOURCE -d $DEST
