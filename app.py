from flask import Flask, jsonify

app = Flask(__name__)

patients = [
    {
        "id": 101,
        "name": "Rahul Sharma",
        "age": 45,
        "condition": "Diabetes",
        "status": "Stable"
    },
    {
        "id": 102,
        "name": "Priya Singh",
        "age": 32,
        "condition": "Hypertension",
        "status": "Under Observation"
    }
]


@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Secure Healthcare Portal</title>
        <style>
            body {
                font-family: Arial;
                background: #f4f7fb;
                text-align: center;
                padding: 50px;
            }

            .card {
                background: white;
                max-width: 700px;
                margin: auto;
                padding: 30px;
                border-radius: 12px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            }

            h1 {
                color: #1f4e79;
            }

            .security {
                margin-top: 20px;
                padding: 15px;
                background: #e8f5e9;
                border-radius: 8px;
            }
        </style>
    </head>

    <body>
        <div class="card">
            <h1>Secure Healthcare Portal</h1>

            <p>DevSecOps-enabled healthcare application</p>

            <div class="security">
                <strong>Security Status: Protected</strong>
                <p>
                    Automated security scanning is integrated
                    into the CI/CD pipeline.
                </p>
            </div>

            <p>Patient records are simulated using dummy data.</p>

            <p>
                DevSecOps Pipeline:
                GitHub → Jenkins → Security Scan → Docker → Kubernetes
            </p>
        </div>
    </body>
    </html>
    """


@app.route("/api/patients")
def get_patients():
    return jsonify(patients)


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "healthcare-portal"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)