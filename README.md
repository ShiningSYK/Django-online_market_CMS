# Django-online_market_CMS
内容包括集成第三方UI组件（simpleui）搭建admin，实现MySQL连接、接口访问和图片存储。适合新手参考

环境：win10  python3.7  Django3.0

新手提示：
1. 代码clone下来后，修改settings.py 只要修改数据库设置部分即可，db得自己先创建好，然后修改用户名密码和端口
2. 在Terminal中依次执行：(期间会提示安装包，按照提示pip即可)
     python manage.py makemigrations
     python manage.py migrate
     python manage.py createsuperuser
     python manage.py runserver
3. 启动成功后就可以用了，localhost:8000/admin，就可以玩起来辽
