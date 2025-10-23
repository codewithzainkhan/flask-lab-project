# flask-lab-project

## Team Members & Roles

| Member | Role | Responsibilities |
|--------|------|------------------|
| Member 1 Zain-ul-Abideen (FA22-BCS-020)| Backend Lead | Created Flask backend routes (`/`, `/health`, `/data`) and logic |
| Member 2 Abdul Muqeet (FA22-BCS-168)| Frontend/API Integration | Designed HTML templates, CSS styling, and integrated frontend with Flask APIs |
| Member 3 Sikandar Mukhtar (FA22-BCS-008)| DevOps Engineer | Configured Dockerfile, CI/CD pipeline (`.github/workflows/ci-cd.yml`), and automated deployment |


## How to Build, Test, and Run

### Requirements
- Python 3.10+
- Docker installed
- GitHub Actions enabled

### Build & Run with Docker
cd main
docker build -t flask-lab .
docker run -p 5000:5000 flask-lab
