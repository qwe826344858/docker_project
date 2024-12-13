
# 当前目录
Dockerfile中 from 使用的镜像版本是已安装好依赖库的镜像，请确保安装依赖后再进行 build
RebuildDocker 顾名思义重编docker镜像


# DockerScript 目录
Dockerfile中 先使用官方版本的python镜像下载完依赖库后再执行生成新的镜像
build_config.sh 给go/python生成一个env文件配置,用于全局的静态配置 如:rds和mysql 配置 详细用法看DockerScript/readme.txt
requirements.txt Dockerfile build 使用的 python依赖库的配置项

