import os
import streamlit as st
import fal_client
import time

# Submit request
handler = fal_client.submit(
    "fal-ai/flux/dev",
    arguments={
        "prompt": "a cat",
        "seed": 6252023,
        "image_size": "landscape_4_3",
        "num_images": 4
    },
)

request_id = handler.request_id
print(request_id)