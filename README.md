# Customer-Lifetime-Value-Prediction


## Git Commands

```bash
git add .

git commit -m "Updated"

git push origin main
```

## How to run?

```bash
conda create -n clv python=3.12 -y

-n: creating a new environment. I will create inside the C:Drive
-p: creating inside this directory
```

```bash
conda activate clv
```

```bash
pip install -r requirements.txt
```

## Workflow

1. constant
2. config_entity
3. artifact_entity
4. component
5. pipeline
6. app.py / demo.py

### Export the environment variable
```bash
export MONGODB_URL="mongodb+srv://<username>:<password>...."

```