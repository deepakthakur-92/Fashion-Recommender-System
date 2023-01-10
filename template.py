import os


dirs = [
    os.path.join("artifacts", "extracted_features"),
    os.path.join("artifacts","pickle_format_data"),
    os.path.join("artifacts","uploads"),
    "config",
    "demo",
    "samples",
    "src",
    os.path.join("src","utils")



]

for dir_ in dirs:
    os.makedirs(dir_, exist_ok=True)
    with open(os.path.join(dir_, "gitkeep"),"w") as f:
        pass



files=[
    os.path.join("config","config.yaml"),
    os.path.join("src","__init__.py"),
    os.path.join("src/utils","__init__,py"),
    ".gitignore",
    "params.yaml"
    

]

for file_ in files:
    with open(file_, "w") as f:
        pass