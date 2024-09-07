import streamlit as st
import openai
from openai import OpenAI
import requests
from io import BytesIO
import base64
import replicate
import json
st.set_page_config(layout="wide")


client = OpenAI()

def translate_to_english(text):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful translator to English."},
            {"role": "user", "content": "Translate it to English: " + text + " Strictly output English translation ONLY"}
        ])
    return response.choices[0].message.content

def detect_n_translate(english_response, original_input, language):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful translator from English to " + language},
            {"role": "user", "content": original_input + " Translate the following English content to " + language + ": English: " + english_response + " output only translated content."}
        ])
    return response.choices[0].message.content

def generate_image(description):
    english = translate_to_english(description)
    prompt = description + " " + english
    URL = get_replicate_url(prompt)
    return URL

def get_perplexity_response(input):
    question = input
    url = "https://api.perplexity.ai/chat/completions"
    print(question)
    payload = {
        "model": "llama-3-sonar-large-32k-online",
        "messages": [
            {
                "role": "system",
                "content": "Answer accurately"
            },
            {
                "role": "user",
                "content": question
            }
        ]
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": "Bearer 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"
    }
    response = requests.post(url, json=payload, headers=headers)
    print(response.text)
    responseD = json.loads(response.text)
    return responseD["choices"][0]["message"]["content"]

def get_replicate_url(description):
    output = replicate.run(
        "stability-ai/sdxl:39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b",
        input={
            "width": 768,
            "height": 768,
            "prompt": description,
            "refine": "expert_ensemble_refiner",
            "scheduler": "K_EULER",
            "lora_scale": 0.6,
            "num_outputs": 1,
            "guidance_scale": 7.5,
            "apply_watermark": False,
            "high_noise_frac": 0.8,
            "negative_prompt": "",
            "prompt_strength": 0.8,
            "num_inference_steps": 25
        }
    )
    print(output)
    return output[0]

st.title("Langflow Hackathon: Multi-language Support")
st.markdown(" by Raghavan Muthuregunathan")
st.markdown("- You can ask questions or generate images in any low-resource language.")
st.markdown("- This project uses Streamlit and OpenAI for language translation and image generation.")
st.markdown("- Note: Due to challenges with custom components for Langflow, Streamlit and OpenAI are used for this implementation.")

mode = st.radio("Choose Mode:", ("Image Mode", "Text Mode"))

language_options = [ "Urdu", "Tamil", "Arabic", "Hindi", "Yoruba", "Swahili", "Hausa", "Amharic", "Igbo"]
selected_language = st.selectbox("Select the language:", language_options)

example1 = "ஒரு பெண் மழையில் நாயுடன் விளையாடுகிறாள்"
example2 = "العربية: ما هي الأنشطة الشعبية للسياح في دبي؟"
example3 = "தமிழ்: தமிழ் நாட்டில் உள்ள புகழ்பெற்ற கோவில்கள் என்ன?"
st.markdown("- " + example1)
st.markdown("- " + example2)
st.markdown("- " + example3)

input_text = st.text_area("Enter the question or describe for image generation (Use any low-resource language):","ஒரு பெண் மழையில் நாயுடன் விளையாடுகிறாள்")

if st.button("Submit"):
    if input_text:
        if mode == "Text Mode":
            translated_text = translate_to_english(input_text)
            english_response = get_perplexity_response(translated_text)
            st.subheader("Response in local language")
            local_response = detect_n_translate(english_response, input_text, selected_language)
            st.write(local_response)
            st.markdown('<font color="red" size="small">LLMs are known to hallucinate</font>', unsafe_allow_html=True)            
            st.write("\n\n-------\n")
            with st.expander("Debug output"):
                st.write("Input in English:" + translated_text.strip())
                st.write(english_response)
                st.write("---------")
                st.write("Detected language: " + selected_language)

        elif mode == "Image Mode":
            image_url = generate_image(input_text)
            if image_url:
                st.subheader("Generated Image:")
                st.image(image_url)
            else:
                st.error("Failed to generate image.")
    else:
        st.error("Please enter some text to translate or describe for image generation.")

st.markdown("***")
st.markdown("This is an implementation of the prompt engineering technique 'Translation Augmented Generation' presented in LF AI Summit.")
