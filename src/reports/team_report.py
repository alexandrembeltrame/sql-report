# src/reports/team_report.py
from src.database.queries import get_team
from pathlib import Path
import json

OUTPUT_DIR = Path("src/reports/output")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def generate_team_report(team: str, save_json: bool = True):
    rows = get_team(team)
    # Impressão simples (CLI)
    print(f"\n📊 Relatório do time: {team}")
    print("-" * 40)
    for name, salary, perf in rows:
        print(f"{name:<10} | Salário: {salary:>8.2f} | Performance: {perf}")

    # Salva arquivo JSON
    if save_json:
        out = [ {"name": r[0], "salary": r[1], "performance": r[2]} for r in rows ]
        path = OUTPUT_DIR / f"team_{team.lower()}.json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(out, f, ensure_ascii=False, indent=2)
        print("📁 Salvo em:", path)
    return rows
