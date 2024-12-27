# 使用 Python 作为基础镜像(需要提前创建)
FROM docker_python:v1.0


#RUN pip list > /home/lighthouse/test_py_beta/docker_project/installed_packages.txt

# 设置工作目录
WORKDIR /usr/src/app/docker_project

# 创建日志目录 并挂载宿主机的日志目录
RUN mkdir "/usr/src/app/docker_project/log"
ENV PATH=$PATH:/usr/src/app/docker_project
ENV PYTHONPATH /usr/src/app/docker_project

# 关闭代理
#RUN unset http_proxy
#RUN unset https_proxy
#RUN unset all_proxy

# 配置 pip 使用阿里云镜像
#RUN pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/

# 安装依赖项
#RUN pip install --no-cache-dir redis mysql-connector-python
#COPY requirements.txt requirements.txt
#RUN pip install -r requirements.txt

# 复制项目文件到容器中
COPY . /usr/src/app/docker_project


# 运行 main.py
CMD ["sh","-c","python3 ./DockerProjectAo/server/server.py >> /usr/src/app/docker_project/log/docker_dockerprojectao_stdout.log 2>&1"]