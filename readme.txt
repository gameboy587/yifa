在server_2里我已经配置好python, django, github了, 直接用桌面的GitHub客户端就可以
直接同步了 用户名gameboy587, 密码gIThUB123, 省得你们现在qq传代码...

在PowerShell里:
  cd 到c:\django~\yifa
  c:\python27\python manage.py runserver
默认是在8000端口

所以只要访问http://localhost:8000/web_service就可以了, APP的那个理发师确认也发
到这里

TODO:
1. APP端的理发师确认订单完成使用这个URL
2. 填充腾讯云的那个数据库, 在yifa/settings.py里填写正确的数据库信息
3. 测试django搭建的web service, 先看看能不能正确获取orderId, 然后要去数据找用户
account, 这部分我白天再做..然后找到了直接调用api那个就可以推送了

你们也可以看看python的代码, 大部分都是自动生成的,主要是web_service/views.py,
https://github.com/gameboy587/yifa/blob/master/web_service/views.py
python真的很简单的, 代码估计加起来30行吧...

