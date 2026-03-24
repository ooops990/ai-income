#!/bin/bash

# AI自动化收入项目 - 快速启动菜单

echo "🚀 AI自动化收入系统 - 快速启动"
echo "================================"
echo ""

PS3='请选择操作 (输入数字): '
options=(
    "1. 查看收入渠道分析报告"
    "2. 查看设置指南"
    "3. 生成新内容"
    "4. 查看收入报告"
    "5. 部署更新"
    "6. 查看网站状态"
    "7. 退出"
)

select opt in "${options[@]}"
do
    case $REPLY in
        1)
            echo ""
            echo "📊 收入渠道分析报告"
            echo "=================="
            cat INCOME_CHANNELS_ANALYSIS.md | head -50
            echo ""
            echo "完整报告: cat INCOME_CHANNELS_ANALYSIS.md"
            echo ""
            ;;
        2)
            echo ""
            echo "📋 收入渠道设置指南"
            echo "=================="
            echo "立即注册的3个最火平台:"
            echo "1. 🥇 Medium Partner Program - 最高收入"
            echo "   网址: https://medium.com/partner-program"
            echo ""
            echo "2. 🥈 Ezoic广告优化 - 提升收入3-5倍"
            echo "   网址: https://www.ezoic.com/"
            echo ""
            echo "3. 🥉 Amazon Associates联盟 - 稳定佣金"
            echo "   网址: https://affiliate-program.amazon.com/"
            echo ""
            echo "详细步骤: cat INCOME_SETUP_GUIDE.md"
            echo ""
            ;;
        3)
            echo ""
            echo "🤖 生成AI内容"
            echo "============"
            cd ~/.openclaw/workspace/ai-income-project
            python3 scripts/generate_content.py
            echo ""
            echo "✅ 新内容已生成!"
            echo "文章保存在: content/ 目录"
            echo ""
            ;;
        4)
            echo ""
            echo "💰 查看收入报告"
            echo "=============="
            cd ~/.openclaw/workspace/ai-income-project
            python3 scripts/track_income.py
            echo ""
            echo "📁 报告保存在: reports/ 目录"
            echo ""
            ;;
        5)
            echo ""
            echo "⚡ 部署更新"
            echo "=========="
            cd ~/.openclaw/workspace/ai-income-project
            echo "正在推送更新到GitHub..."
            git add .
            git commit -m "自动更新: $(date '+%Y-%m-%d %H:%M:%S')" 2>/dev/null || true
            git push origin main
            echo ""
            echo "✅ 更新已推送!"
            echo "GitHub Actions将自动部署网站"
            echo ""
            ;;
        6)
            echo ""
            echo "🌐 网站状态"
            echo "=========="
            echo "网站URL: https://ooops990.github.io/ai-income/"
            echo ""
            echo "GitHub仓库: https://github.com/ooops990/ai-income"
            echo ""
            echo "GitHub Actions状态:"
            echo "https://github.com/ooops990/ai-income/actions"
            echo ""
            echo "GitHub Pages设置:"
            echo "https://github.com/ooops990/ai-income/settings/pages"
            echo ""
            ;;
        7)
            echo ""
            echo "👋 退出"
            echo "======"
            break
            ;;
        *)
            echo "无效选项"
            ;;
    esac
    
    echo "------------------------"
    echo ""
done

echo ""
echo "💡 提示: 所有自动化脚本都在 scripts/ 目录"
echo "📁 项目结构:"
echo "  content/     - AI生成的文章"
echo "  scripts/     - 自动化脚本"
echo "  reports/     - 收入报告"
echo "  .github/     - GitHub Actions配置"
echo ""
echo "🚀 立即开始赚取收入:"
echo "1. 注册上面3个平台"
echo "2. 获取API凭证"
echo "3. 开始自动化收入!"
echo ""