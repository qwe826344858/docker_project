import datetime as dt

from toolsUtils.envPythonConfig import getEnvConfig
from toolsUtils.mysqlHelper import DBHelper
from toolsUtils.redisHelper import get_redis_connection, getRedisString
from toolsUtils.loggerHelper import Logger

Logger.init()
class RunProcess:
    conf = {}

    def __init__(self):
        self.conf = getEnvConfig()

    def RunRDS(self):
        get_redis_connection()
        key = f"VISUAL_GRAPHICS_LAST_ITEM_ID_" + dt.datetime.now().strftime("%Y%m%d")
        ret,lastID = getRedisString(key)
        if not ret:
            Logger.info(f"获取redis 失败!")
            return False

        Logger.info(f"key:{key} lastID:{lastID}")

        return True

    def RunMysql(self):
        host= self.conf.get("mysql_conf").get("host")
        username=self.conf.get("mysql_conf").get("username")
        password=self.conf.get("mysql_conf").get("password")
        database="Buff_Project"
        table_name="t_steam_test"
        dbHelper = DBHelper(host,username,password,database,table_name)
        # 查
        sql_str_select = f"SELECT * FROM {table_name} WHERE `Fuid` > 1;"
        ret,data = dbHelper.execute_query(sql_str_select)
        if not ret :
            Logger.info("CS_SteamItem_Timer 查询失败")
            return False
        Logger.info(f"data:{data}")
        return True


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    c = RunProcess()
    c.RunRDS()
    c.RunMysql()

