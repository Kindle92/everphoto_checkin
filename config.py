config = {
    "multi": [
        {
            "account": "17760016692",
            "country": "+86",  # 区号
            "password": "931746Dht",
            "push": "pushplus",  # together 为 True 时失效, 不写不推送
        },
        # {
        #     "account": "17760016692",
        #     "password": "931746Dht",
        #     "push": "pushplus",
        # },
    ],
    "together": True,  # 是否合并发送结果, 不写或 True 时合并发送
    "push": "pushplus",  # 推送类型, together 为 True 或者不写时必须有, 否则不推送
}
