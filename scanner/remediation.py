
def remediate_dockerfile(dockerfile_path, output_path='./sample_dockerfile/fixed/Dockerfile.fixed'):
    with open(dockerfile_path, 'r') as f:
        content = f.read()

    content = content.replace('ADD ', 'COPY ')
    content = content.replace('USER root', 'USER appuser')

    with open(output_path, 'w') as f:
        f.write(content)

    return output_path
