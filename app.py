import streamlit as st
import fal_client

st.title("Ali Fehmi Yildiz AI Image Generator using Fal.ai")
st.write("Enter a text prompt and generate AI images!")

prompt = st.text_input("Enter your prompt:", "A futuristic cityscape at sunset")
num_images = st.slider("Number of images:", min_value=1, max_value=4, value=2)

# Function to display logs without nesting inside `st.status()`
def on_queue_update(update):
    if isinstance(update, fal_client.InProgress):
        for log in update.logs:
            st.write(f" {log['message']}")  # Just write logs without nesting

if st.button("Generate Images"):
    with st.status(" Request sent to Fal.ai..."):
        st.write(" Generating images... Please wait.")

        # Submit request to Fal.ai
        result = fal_client.subscribe(
            "fal-ai/flux/dev",
            arguments={
                "prompt": prompt,
                "num_images": num_images
            },
            with_logs=True,
            on_queue_update=on_queue_update,  # Now logs are printed correctly
        )

    if "images" in result:
        st.success(" Image generation complete!")
        for img in result["images"]:
            st.image(img["url"], caption="Generated Image", use_container_width=True)
    else:
        st.error(" Image generation failed. Try again.")
