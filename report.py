
from rich.console import Console
from rich.table import Table

def generate_report(findings):
    console = Console()
    if not findings:
        console.print("[green]No security issues found![/green]")
        return

    table = Table(title="Security Scan Report")
    table.add_column("Issue", style="red")
    table.add_column("Severity", style="yellow")
    table.add_column("Fix", style="green")

    for f in findings:
        table.add_row(f['issue'], f['severity'], f['fix'])

    console.print(table)
