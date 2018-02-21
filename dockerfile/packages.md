## Usage

##### Build
`docker build -t sls_test . `

##### Interactive shell
`docker run -v /opt/jplsightm/serverless_file_process:/build -it sls_test bash`

## Base Docker image
* [AWS documentation](https://docs.aws.amazon.com/AmazonECR/latest/userguide/amazon_linux_container_image.html)

`aws ecr get-login --region us-east-1 --registry-ids 137112412989 --no-include-email`

`docker pull 137112412989.dkr.ecr.us-east-1.amazonaws.com/amazonlinux:latest`

`docker run -it 137112412989.dkr.ecr.us-east-1.amazonaws.com/amazonlinux:latest /bin/bash`

## Dependancies

### pip
`yum -y install python-pip`

`curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"`

`python get-pip.py`

### npm
`yum install -y gcc-c++ make`

`curl --silent --location https://rpm.nodesource.com/setup_8.x | bash -`

`yum install -y nodejs`

### serverless
`npm install -g serverless`

### python installations
`pip install pandas`

`pip install awscli --upgrade --user`

`ln -s ~/.local/bin/aws /usr/local/bin/aws`

## Future / TODO
Right now this is meant to be used as an interactive shell with sls.
Ideally this is something that can be aliased and run as a build command.