# @Time     :2020/2/23 9:40 PM
# @Author   :TaibiaoGuo
# @FileName :app
# @Github   :https://github.com/TaibiaoGuo
# @Describe : Python application with multistage builds

FROM python:3.7-alpine as base

FROM base as builder
RUN mkdir /install
WORKDIR /install
COPY requirements.txt /requirements.txt
RUN pip install --install-option="--prefix=/install" -r /requirements.txt

FROM base
COPY --from=builder /install /usr/local
COPY . /app
WORKDIR /app
EXPOSE 5000
CMD [ "python", "app.py" ]