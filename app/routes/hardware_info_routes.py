from flask import Blueprint
from flask_restful import Api, Resource
import psutil

hardware = Blueprint("hardware", __name__)
api = Api(hardware)

class CPUInformation(Resource):
    def get(self):
        try:
            cpu_usage = psutil.cpu_percent(interval=1)
            cpu_freq = psutil.cpu_freq()
            load_avg = psutil.getloadavg()
            return {"cpu_usage": cpu_usage,
                    "cpu_freq": cpu_freq,
                    "avg_load": load_avg, 
                    "response_code": 200}
        except Exception as e:
            return {"error": f"Exception: {e}", 
                    "response_code": 500}
        
class MemoryInformation(Resource):
    def get(self):
        try:
            memory_info = psutil.virtual_memory()
            total_memory = f"{memory_info.total / (1024 ** 3):.2f} GB"
            available_memory = f"{memory_info.available / (1024 ** 3):.2f} GB"
            used_memory = f"{memory_info.used / (1024 ** 3):.2f} GB"
            memory_usage = f"{memory_info.percent}%"
                        
            return {
                    "available_memory": available_memory,
                    "total_memory":total_memory,
                    "used_memory": used_memory,
                    "usage_percentage": memory_usage,
                    "response_code": 200}
            
        except Exception as e:
            return {"error": f"Exception: {e}",
                    "response_code": 500}
            
class DiskInformation(Resource):
    def get(self):
        try:
            disk_usage = psutil.disk_usage('/')
            total_usage = f"{disk_usage.total / (1024 ** 3):.2f} GB"
            used_space = f"{disk_usage.used / (1024 ** 3):.2f} GB"
            free_space = f"{disk_usage.free / (1024 ** 3):.2f} GB"
            usage_percenage = f"{disk_usage.percent}%"
            
            return {"used_space": used_space,
                    "free_space":free_space,
                    "total_space":total_usage,
                    "usage_percentage":usage_percenage,
                    "response_code": 200}
        except Exception as e:
            return {"error": f"Exception: {e}",
                    "response_code": 500}
            
api.add_resource(CPUInformation, "/cpu-info")
api.add_resource(MemoryInformation, "/mem-info")
api.add_resource(DiskInformation, "/disk-info")