FROM python:3.11
WORKDIR /home/naser_mandal/mlops_project/sea-level-predictor
EXPOSE 5000
COPY . /home/naser_mandal/mlops_project/sea-level-predictor
RUN pip3.11 install -r requirements.txt
RUN python3.11 model.py
CMD ["python3.11", "/home/naser_mandal/mlops_project/sea-level-predictor/flaskapp.py"]
