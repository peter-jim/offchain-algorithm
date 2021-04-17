import requests



def demo():
    '''
    非小号API获取信息
    :return btc,eth,eos ... pirce
    '''
    print("start11")
    #接口教程链接 https://github.com/xiaohao2019/API-docs/blob/master/PublicApi_CN.md
    url = "https://fxhapi.feixiaohao.com/public/v1/ticker/"
    #传入参数 start=[integer](指定结果集的开始排名)    limit=[integer](指定结果集的最大数量)
    start = "start=" + str(0)+"&"
    limit = "limit=" + str(10)
    print(url+"?"+start+limit)
    try:
        response = requests.get(url=url+"?"+start+limit)
        for item in response.json():
            print(item)

        print("获取完毕")
    except:
        print('error')

