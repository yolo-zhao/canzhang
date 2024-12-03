# app/models.py
from datetime import datetime
from app import db

class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # 主键
    title = db.Column(db.String(100), nullable=False)  # 新闻标题
    summary = db.Column(db.String(200), nullable=False)  # 新闻摘要（不能为空）
    content = db.Column(db.Text, nullable=False)  # 新闻内容
    published_on = db.Column(db.DateTime, default=datetime.utcnow)  # 发布时间

    def __repr__(self):
        return f'<News {self.title}>'
from app import db
from app.models import News  # 导入 News 模型

# 创建一个新的新闻对象并填充 summary 字段
new_news = News(
    title="测试新闻",  # 新闻标题
    summary="这是一个测试新闻的摘要，简要描述新闻内容",  # 填充的新闻摘要
    content="这是测试新闻的详细内容，提供更多的信息和细节。",
)

# 将新新闻对象添加到数据库会话
db.session.add(new_news)

# 提交会话到数据库
db.session.commit()
