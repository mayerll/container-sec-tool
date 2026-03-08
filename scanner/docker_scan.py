import docker
import re

class DockerScanner:
    def __init__(self):
        self.client = docker.from_env()
    
    def scan_image(self, image_name):
        findings = []

        image = self.client.images.pull(image_name)

        inspect_data = self.client.api.inspect_image(image.id)
        user = inspect_data['Config'].get('User', '')
        if user == '' or user == 'root':
            findings.append({
                'issue': 'Running as root user',
                'severity': 'High',
                'fix': 'Use a non-root user in Dockerfile'
            })

        exposed_ports = inspect_data['Config'].get('ExposedPorts', {})
        for port in exposed_ports:
            port_num = int(port.split('/')[0])
            if port_num < 1024:
                findings.append({
                    'issue': f'Exposing privileged port {port_num}',
                    'severity': 'Medium',
                    'fix': 'Use non-privileged ports >1024'
                })

        return findings

    def scan_dockerfile(self, dockerfile_path):
        findings = []
        with open(dockerfile_path, 'r') as f:
            content = f.read()
            if re.search(r'^ADD ', content, re.MULTILINE):
                findings.append({
                    'issue': 'Using ADD instead of COPY',
                    'severity': 'Low',
                    'fix': 'Replace ADD with COPY for better control'
                })
            if re.search(r'^USER\s+root', content, re.MULTILINE):
                findings.append({
                    'issue': 'Running as root user',
                    'severity': 'High',
                    'fix': 'Specify a non-root USER'
                })
        return findings
