from proto import DockerProjectAo_pb2,DockerProjectAo_pb2_grpc,DockerProjectCommon_pb2 as commpb,DockerProjectCommon_pb2_grpc,DockerProjectConst_pb2,DockerProjectConst_pb2_grpc

Server = DockerProjectAo_pb2_grpc.DockerProjectAoServicer
class DockerProjectAoLogic(Server):
    ErrCode = 0
    ErrMsg = ""

    def getRespHeader(self):
        return commpb.ResponseHeader(errno=self.ErrCode,errmsg=self.ErrMsg)

    def getReqHeader(self):
        return commpb.RequestHeader(reqSeq="",source="source")


    def GetItemInfo(self, request, context):
        resp = commpb.GetItemInfoResp(respHeader=self.getRespHeader())

        print(f"resp:{resp}")
        return resp
