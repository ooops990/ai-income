#!/usr/bin/env python3
"""
收入追踪脚本
模拟收入数据并生成报告
"""

import json
import datetime
import random
from pathlib import Path

def generate_income_data():
    """生成模拟收入数据"""
    
    # 收入来源
    sources = {
        "google_adsense": {
            "name": "Google AdSense",
            "base_rate": 0.5,  # 每千次展示收入（美元）
            "growth_rate": 0.05  # 日增长率
        },
        "amazon_associates": {
            "name": "Amazon联盟",
            "base_rate": 2.0,  # 平均每单佣金
            "conversion_rate": 0.01  # 转化率
        },
        "donations": {
            "name": "捐赠",
            "base_rate": 5.0,  # 平均捐赠金额
            "frequency": 0.1  # 捐赠频率
        }
    }
    
    # 模拟30天数据
    data = []
    total_income = 0
    
    for day in range(30):
        date = (datetime.datetime.now() - datetime.timedelta(days=29-day)).strftime('%Y-%m-%d')
        
        daily_data = {
            "date": date,
            "traffic": random.randint(100, 1000),  # 日访问量
            "income": {}
        }
        
        daily_total = 0
        
        for source_id, source_info in sources.items():
            # 计算该来源收入
            if source_id == "google_adsense":
                impressions = daily_data["traffic"] * 3  # 假设每访问3次展示
                income = impressions / 1000 * source_info["base_rate"] * (1 + source_info["growth_rate"] * day)
            elif source_id == "amazon_associates":
                clicks = daily_data["traffic"] * 0.1  # 10%点击率
                orders = clicks * source_info["conversion_rate"]
                income = orders * source_info["base_rate"]
            else:  # donations
                income = random.random() * source_info["frequency"] * source_info["base_rate"]
            
            income = round(income, 2)
            daily_data["income"][source_id] = {
                "name": source_info["name"],
                "amount": income
            }
            daily_total += income
        
        daily_data["total"] = round(daily_total, 2)
        total_income += daily_total
        data.append(daily_data)
    
    return {
        "generated_at": datetime.datetime.now().isoformat(),
        "period_days": 30,
        "total_income": round(total_income, 2),
        "average_daily": round(total_income / 30, 2),
        "data": data
    }

def generate_report(income_data):
    """生成收入报告"""
    
    report = f"""# AI自动化收入报告

## 概览
- **报告时间**: {datetime.datetime.now().strftime('%Y年%m月%d日 %H:%M:%S')}
- **统计周期**: 最近30天
- **总收入**: ${income_data['total_income']}
- **日均收入**: ${income_data['average_daily']}

## 收入来源分析

"""
    
    # 按来源汇总
    source_totals = {}
    for day_data in income_data["data"]:
        for source_id, source_income in day_data["income"].items():
            if source_id not in source_totals:
                source_totals[source_id] = {
                    "name": source_income["name"],
                    "total": 0
                }
            source_totals[source_id]["total"] += source_income["amount"]
    
    for source_id, source_info in source_totals.items():
        percentage = (source_info["total"] / income_data["total_income"]) * 100
        report += f"### {source_info['name']}\n"
        report += f"- 总收入: ${source_info['total']:.2f}\n"
        report += f"- 占比: {percentage:.1f}%\n\n"
    
    # 趋势分析
    report += "## 趋势分析\n\n"
    
    # 最近7天数据
    recent_7days = income_data["data"][-7:]
    recent_total = sum(day["total"] for day in recent_7days)
    previous_7days = income_data["data"][-14:-7]
    previous_total = sum(day["total"] for day in previous_7days)
    
    if previous_total > 0:
        growth = ((recent_total - previous_total) / previous_total) * 100
        report += f"- **最近7天收入**: ${recent_total:.2f}\n"
        report += f"- **环比增长**: {growth:.1f}%\n"
    else:
        report += f"- **最近7天收入**: ${recent_total:.2f}\n"
        report += "- **环比增长**: 首次统计\n"
    
    # 建议
    report += "\n## 优化建议\n\n"
    
    # 根据数据给出建议
    best_source = max(source_totals.items(), key=lambda x: x[1]["total"])
    worst_source = min(source_totals.items(), key=lambda x: x[1]["total"])
    
    report += f"1. **重点发展**: {best_source[1]['name']}是目前最主要的收入来源，可以考虑进一步优化。\n"
    report += f"2. **需要改进**: {worst_source[1]['name']}的收入较低，需要分析原因并改进策略。\n"
    report += "3. **内容优化**: 分析高收入文章的特点，生成更多类似内容。\n"
    report += "4. **流量提升**: 通过SEO优化和社交媒体推广增加网站流量。\n"
    
    report += "\n---\n"
    report += "*本报告由AI自动生成，数据为模拟数据。实际收入可能有所不同。*\n"
    
    return report

def main():
    """主函数"""
    print("📊 生成收入报告...")
    
    # 创建报告目录
    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)
    
    # 生成收入数据
    income_data = generate_income_data()
    
    # 保存原始数据
    data_file = reports_dir / "income_data.json"
    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(income_data, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 收入数据已保存: {data_file}")
    
    # 生成报告
    report = generate_report(income_data)
    
    # 保存报告
    report_file = reports_dir / f"income_report_{datetime.datetime.now().strftime('%Y%m%d')}.md"
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"✅ 收入报告已生成: {report_file}")
    
    # 输出摘要
    print(f"\n📈 收入摘要:")
    print(f"   总收入: ${income_data['total_income']}")
    print(f"   日均收入: ${income_data['average_daily']}")
    
    # 显示主要收入来源
    print(f"\n💰 主要收入来源:")
    source_totals = {}
    for day_data in income_data["data"]:
        for source_id, source_income in day_data["income"].items():
            if source_id not in source_totals:
                source_totals[source_id] = {
                    "name": source_income["name"],
                    "total": 0
                }
            source_totals[source_id]["total"] += source_income["amount"]
    
    for source_id, source_info in source_totals.items():
        percentage = (source_info["total"] / income_data["total_income"]) * 100
        print(f"   {source_info['name']}: ${source_info['total']:.2f} ({percentage:.1f}%)")

if __name__ == "__main__":
    main()