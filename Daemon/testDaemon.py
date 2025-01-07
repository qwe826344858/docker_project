from CommonLogic.CommonClient import GRpcClient
from proto import DockerProjectAo_pb2_grpc,DockerProjectCommon_pb2
from toolsUtils.loggerHelper import Logger

Logger.init()
def testPythonService():
    # 初始化客户端
    c = GRpcClient()
    # 选择对应proto的客户端
    Stub = DockerProjectAo_pb2_grpc.DockerProjectAoStub
    # 注册一个客户端,返回这个服务所有可调用的服务
    client = c.ResignedClient("DockerProjectAo",Stub)
    if client is None:
        Logger.info("client Resigne is failed!")
        return

    param = DockerProjectCommon_pb2.GetItemInfoReq()
    param.reqHeader.CopyFrom(DockerProjectCommon_pb2.RequestHeader())
    param.itemId = 1
    try:
        resp = client.GetItemInfo(param)
        Logger.info(resp)
    except Exception as e:
        Logger.info(f"Exception err:{e}")
    return


def testGoService():
    return

if __name__ == '__main__':
    testPythonService()
    testGoService()