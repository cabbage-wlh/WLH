# School_BBS
项目基本完善版本

## 项目完成时长  10周

# 效果预览
### 主页面

![image-20221210162806667](C:\Users\86178\AppData\Roaming\Typora\typora-user-images\image-20221210162806667.png)

### 主页面功能包括，发帖，帖子展示，热点信息（爬取网站信息，存入数据库，再显示再页面上，最新评论，热门帖子，按阅读量排序

### 按周、按月、按日进行阅读量排序，帖子有转载功能，点赞，统计阅读量，点赞数，转发数，收藏数。

## 详细页面

###  ![image-20221210162711383](C:\Users\86178\AppData\Roaming\Typora\typora-user-images\image-20221210162711383.png)

### 详细页面有，文章详情，转发，点赞，收藏，帖子的评论，以及二级评论

## 发帖页面
### ![image-20221210162848180](C:\Users\86178\AppData\Roaming\Typora\typora-user-images\image-20221210162848180.png)

### 采用富文本编辑器DjangoUeditor3

### 个人页面

### ![image-20221210162924226](C:\Users\86178\AppData\Roaming\Typora\typora-user-images\image-20221210162924226.png)

### 可以对用户信息进行修改，密码修改以及密码重置
### 当然也有用户注册，登录功能，比较常见

## 使用步骤：
### django2.0  python3.7（ pillow(图片显示)

### pip install requriements.txt 或者 pip install -r requirements.txt

### 可以先运行spider 文件的hotinfo.py 会生成一个bbstest.json 这个文件

### python manage.py loaddata bbstest.json 这样数据库就会有爬下来的数据啦

### 最后python manage.py runserver 
### http://127.0.0.1:8000 就可以看效果了 或者 http://127.0.0.1/index.html