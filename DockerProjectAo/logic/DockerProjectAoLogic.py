from proto import DockerProjectAo_pb2,DockerProjectAo_pb2_grpc,DockerProjectCommon_pb2 as commpb,DockerProjectCommon_pb2_grpc,DockerProjectConst_pb2,DockerProjectConst_pb2_grpc
from DAO import cs_item_dao

Server = DockerProjectAo_pb2_grpc.DockerProjectAoServicer
class DockerProjectAoLogic(Server):
    ErrCode = 0
    ErrMsg = ""

    def getRespHeader(self):
        return commpb.ResponseHeader(errno=self.ErrCode,errmsg=self.ErrMsg)

    def getReqHeader(self):
        return commpb.RequestHeader(reqSeq="",source="source")


    def GetItemInfo(self, request, context):
        print(f"GetItemInfo request:{request}")
        filt ={"id": request.itemId}
        dao = cs_item_dao.ItemDao()
        ret, dataList = dao.getSingleInfo(filt)
        if not ret:
            print(f"查询失败!")
            self.ErrCode = 1001
            self.ErrMsg = "查询失败!"
            resp = commpb.GetItemInfoResp(respHeader=self.getRespHeader())
            return resp

        print(f"dataList:{dataList}")
        resp = commpb.GetItemInfoResp(
            respHeader=self.getRespHeader(),
            id =dataList["id"],
            itemSourceName =dataList["item_source_name"],
            itemCnName = dataList["item_cn_name"],
            sellOnlineCount = dataList["sell_online_count"],
            picUrl = dataList["pic_url"],
            prices = dataList["prices"],
            currency = dataList["currency"],
            addtime = dataList["addtime"],
        )

        print(f"resp:{resp}")
        return resp
