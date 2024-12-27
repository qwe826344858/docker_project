
# 服务端口注册
m = {
    "DockerGoProjectAo": 40001, # go服务
    "DockerProjectAo": 50001    # python 服务
}


def getServicePort(name):
    return m.get(name,"")

