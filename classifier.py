# -*- coding: utf-8 -*-
"""
垃圾分类识别程序 - 主程序
支持查询、模糊搜索、批量查询等功能
"""

import argparse
from database import (
    GARBAGE_DATABASE,
    GarbageType,
    get_category_emoji,
    get_category_info,
    get_all_categories,
    get_database_size,
)


def search_garbage_detailed(name: str) -> dict:
    """查询垃圾分类（详细版）"""
    # 精确匹配
    if name in GARBAGE_DATABASE:
        category = GARBAGE_DATABASE[name]
        info = get_category_info(category)
        return {
            "found": True,
            "name": name,
            "category": category,
            "emoji": info.get("emoji", ""),
            "color": info.get("color", ""),
            "description": info.get("description", ""),
            "tip": info.get("tip", ""),
        }
    
    # 模糊匹配
    matches = []
    for garbage_name, category in GARBAGE_DATABASE.items():
        if name in garbage_name or garbage_name in name:
            matches.append({
                "name": garbage_name,
                "category": category,
                "emoji": get_category_emoji(category),
            })
    
    if matches:
        return {
            "found": False,
            "query": name,
            "matches": matches[:10],
            "total_matches": len(matches),
        }
    
    return {
        "found": False,
        "query": name,
        "matches": [],
    }


def batch_search(names: list) -> None:
    """批量查询垃圾分类"""
    print("\n" + "=" * 50)
    print("垃圾分类批量查询结果")
    print("=" * 50 + "\n")
    
    stats = {
        GarbageType.RECYCLABLE: [],
        GarbageType.HAZARDOUS: [],
        GarbageType.WET: [],
        GarbageType.DRY: [],
        "unknown": [],
    }
    
    for name in names:
        result = search_garbage_detailed(name)
        if result["found"]:
            stats[result["category"]].append(name)
        else:
            stats["unknown"].append(name)
    
    for category, items in stats.items():
        if items:
            emoji = get_category_emoji(category) if category != "unknown" else "?"
            category_name = category if category != "unknown" else "未知"
            print(f"[{emoji}] {category_name}:")
            for item in items:
                print(f"  - {item}")
            print()
    
    print("-" * 50)
    total = len(names)
    known = total - len(stats["unknown"])
    print(f"统计：共查询 {total} 项，已知 {known} 项，未知 {len(stats['unknown'])} 项")
    print("=" * 50 + "\n")


def list_all_garbage() -> None:
    """列出所有垃圾分类数据"""
    print("\n" + "=" * 50)
    print("垃圾分类完整数据库")
    print("=" * 50 + "\n")
    
    grouped = {
        GarbageType.RECYCLABLE: [],
        GarbageType.HAZARDOUS: [],
        GarbageType.WET: [],
        GarbageType.DRY: [],
    }
    
    for name, category in GARBAGE_DATABASE.items():
        grouped[category].append(name)
    
    for category, items in grouped.items():
        emoji = get_category_emoji(category)
        info = get_category_info(category)
        print(f"[{emoji}] {category} ({info['color']}桶) - {info['description']}")
        print(f"   共 {len(items)} 项")
        print(f"   示例：{', '.join(items[:5])}")
        print(f"   提示：{info['tip']}")
        print()
    
    print("-" * 50)
    print(f"统计：数据库总计 {get_database_size()} 项垃圾")
    print("=" * 50 + "\n")


def interactive_mode() -> None:
    """交互式查询模式"""
    print("\n" + "=" * 50)
    print("欢迎使用垃圾分类查询系统")
    print("=" * 50)
    print("\n提示：")
    print("  - 输入垃圾名称进行查询")
    print("  - 输入 'list' 查看所有分类")
    print("  - 输入 'stats' 查看统计信息")
    print("  - 输入 'quit' 或 'exit' 退出程序")
    print("  - 输入 'help' 查看帮助")
    print("=" * 50 + "\n")
    
    while True:
        try:
            query = input("请输入垃圾名称：").strip()
            
            if not query:
                continue
            
            if query.lower() in ["quit", "exit", "q"]:
                print("\n再见！记得做好垃圾分类哦～\n")
                break
            
            if query.lower() == "help":
                print("\n帮助信息：")
                print("  - 直接输入垃圾名称，如：苹果、电池、塑料瓶")
                print("  - 支持模糊搜索，如：输入 '苹果' 会匹配 '苹果核'")
                print("  - 输入 'list' 查看所有垃圾分类数据")
                print("  - 输入 'stats' 查看数据库统计")
                print("  - 输入 'quit' 退出程序\n")
                continue
            
            if query.lower() == "list":
                list_all_garbage()
                continue
            
            if query.lower() == "stats":
                print(f"\n数据库统计：")
                print(f"   总记录数：{get_database_size()} 项")
                for category in get_all_categories():
                    count = sum(1 for c in GARBAGE_DATABASE.values() if c == category)
                    emoji = get_category_emoji(category)
                    print(f"   [{emoji}] {category}: {count} 项")
                print()
                continue
            
            result = search_garbage_detailed(query)
            
            if result["found"]:
                print(f"\n[OK] 查询结果：")
                print(f"   [{result['emoji']}] {result['name']} -> {result['category']}")
                print(f"   分类说明：{result['description']}")
                print(f"   提示：{result['tip']}\n")
            else:
                print(f"\n[!] 未找到 '{query}' 的准确分类")
                if result["matches"]:
                    print("   相似项参考：")
                    for match in result["matches"]:
                        print(f"   - {match['name']}: [{match['emoji']}] {match['category']}")
                    print()
                else:
                    print("   数据库中没有相关记录\n")
        
        except KeyboardInterrupt:
            print("\n\n程序中断，再见！\n")
            break
        except EOFError:
            print("\n\n再见！\n")
            break


def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description="垃圾分类识别程序",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python classifier.py                    # 交互模式
  python classifier.py -q 苹果             # 查询苹果
  python classifier.py -b 苹果 电池 塑料瓶  # 批量查询
  python classifier.py -l                 # 列出所有数据
        """
    )
    
    parser.add_argument("-q", "--query", type=str, help="查询单个垃圾的分类")
    parser.add_argument("-b", "--batch", type=str, nargs="+", help="批量查询多个垃圾")
    parser.add_argument("-l", "--list", action="store_true", help="列出所有垃圾分类数据")
    parser.add_argument("-s", "--stats", action="store_true", help="显示数据库统计信息")
    
    args = parser.parse_args()
    
    if args.query:
        result = search_garbage_detailed(args.query)
        if result["found"]:
            print(f"\n[{result['emoji']}] {result['name']} -> {result['category']}")
            print(f"分类说明：{result['description']}")
            print(f"提示：{result['tip']}\n")
        else:
            print(f"\n[!] 未找到 '{args.query}'")
            if result["matches"]:
                print("相似项：")
                for match in result["matches"]:
                    print(f"  - {match['name']}: [{match['emoji']}] {match['category']}")
            print()
    
    elif args.batch:
        batch_search(args.batch)
    
    elif args.list:
        list_all_garbage()
    
    elif args.stats:
        print(f"\n统计：")
        print(f"   总记录数：{get_database_size()} 项\n")
        for category in get_all_categories():
            count = sum(1 for c in GARBAGE_DATABASE.values() if c == category)
            emoji = get_category_emoji(category)
            info = get_category_info(category)
            print(f"   [{emoji}] {category} ({info['color']}桶): {count} 项")
        print()
    
    else:
        interactive_mode()


if __name__ == "__main__":
    main()
