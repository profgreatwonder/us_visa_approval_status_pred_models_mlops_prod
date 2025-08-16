import os
from pathlib import Path

# project_name = "us_visa_approval_status_mlops_prod"
project_name = "."

list_of_files_and_dirs = [
    f"{project_name}/__init__.py", # makes the directory a local package
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py",
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/testing/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/pipeline/prediction_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",


    # f"{project_name}/utils/model.yaml",
    # f"{project_name}/utils/schema.yaml",


    # f"{project_name}/app.py",
    # f"{project_name}/demo.py",
    # f"{project_name}/setup.py",
    # f"{project_name}/Dockerfile",
    # f"{project_name}/requiremets.txt",
    # f"{project_name}/.dockerignore",
    # f"{project_name}/.gitignore",

    # to add more files and directories, append to this list
    "app.py",
    "demo.py",
    "setup.py",
    "Dockerfile",
    "requirements.txt",
    ".dockerignore",
    ".gitignore",
    "config/model.yaml",
    "config/schema.yaml",

]


for filepath in list_of_files_and_dirs:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    else:
        print(f"file already exist at: {filepath}, skipping creation....")