import streamlit as st
import fal_client
import os

# Set API Key (Ensure this is set in your environment)
if "FAL_KEY" not in os.environ:
    st.error("❌ API Key missing! Set FAL_KEY as an environment variable.")
    st.stop()

# Authenticate with Fal.ai
fal_client.auth(os.getenv("FAL_KEY"))

# Streamlit UI
st.title("🖼️ AI Image Generator using Fal.ai")
st.write("Enter a text prompt and generate AI images!")

# User input for prompt
prompt = st.text_input("Enter your prompt:", "A futuristic cityscape at sunset")

# Number of images
num_images = st.slider("Number of images:", min_value=1, max_value=4, value=2)

# Function to display logs
def on_queue_update(update):
    if isinstance(update, fal_client.InProgress):
        for log in update.logs:
            st.write(f"⏳ {log['message']}")

# Button to generate images
if st.button("Generate Images"):
    st.write("🚀 Generating images... Please wait.")

    # Submit request to Fal.ai
    result = fal_client.subscribe(
        "fal-ai/flux/dev",
        arguments={
            "prompt": prompt,
            "num_images": num_images
        },
        with_logs=True,
        on_queue_update=on_queue_update,
    )

    # Display the generated images if available
    if "images" in result:
        st.write("🎉 Image generation complete!")
        for img in result["images"]:
            st.image(img["url"], caption="Generated Image", use_column_width=True)
    else:
        st.error("❌ Image generation failed. Try again.")
