
import re

def remediate_dockerfile(dockerfile_path,
        output_path='./sample_dockerfile/fixed/Dockerfile.fixed'):
    with open(dockerfile_path, 'r') as f:
        content = f.read()

    content = re.sub(r'^ADD ', 'COPY ', content, flags=re.MULTILINE)
    content = re.sub(r'^USER\s+root', 'USER appuser', content, flags=re.MULTILINE)

    with open(output_path, 'w') as f:
        f.write(content)

    return output_path
