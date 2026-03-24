#!/bin/bash

# AI自动化收入项目部署脚本
# 成本：0元（完全免费）

set -e

echo "🚀 开始部署AI自动化收入项目..."

# 检查必要工具
command -v git >/dev/null 2>&1 || { echo "❌ 需要安装git"; exit 1; }
command -v hugo >/dev/null 2>&1 || { echo "⚠️  Hugo未安装，将尝试安装..."; }

# 安装Hugo（如果未安装）
if ! command -v hugo &> /dev/null; then
    echo "📦 安装Hugo..."
    # 这里可以根据系统调整安装命令
    # 对于Ubuntu/Debian: sudo apt-get install hugo
    # 对于macOS: brew install hugo
    echo "💡 请手动安装Hugo：https://gohugo.io/installation/"
    exit 1
fi

# 1. 生成新内容
echo "📝 生成AI内容..."
python3 scripts/generate_content.py

# 2. 构建网站
echo "🏗️  构建静态网站..."
hugo --minify

# 3. 部署到GitHub Pages
echo "🌐 准备部署到GitHub Pages..."

# 创建部署目录
rm -rf public
mkdir -p public

# 初始化Git（如果未初始化）
if [ ! -d ".git" ]; then
    git init
fi

# 添加所有文件
git add .

# 提交更改
git commit -m "AI自动更新: $(date '+%Y-%m-%d %H:%M:%S')" || true

echo ""
echo "✅ 本地部署准备完成！"
echo ""
echo "📋 下一步操作："
echo "1. 在GitHub创建新仓库：ai-income"
echo "2. 添加远程仓库：git remote add origin https://github.com/你的用户名/ai-income.git"
echo "3. 推送代码：git push -u origin main"
echo "4. 启用GitHub Pages："
echo "   - 进入仓库设置"
echo "   - 找到Pages选项"
echo "   - 选择分支：gh-pages 或 main/docs"
echo ""
echo "💰 收入渠道设置："
echo "1. 注册Google AdSense：https://www.google.com/adsense"
echo "2. 申请Amazon联盟：https://affiliate-program.amazon.com"
echo "3. 添加捐赠链接：https://buymeacoffee.com"
echo ""
echo "📊 监控设置："
echo "1. 注册Google Analytics"
echo "2. 添加跟踪代码到config.toml"
echo ""
echo "⏰ 自动化设置："
echo "1. 设置cron job每天运行此脚本"
echo "2. 配置GitHub Actions自动部署"
echo ""
echo "💡 提示：所有服务注册都是免费的！"