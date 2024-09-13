from flask import request
from celery import shared_task
from datetime import datetime

@shared_task
def scrape_website(url):
    # https://www.picknpull.com/api/vehicle/search?&makeId=67&modelId=958&year=94-01&distance=25&zip=94560&language=english
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
    }
    response = request.get(url, headers).json()

    return parse_json_data(response)

@shared_task
def parse_json_data(results):
    vals = {}
    for data in results:
        location = data["location"].get("name", "Name Not Found")
        vehicles = data["vehicles"]
        vehicle_info = []
        for vehicle in vehicles:
            vin = vehicle.get("vin", "Unknown VIN")
            link_to_post = (
                f"https://www.picknpull.com/check-inventory/vehicle-details/{vin}"
            )
            year = vehicle.get("year", "Unknown Year")
            model = vehicle.get("model", "Unknown Model")
            make = vehicle.get("make", "Unknown Make")
            row = vehicle.get("row", "Unknown Row")
            image_url = vehicle.get("largeImage", "Image URL Unavailable")
            date_added = vehicle.get("dateAdded", "Date Not Found")
            if date_added:
                date_added = format_date(date_added)
            car = f"{year} {make} {model}"
            vehicle_info.append(
                {
                    "Car": car,
                    "VIN": vin,
                    "Row": row,
                    "Link": link_to_post,
                    "Image URL": image_url,
                    "Date Added": date_added,
                }
            )
        vehicle_info.sort(key=lambda vehicle: vehicle.get("VIN"))
        vals[location] = vehicle_info
    return vals

def format_date(date):
    date_vals = datetime.fromisoformat(date)
    return f"{date_vals.month}-{date_vals.day}-{date_vals.year}"
    

@shared_task
def URL_Builder():
    pass