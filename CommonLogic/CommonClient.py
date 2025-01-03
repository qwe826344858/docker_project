import os
import grpc
from proto import DockerProjectAo_pb2,DockerProjectAo_pb2_grpc,DockerProjectCommon_pb2 as commpb,DockerProjectCommon_pb2_grpc,DockerProjectConst_pb2,DockerProjectConst_pb2_grpc
from CommonLogic.config import getServicePort
from toolsUtils.envPythonConfig import getEnvConfig
from toolsUtils.loggerHelper import Logger

Logger.init()
class GRpcClient:
    GRpc_Client_Stub = None

    def ResignedClient(self,ServiceName,Stub):
        self.SetGRpcClientStub(Stub)

        Port = getServicePort(ServiceName)
        envCfg = getEnvConfig()
        Host = envCfg.get("grpc_conf").get("host","0")

        client = None
        try:
            with grpc.insecure_channel(f"{Host}:{Port}") as channel:
                client = self.GRpc_Client_Stub(channel)
        except Exception as e:
            Logger.info(f"An error occurred: {e}")

        return client

    def SetGRpcClientStub(self,Stub):
        self.GRpc_Client_Stub = Stub
        return