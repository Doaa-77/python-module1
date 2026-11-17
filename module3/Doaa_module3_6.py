from fastapi import FastAPI
import math

app = FastAPI()

# Sample list of 20 items
items_list = list(range(1, 21))

@app.get("/items")
def get_items(page: int = 1, size: int = 5):

    # Calculate which items to return
    start = (page - 1) * size
    end = start + size

    selected_items = items_list[start:end]

    # Calculate total number of pages
    total_items = len(items_list)
    total_pages = math.ceil(total_items / size)

    return {
        "items": selected_items,
        "page": page,
        "size": size,
        "total_items": total_items,
        "total_pages": total_pages
    }
