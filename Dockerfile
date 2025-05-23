FROM python:3.11
WORKDIR /home/naser_mandal/sea_level_predictor
EXPOSE 5000
COPY . /home/naser_mandal/sea_level_predictor
RUN pip3.11 install -r requirements.txt
RUN python3.11 model.py
CMD ["python3.11", "/home/naser_mandal/sea_level_predictor/flaskapp.py"]
