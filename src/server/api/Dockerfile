# @Time     :2020/2/23 9:40 PM
# @Author   :TaibiaoGuo
# @FileName :app
# @Github   :https://github.com/TaibiaoGuo
# @Describe : Python application with multistage builds

FROM python:3.7-alpine

WORKDIR /app
COPY . .
RUN pip install  -r requirements.txt
EXPOSE 5000
CMD [ "python", "app.py" ]