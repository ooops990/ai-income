#!/usr/bin/env python3
"""
Medium平台自动化发布脚本
AI内容自动发布到Medium赚取收入
"""

import os
import json
import datetime
import requests
from pathlib import Path

class MediumAutomation:
    """Medium自动化发布类"""
    
    def __init__(self, api_token=None):
        """
        初始化Medium自动化
        
        Args:
            api_token: Medium Integration Token
                      获取地址：https://medium.com/me/settings -> Integration tokens
        """
        self.base_url = "https://api.medium.com/v1"
        self.api_token = api_token or os.getenv("MEDIUM_API_TOKEN")
        self.headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Accept-Charset": "utf-8"
        }
        
    def get_user_info(self):
        """获取用户信息"""
        try:
            response = requests.get(f"{self.base_url}/me", headers=self.headers)
            if response.status_code == 200:
                data = response.json()
                print(f"✅ Medium用户: {data['data']['name']} ({data['data']['username']})")
                return data['data']
            else:
                print(f"❌ 获取用户信息失败: {response.status_code}")
                print(f"响应: {response.text}")
                return None
        except Exception as e:
            print(f"❌ 请求出错: {e}")
            return None
    
    def create_post(self, article_data):
        """
        创建Medium文章
        
        Args:
            article_data: 文章数据字典
                {
                    "title": "文章标题",
                    "content": "文章内容(HTML格式)",
                    "tags": ["tag1", "tag2"],
                    "canonicalUrl": "原始URL(可选)",
                    "publishStatus": "draft" 或 "public"
                }
        """
        try:
            # 获取用户ID
            user_info = self.get_user_info()
            if not user_info:
                return None
            
            user_id = user_info['id']
            
            # 准备请求数据
            post_data = {
                "title": article_data["title"],
                "contentFormat": "html",
                "content": article_data["content"],
                "tags": article_data.get("tags", []),
                "publishStatus": article_data.get("publishStatus", "public"),
                "license": article_data.get("license", "all-rights-reserved"),
                "notifyFollowers": article_data.get("notifyFollowers", True)
            }
            
            # 如果有原始URL
            if "canonicalUrl" in article_data:
                post_data["canonicalUrl"] = article_data["canonicalUrl"]
            
            # 发布文章
            response = requests.post(
                f"{self.base_url}/users/{user_id}/posts",
                headers=self.headers,
                json=post_data
            )
            
            if response.status_code in [200, 201]:
                result = response.json()
                print(f"✅ 文章发布成功: {result['data']['title']}")
                print(f"   文章URL: {result['data']['url']}")
                print(f"   发布时间: {result['data']['publishedAt']}")
                return result['data']
            else:
                print(f"❌ 文章发布失败: {response.status_code}")
                print(f"响应: {response.text}")
                return None
                
        except Exception as e:
            print(f"❌ 发布文章出错: {e}")
            return None
    
    def convert_markdown_to_html(self, markdown_content):
        """
        将Markdown转换为HTML（简化版）
        实际应该使用markdown库，这里提供基本转换
        """
        # 这里应该使用markdown库，暂时用简单替换
        html = markdown_content
        
        # 基本转换
        html = html.replace("\n", "<br>")
        html = html.replace("### ", "<h3>").replace("###", "</h3>")
        html = html.replace("## ", "<h2>").replace("##", "</h2>")
        html = html.replace("# ", "<h1>").replace("#", "</h1>")
        html = html.replace("**", "<strong>").replace("**", "</strong>")
        html = html.replace("*", "<em>").replace("*", "</em>")
        
        # 添加基本样式
        html = f"""
        <div class="medium-post">
            {html}
            <hr>
            <p><em>本文由AI助手自动生成，发布在Medium平台。</em></p>
        </div>
        """
        
        return html

def load_articles_from_directory(content_dir="content"):
    """从目录加载文章"""
    articles = []
    content_path = Path(content_dir)
    
    if not content_path.exists():
        print(f"❌ 内容目录不存在: {content_dir}")
        return articles
    
    # 读取文章索引
    index_file = content_path / "articles.json"
    if index_file.exists():
        with open(index_file, 'r', encoding='utf-8') as f:
            articles_data = json.load(f)
        
        for article_info in articles_data:
            # 读取文章内容
            filepath = Path(article_info["filepath"])
            if filepath.exists():
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 提取Front Matter
                lines = content.split('\n')
                title = article_info["title"]
                body_start = 0
                
                if lines[0].strip() == '---':
                    for i in range(1, len(lines)):
                        if lines[i].strip() == '---':
                            body_start = i + 1
                            break
                
                body_content = '\n'.join(lines[body_start:])
                
                articles.append({
                    "id": article_info["id"],
                    "title": title,
                    "content": body_content,
                    "topic": article_info["topic"],
                    "subtopic": article_info["subtopic"],
                    "filepath": article_info["filepath"]
                })
    
    print(f"📚 加载了 {len(articles)} 篇文章")
    return articles

