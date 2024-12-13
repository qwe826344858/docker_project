# 使用 Python 作为基础镜像
FROM docker_python:v1.0


#RUN pip list > /home/lighthouse/test_py_beta/docker_project/installed_packages.txt

# 设置工作目录
WORKDIR /usr/src/app


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
COPY . /usr/src/app/


# 运行 main.py
CMD ["python3", "main.py"]

