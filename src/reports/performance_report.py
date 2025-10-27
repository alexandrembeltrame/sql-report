# src/reports/performance_report.py
from src.database.queries import get_top_performers
from pathlib import Path
import json

OUTPUT_DIR = Path("src/reports/output")

def generate_performance_report(limit: int = 3, save_json: bool = True):
    rows = get_top_performers(limit)
    print("\n🏆 Top Performers da Empresa")
    print("-" * 40)
    for name, dep, perf in rows:
        print(f"{name:<10} | {dep:<12} | {perf}")

    if save_json:
        out = [{"name": r[0], "department": r[1], "performance": r[2]} for r in rows]
        path = OUTPUT_DIR / f"top_performers_{limit}.json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(out, f, ensure_ascii=False, indent=2)
        print("📁 Salvo em:", path)
    return rows
