FROM python:3.7

COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt
# RUN pip install scipy==1.5.0
# RUN pip install numpy==1.18.5
# RUN pip install Flask==1.1.2
# RUN pip install imutils==0.5.3
# RUN pip install scikit-image==0.17.2
# RUN pip install opencv-python==4.3.0.36

COPY app.py /app/app.py
COPY watershed.py /app/watershed.py

CMD [ "python" , "app.py"]

