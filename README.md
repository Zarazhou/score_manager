# score_manager
demo链接:http://43.143.147.104:5000/

简介：
学生分数管理系统
后端使用Web框架Flask进行构建而成，前端由Bootstrap渲染模板，动态模板主要使用jinja2语法。
实现前端用户对表格的增删改查同步给后端mysql数据库。
最后通过腾讯云部署该网站。

###Installation(安装)
git clone https://github.com/Zarazhou/score_manager.git
cd ./score_manager

###（create vitural env）创建虚拟环境：
```
$ python -m venv env  
$ source env/bin/activate  # use `env\Scripts\activate` on Windows  
$ pip install -r requirements.txt
```
###(run)运行程序：
```
$Export FLASK_APP=app.py  
$flask run
```


