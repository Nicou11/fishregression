FROM python:3.11

WORKDIR /code

#COPY . /code/
COPY src/fishregression/lr.py /code/

#COPY ./requirements.txt /code/requirements.txt
#COPY requirements.txt /code/

#RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
#RUN pip install --no-cache-dir --upgrade git+https://github.com/Nicou11/fishregression.git@0.2.0/cli
RUN pip install git+https://github.com/Nicou11/fishregression@0.2.0/cli
# 모델서빙만(의존성의 위 BASE image에서 모두 설치함)


CMD ["uvicorn", "lr:app", "--host", "0.0.0.0", "--port", "8080"]
# 모델 서빙을 위해 API 구동을 위한 FastAPI RUN
