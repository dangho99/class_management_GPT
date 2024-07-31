import yaml
import os

project_path = os.path.abspath(os.path.join(''))

if __name__ == '__main__':
    project_path = os.path.dirname(project_path)
else:
    project_path = os.path.join(os.path.dirname(__file__), '..')


def get_path_project():
    return project_path


def load(path):
    """

    :param path:
    :return:
    """
    with open(path) as f:
        conf = yaml.load(f, Loader=yaml.FullLoader)
    return conf

def load_error_code():
    path = f"""{project_path}/config/{os.environ['envir']}/error_code.yaml"""
    config = load(path=path)
    return config.get("error_code")
    
def load_sql_config():
    path = f"""{project_path}/config/{os.environ['envir']}/sql.yaml"""
    config = load(path=path)
    if "sql" not in config:
        print("sql hasn't configured yet")
        return None
    return config.get("sql")



def get_log_config(path=None):
    """

    :param path:
    :return:
    """
    log_path = f"""config/{os.environ['envir']}/log.yaml"""
    path = os.path.join(project_path, log_path) if path is None else path
    return load(path)


def load_minio_config():
    path = f"""{project_path}/config/{os.environ['envir']}/application.yaml"""
    config = load(path=path)
    if "minio" not in config:
        print("minio hasn't configured yet")
        return None
    return config.get("minio")


def load_project_config():
    project_type = os.environ['project_type']
    path = f"""{project_path}/config/{os.environ['envir']}/{project_type}.yaml"""
    config = load(path=path)
    if project_type not in config:
        print(f"{project_type} hasn't configured yet")
        return None
    return config.get(project_type)



