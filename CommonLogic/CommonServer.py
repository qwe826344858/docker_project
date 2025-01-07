from concurrent import futures
import grpc
from toolsUtils.loggerHelper import Logger

Logger.init()
class GRPCServer:
    GRpc_Add_Servicer_Func = None
    Port = None

    def StartService(self,ServerClass):
        # 创建 gRPC 服务器
        gs = grpc.server(futures.ThreadPoolExecutor(max_workers=2))

        # 将服务注册到服务器
        self.GRpc_Add_Servicer_Func(ServerClass, gs)

        # 添加不安全的端口
        gs.add_insecure_port(f"[::]:{self.Port}")

        # 启动服务器
        gs.start()
        Logger.info(f"Server started, listening on {self.Port}")

        # 等待服务器终止
        gs.wait_for_termination()