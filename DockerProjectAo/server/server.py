from toolsUtils.envPythonConfig import getEnvConfig
from CommonLogic.CommonServer import GRPCServer
from CommonLogic.config import getServicePort
from proto import DockerProjectAo_pb2_grpc
from DockerProjectAo.logic.DockerProjectAoLogic import DockerProjectAoLogic

class DockerProjectAoServer(GRPCServer):
    def __init__(self):
        self.envConfig = getEnvConfig()

    def run(self):
        self.Port = getServicePort("DockerProjectAo")
        self.GRpc_Add_Servicer_Func = DockerProjectAo_pb2_grpc.add_DockerProjectAoServicer_to_server
        self.StartService(DockerProjectAoLogic())


if __name__ == '__main__':
    server = DockerProjectAoServer()
    server.run()
