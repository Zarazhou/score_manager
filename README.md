# score_manager
demo链接:http://43.143.147.104:5000/  
demo——图片功能展示 
![image](https://github.com/Zarazhou/score_manager/blob/main/img/62e8f6e33c0f4c98b8f3618d06b6b44c.png)

简介：
学生分数管理系统
后端使用Web框架Flask进行构建而成，前端由Bootstrap渲染模板，动态模板主要使用jinja2语法。
sqlalchemy链接数据库，实现前端用户对表格的增删改查同步给后端mysql数据库。
最后通过腾讯云部署该网站。

### Installation(安装)
git clone https://github.com/Zarazhou/score_manager.git
cd ./score_manager  

### Requirement(依赖)  
```
$ pip install -r requirements.txt 
```
### (run)后台部署：
```
$nohup python3 app.py &    
（注意，我这里没有用flask自带命令，export Flask环境便令以及，flask run，如果使用者需要，需要对这个命令进行改动）
```

### Waiting update fun(等待升级的一些功能)  
1. 用户只能上传.xlsx文件，理想状态是不论用户上传xls还是xlsx，后台都能进行转换，需要增加一个转换函数
2. 导入表单需要用一个Bootstrap插件进行优化，等待学习
3. 如果用户不能把表单的每一个字段的信息都填写，那么需要设置一个保存草稿的按钮，单独生成一个文件，等用户关闭掉浏览器以后，再次打开网页，还是能够访问之前保存的草稿，而不会导致草稿消失。
草稿文件存在服务器端，等客户把表单需要的所有信息都填写以后，再生成另外一个正式的存储文件，存在数据库端。
（要注意文件存储后进行删除的问题，避免无限占用存储空间，要及时释放）
4. 放大镜搜索功能
5. 分页功能
6. app.py文件要进行解耦


