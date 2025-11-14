thonimport json
from .utils import save_json

class DataExporter:
    def __init__(self):
        pass

    def export_to_json(self, data, file_name):
        save_json(data, f'data/{file_name}')