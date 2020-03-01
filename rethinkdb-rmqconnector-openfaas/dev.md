## Dev Notes

### Adding new functions

```bash
faas-cli new --lang python3-skeleton new-function-name --append stack.yml
```

Add following into all functions to ensure they get configuration data

```yaml
environment_file:
  - config.yml
build_options:
  - dev
annotations:
  topic: xxxxx
```

### Building base, changefeeder, and functions

```bash
docker-compose build --no-cache && faas-cli build -f stack.yml && faas-cli deploy -f stack.yml
```


```bash
faas-cli build -f stack.yml
```

```bash
faas-cli deploy -f stack.yml
```

```bash
echo -n <your-faas-generated-password> | faas-cli login --username=admin --password-stdin
```