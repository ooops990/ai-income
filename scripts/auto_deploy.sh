#!/bin/bash

# AI自动化收入项目 - 一键部署脚本
# 用户只需运行此脚本并输入少量信息

set -e

echo "🚀 AI自动化收入项目 - 一键部署"
echo "================================"
echo ""

# 检查Git配置
echo "🔍 检查Git配置..."
if ! git config --global user.name &> /dev/null; then
    echo "⚠️  Git用户信息未配置"
    read -p "请输入你的GitHub用户名: " github_username
    read -p "请输入你的邮箱地址: " user_email
    git config --global user.name "$github_username"
    git config --global user.email "$user_email"
    echo "✅ Git配置完成"
fi

echo ""
echo "📋 部署步骤："
echo "1. 创建GitHub仓库（需要浏览器操作）"
echo "2. 推送代码到GitHub"
echo "3. 启用GitHub Pages"
echo ""

# 显示仓库创建说明
echo "🖥️  第一步：创建GitHub仓库"
echo ""
echo "请访问：https://github.com/new"
echo ""
echo "填写以下信息："
echo "  • Repository name: ai-income"
echo "  • Description: AI自动化收入项目 - 完全自动化运营"
echo "  • 选择: Public（公开）"
echo "  • 不要勾选任何初始化选项"
echo "  • 点击 'Create repository'"
echo ""
echo "创建完成后，复制仓库的HTTPS地址（格式如：https://github.com/你的用户名/ai-income.git）"
echo ""
read -p "请输入GitHub仓库HTTPS地址: " repo_url

if [[ -z "$repo_url" ]]; then
    echo "❌ 未提供仓库地址，退出"
    exit 1
fi

# 第二步：推送代码
echo ""
echo "📤 第二步：推送代码到GitHub"

cd ~/.openclaw/workspace/ai-income-project

# 添加远程仓库
echo "正在添加远程仓库..."
git remote remove origin 2>/dev/null || true
git remote add origin "$repo_url"

# 重命名分支
echo "正在配置分支..."
git branch -M main

# 推送代码
echo "正在推送代码到GitHub..."
if git push -u origin main; then
    echo "✅ 代码推送成功！"
else
    echo "❌ 推送失败，可能需要认证"
    echo ""
    echo "💡 如果提示需要认证："
    echo "1. 访问 https://github.com/settings/tokens"
    echo "2. 创建新的token（选择repo权限）"
    echo "3. 使用token作为密码推送"
    echo ""
    echo "或者使用SSH方式："
    echo "1. 使用SSH地址：git@github.com:你的用户名/ai-income.git"
    echo "2. 确保已配置SSH密钥"
    exit 1
fi

# 第三步：显示后续步骤
echo ""
echo "🎉 代码推送完成！"
echo ""
echo "🔧 第三步：启用GitHub Pages"
echo ""
echo "请在浏览器中完成："
echo "1. 访问你的仓库：$repo_url"
echo "2. 点击 'Settings' → 'Pages'"
echo "3. 配置："
echo "   • Source: Deploy from a branch"
echo "   • Branch: gh-pages"
echo "   • Folder: / (root)"
echo "4. 点击 Save"
echo ""
echo "⏰ 第四步：等待GitHub Actions运行"
echo ""
echo "GitHub Actions将自动："
echo "1. 生成gh-pages分支（第一次需要等待2-3分钟）"
echo "2. 部署网站"
echo "3. 设置每日自动更新"
echo ""
echo "🌐 网站地址："
echo "https://$(echo "$repo_url" | sed -n 's|.*github.com/\([^/]*\)/.*|\1|p').github.io/ai-income/"
echo ""
echo "📊 监控部署状态："
echo "访问仓库 → Actions → 查看部署工作流"
echo ""
echo "✅ 部署完成！项目将在24小时内开始产生内容更新。"
echo ""
echo "💰 下一步：设置收入渠道（可选）"
echo "1. Google AdSense: https://www.google.com/adsense"
echo "2. Amazon联盟: https://affiliate-program.amazon.com"
echo "3. Buy Me a Coffee: https://buymeacoffee.com"
echo ""
echo "📈 项目将在1-2周内开始产生收入！"