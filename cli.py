
import argparse
from scanner.docker_scan import DockerScanner
from scanner.remediation import remediate_dockerfile
from report import generate_report
from rich.console import Console

console = Console()
scanner = DockerScanner()

def main():
    parser = argparse.ArgumentParser(description="Container Security Automation Tool")
    parser.add_argument('--dockerfile', help='Path to Dockerfile')
    parser.add_argument('--image', help='Docker image name')
    parser.add_argument('--remediate', action='store_true', help='Apply automatic fixes')

    args = parser.parse_args()
    findings = []

    if args.image:
        findings = scanner.scan_image(args.image)
    elif args.dockerfile:
        findings = scanner.scan_dockerfile(args.dockerfile)
        if args.remediate:
            fixed_file = remediate_dockerfile(args.dockerfile)
            console.print(f"[green]Remediated Dockerfile saved to {fixed_file}[/green]")

    generate_report(findings)

if __name__ == "__main__":
    main()
