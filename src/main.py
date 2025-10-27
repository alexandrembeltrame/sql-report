# src/main.py
from src.reports.team_report import generate_team_report
from src.reports.performance_report import generate_performance_report

if __name__ == "__main__":
    print("\n=== Sistema de Relatórios Corporativos ===")
    generate_team_report("TI")
    generate_team_report("Financeiro")
    generate_performance_report()
