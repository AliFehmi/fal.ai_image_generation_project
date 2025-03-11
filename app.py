import streamlit as st
import fal_client
import time

# Set your Fal.ai API key
API_KEY = "0f2711f9-87e3-4d64-aa8b-a6b31aaffeb0:b0ab8c100de1d5ed26b0a0ff7df1512e"


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
