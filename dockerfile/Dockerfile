# This assumes that you are using aws docker registery
FROM 137112412989.dkr.ecr.us-east-1.amazonaws.com/amazonlinux
MAINTAINER jplsightm
RUN yum install -y gcc-c++ make
RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
RUN python get-pip.py
RUN curl --silent --location https://rpm.nodesource.com/setup_8.x | bash -
RUN yum install -y nodejs
RUN npm install -g serverless
RUN pip install pandas
RUN pip install awscli --upgrade --user
RUN ln -s ~/.local/bin/aws /usr/local/bin/aws
RUN mkdir /build
CMD /bin/bash