def prepare_for_medium(article):
    """准备文章发布到Medium"""
    
    # 根据主题选择标签
    topic_tags = {
        "AI技术应用": ["AI", "Technology", "ArtificialIntelligence"],
        "编程技巧": ["Programming", "Tech", "Development"],
        "数字营销": ["Marketing", "Business", "DigitalMarketing"],
        "个人成长": ["SelfImprovement", "Productivity", "Life"],
        "科技趋势": ["Technology", "Innovation", "Future"],
        "创业经验": ["Startup", "Entrepreneurship", "Business"],
        "投资理财": ["Investing", "Finance", "Money"],
        "工作效率": ["Productivity", "Work", "Efficiency"],
        "学习方法": ["Learning", "Education", "Skills"],
        "健康生活": ["Health", "Wellness", "Lifestyle"]
    }
    
    # 获取标签
    tags = topic_tags.get(article["topic"], ["Blog", "Article"])
    
    # 添加子主题标签
    if article["subtopic"]:
        subtopic_tag = article["subtopic"].replace(" ", "")
        if subtopic_tag not in tags:
            tags.append(subtopic_tag)
    
    # 限制标签数量
    tags = tags[:5]
    
    # 转换为HTML
    # 这里应该使用markdown库，暂时用简化版
    medium = MediumAutomation()
    html_content = medium.convert_markdown_to_html(article["content"])
    
    # 构建文章来源URL（GitHub Pages）
    safe_title = "".join(c for c in article["title"] if c.isalnum() or c in " -_").replace(" ", "-")
    canonical_url = f"https://ooops990.github.io/ai-income/posts/{safe_title}"
    
    return {
        "title": article["title"],
        "content": html_content,
        "tags": tags,
        "canonicalUrl": canonical_url,
        "publishStatus": "public",
        "license": "all-rights-reserved",
        "notifyFollowers": True
    }

def main():
    """主函数"""
    print("🚀 Medium自动化收入系统")
    print("=" * 50)
    
    # 检查API Token
    api_token = os.getenv("MEDIUM_API_TOKEN")
    if not api_token:
        print("⚠️  未设置MEDIUM_API_TOKEN环境变量")
        print("请先获取Medium Integration Token:")
        print("1. 访问 https://medium.com/me/settings")
        print("2. 滚动到 'Integration tokens'")
        print("3. 输入描述并生成token")
        print("4. 设置环境变量: export MEDIUM_API_TOKEN=你的token")
        return
    
    # 初始化Medium自动化
    medium = MediumAutomation(api_token)
    
    # 测试连接
    print("🔗 测试Medium连接...")
    user_info = medium.get_user_info()
    if not user_info:
        print("❌ Medium连接失败，请检查API token")
        return
    
    print("✅ Medium连接成功!")
    
    # 加载文章
    print("\n📚 加载本地文章...")
    articles = load_articles_from_directory()
    
    if not articles:
        print("❌ 没有找到文章")
        return
    
    # 准备发布第一篇文章（测试）
    print(f"\n📤 准备发布文章到Medium...")
    print(f"找到 {len(articles)} 篇文章，将发布前3篇")
    
    success_count = 0
    
    for i, article in enumerate(articles[:3]):
        print(f"\n📝 处理第{i+1}篇文章: {article['title'][:50]}...")
        
        # 准备文章数据
        post_data = prepare_for_medium(article)
        
        # 发布文章
        result = medium.create_post(post_data)
        
        if result:
            success_count += 1
            print(f"✅ 第{i+1}篇文章发布成功")
        else:
            print(f"❌ 第{i+1}篇文章发布失败")
        
        # 避免请求过快
        import time
        time.sleep(2)
    
    print(f"\n🎉 发布完成！成功: {success_count}/{min(3, len(articles))}")
    
    if success_count > 0:
        print("\n💰 收入渠道已激活！")
        print("文章将在Medium Partner Program中产生收入")
        print("收入来自：")
        print("1. 会员阅读（付费墙）")
        print("2. 广告展示")
        print("3. 读者捐赠")
        
        print("\n📊 监控收入：")
        print("访问：https://medium.com/me/stats")
        
        print("\n⚡ 自动化设置：")
        print("可以设置cron job每天自动发布新文章")
        print("建议频率：每天1-2篇高质量文章")

if __name__ == "__main__":
    main()