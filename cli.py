
import argparse
from scanner.docker_scan import DockerScanner
from scanner.remediation import remediate_dockerfile
from report import generate_report
from rich.console import Console
import json

console = Console()
scanner = DockerScanner()

def main():
    parser = argparse.ArgumentParser(description="Container Security Automation Tool")
    parser.add_argument('--dockerfile', help='Path to Dockerfile')
    parser.add_argument('--image', help='Docker image name')
    parser.add_argument('--remediate', action='store_true', help='Apply automatic fixes')
    parser.add_argument('--dry-run', action='store_true', help='Show remediation actions without applying them')
    parser.add_argument('--json-report', help='Save findings as JSON file')

    args = parser.parse_args()
    findings = []

    if args.image:
        findings = scanner.scan_image(args.image)
    elif args.dockerfile:
        findings = scanner.scan_dockerfile(args.dockerfile)
        if args.remediate:
            if args.dry_run:
                console.print("[yellow]Dry-run mode: The following fixes would be applied:[/yellow]")
                for f in findings:
                    console.print(f"- {f['fix']}")
            else:
                fixed_file = remediate_dockerfile(args.dockerfile)
                console.print(f"[green]Remediated Dockerfile saved to {fixed_file}[/green]")

    generate_report(findings)

    if args.json_report:
        with open(args.json_report, 'w') as f:
            json.dump(findings, f, indent=2)
        console.print(f"[green]JSON report saved to {args.json_report}[/green]")

if __name__ == "__main__":
    main()
