#!/bin/bash

# GitHub自动化设置脚本
# 使用你的GitHub账号完成项目部署

echo "🚀 GitHub自动化部署设置"
echo "======================="

# 检查git配置
echo "🔍 检查Git配置..."
git config --global user.name
git config --global user.email

echo ""
echo "📋 请完成以下步骤："
echo ""
echo "1. 访问 https://github.com/new 创建新仓库"
echo "   仓库名: ai-income"
echo "   描述: AI自动化收入项目"
echo "   公开仓库"
echo "   不要初始化README、.gitignore或license"
echo ""
echo "2. 复制仓库的SSH地址（格式如：git@github.com:你的用户名/ai-income.git）"
echo ""
echo "3. 运行以下命令完成设置："
echo ""
echo "   cd ~/.openclaw/workspace/ai-income-project"
echo "   git remote add origin git@github.com:你的用户名/ai-income.git"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""
echo "4. 启用GitHub Pages："
echo "   - 进入仓库设置（Settings）"
echo "   - 找到Pages选项"
echo "   - 分支选择: gh-pages"
echo "   - 保存"
echo ""
echo "5. 设置GitHub Actions权限："
echo "   - 进入仓库设置 → Actions → General"
echo "   - 确保'Workflow permissions'设置为'Read and write permissions'"
echo ""
echo "🎯 完成以上步骤后："
echo "   - 网站将自动部署到: https://你的用户名.github.io/ai-income/"
echo "   - GitHub Actions将每天自动更新内容"
echo "   - 你可以开始设置收入渠道"
echo ""
echo "💡 提示：所有步骤可在5分钟内完成，之后项目将完全自动化运行！"