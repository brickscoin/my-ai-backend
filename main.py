from fastapi import FastAPI

app = FastAPI()

# =========================
# 🧠 PROJECT MEMORY
# =========================

projects = {}

# =========================
# 📋 CREATE PROJECT
# =========================

@app.get("/create_project")
def create_project(name: str, idea: str):
    projects[name] = {
        "idea": idea,
        "tasks": [],
        "status": "created"
    }
    return {"message": f"Project '{name}' created 🚀"}


# =========================
# 📋 ADD TASK
# =========================

@app.get("/add_task")
def add_task(name: str, task: str):
    if name in projects:
        projects[name]["tasks"].append(task)
        return {"message": f"Task added to {name}"}
    return {"error": "Project not found"}


# =========================
# 🤖 AUTO EXECUTE (Dummy)
# =========================

@app.get("/run_project")
def run_project(name: str):
    if name not in projects:
        return {"error": "Project not found"}

    tasks = projects[name]["tasks"]
    results = []

    for t in tasks:
        results.append(f"✅ Done: {t}")

    return {
        "project": name,
        "result": results,
        "status": "completed"
    }


# =========================
# 📊 VIEW PROJECT
# =========================

@app.get("/view_project")
def view_project(name: str):
    if name in projects:
        return projects[name]
    return {"error": "Project not found"}