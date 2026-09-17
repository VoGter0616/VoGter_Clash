import os
from datetime import datetime, timezone, timedelta
import requests

# Proxy 规则源列表
proxy_urls = [
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Proxy/Proxy.list",
    "https://raw.githubusercontent.com/VoGter0616/VoGter_Clash/refs/heads/main/rule/Clash/Proxy.list",
]


def get_beijing_time():
    """获取当前的北京时间字符串 (UTC+8)"""
    utc_now = datetime.now(timezone.utc)
    beijing_now = utc_now.astimezone(timezone(timedelta(hours=8)))
    return beijing_now.strftime("%Y-%m-%d %H:%M:%S")


def merge_proxy_rules():
    output_dir = "rule/Merged"
    output_path = os.path.join(output_dir, "Proxy_Merged.list")

    # 1. 读取旧文件用于比对新增数量
    old_rules = set()
    if os.path.exists(output_path):
        try:
            with open(output_path, "r", encoding="utf-8") as f:
                for line in f.readlines():
                    line = line.strip()
                    if line and not line.startswith(("#", ";")):
                        old_rules.add(line)
        except Exception as e:
            print(f"读取旧文件失败或旧文件不存在: {e}")

    # 2. 抓取最新规则
    new_rules = set()
    for url in proxy_urls:
        try:
            response = requests.get(url, timeout=15)
            if response.status_code == 200:
                for line in response.text.splitlines():
                    line = line.strip()
                    if line and not line.startswith(("#", ";")):
                        new_rules.add(line)
        except Exception as e:
            print(f"Error fetching {url}: {e}")

    # 3. 计算新增规则的数量
    added_count = len(new_rules - old_rules)

    # 4. 统计各类规则数量
    stats = {
        "DOMAIN": 0,
        "DOMAIN-KEYWORD": 0,
        "DOMAIN-SUFFIX": 0,
        "IP-CIDR": 0,
        "IP-CIDR6": 0,
        "OTHER": 0,
    }

    for rule in new_rules:
        parts = rule.split(",")
        if parts:
            rule_type = parts[0].strip().upper()
            if rule_type in stats:
                stats[rule_type] += 1
            else:
                stats["OTHER"] += 1

    total_count = len(new_rules)
    updated_at = get_beijing_time()

    # 5. 确保目录存在
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 6. 写入文件（头部全为纯数字计数）
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("# Custom_Proxy_List\n")
        f.write(f"# UPDATED: {updated_at} (UTC+8)\n")
        f.write(f"# DOMAIN: {stats['DOMAIN']}\n")
        f.write(f"# DOMAIN-KEYWORD: {stats['DOMAIN-KEYWORD']}\n")
        f.write(f"# DOMAIN-SUFFIX: {stats['DOMAIN-SUFFIX']}\n")
        f.write(f"# IP-CIDR: {stats['IP-CIDR']}\n")
        f.write(f"# IP-CIDR6: {stats['IP-CIDR6']}\n")
        if stats["OTHER"] > 0:
            f.write(f"# OTHER: {stats['OTHER']}\n")
        f.write(f"# NEWLY ADDED: {added_count}\n")
        f.write(f"# TOTAL: {total_count}\n\n")

        # 写入排序后的具体规则列表
        f.write("\n".join(sorted(new_rules)))

    # 控制台日志
    print(
        f"Proxy规则合并完成！\n"
        f"更新时间: {updated_at}\n"
        f"当前总计: {total_count} 条 | 相比上次新增: {added_count} 条"
    )


if __name__ == "__main__":
    merge_proxy_rules()
