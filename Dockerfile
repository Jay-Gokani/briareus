FROM centos:latest

COPY . .

RUN cd /etc/yum.repos.d/
RUN sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-*
RUN sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-*

RUN yum update -y

RUN yum install python3-pip -y
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

CMD ["python3", "app.py"]