FROM pypy:latest
WORKDIR /app
COPY . /app
RUN python -m pip freeze -l > requirements.txt
CMD python watchnext.py
