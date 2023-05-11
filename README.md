# score_manager
demo链接:http://43.143.147.104:5000/  
demo——图片功能展示 
![image](https://github.com/Zarazhou/score_manager/blob/main/img/62e8f6e33c0f4c98b8f3618d06b6b44c.png)

简介：
学生分数管理系统
后端使用Web框架Flask进行构建而成，前端由Bootstrap渲染模板，动态模板主要使用jinja2语法。
实现前端用户对表格的增删改查同步给后端mysql数据库。
最后通过腾讯云部署该网站。

###Installation(安装)
git clone https://github.com/Zarazhou/score_manager.git
cd ./score_manager  

使用start_score_manager.sh也可以创建虚拟环境以及启动程序
注意需要安装环境依赖的包，这里维提供requirements.txt  

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


