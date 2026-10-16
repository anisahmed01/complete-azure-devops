from flask import Flask, jsonify, render_template
import os

app = Flask(__name__)

PORTFOLIO = {
    "name": "Anis Ahmed",
    "role": "DevOps Engineer",
    "experience": "5+ years",
    "intro": (
        "I build reliable cloud infrastructure, automate delivery "
        "pipelines, and help teams ship software with confidence."
    ),
    "skills": [
        ("Cloud", "AWS · Azure · GCP"),
        ("Infrastructure", "Terraform · Linux"),
        ("Containers", "Docker · Kubernetes · Helm"),
        ("CI/CD", "Jenkins · Azure Pipelines · GitHub Actions"),
        ("Observability", "Prometheus · Grafana"),
        ("Automation", "Python · Bash · Git"),
    ],
    "projects": [
        {
            "number": "01",
            "name": "Jenkins CI/CD Automation",
            "description": (
                "Automated application builds, testing, quality checks, "
                "container image creation, and deployment workflows."
            ),
            "tags": ["Jenkins", "Docker", "AWS", "CI/CD"],
        },
        {
            "number": "02",
            "name": "Azure Container Deployment",
            "description": (
                "Built a pipeline to test a Flask application, publish "
                "versioned images to ACR, and deploy containers to Azure."
            ),
            "tags": ["Azure Pipelines", "ACR", "Container Apps", "WIF"],
        },
        {
            "number": "03",
            "name": "Infrastructure as Code",
            "description": (
                "Provisioned cloud infrastructure using reusable Terraform "
                "configuration and remote state management."
            ),
            "tags": ["Terraform", "AWS", "IaC", "Automation"],
        },
    ],
}


@app.route("/")
def home():
    return render_template(
        "index.html",
        portfolio=PORTFOLIO,
        app_message=os.getenv("APP_MESSAGE", "Building things that scale."),
        version=os.getenv("APP_VERSION", "1.0.5"),
    )


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)