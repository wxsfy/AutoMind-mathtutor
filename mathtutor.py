import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Load .env file containing the OpenAI API key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client
client = openai.OpenAI(api_key=api_key)

# Streamlit UI setup
st.set_page_config(page_title="MathBot", page_icon="🧠")
st.title("🧠 MathBot")
st.write("Ask me any math question, and I’ll explain it step-by-step.")

# Input box
question = st.text_input("Type your math question here:")

if question:
	with st.spinner("Thinking..."):
		try:
			response = client.chat.completions.create(
				model="gpt-3.5-turbo",
				messages=[
					{"role": "system", "content": "You are a helpful math tutor. Always explain answers step-by-step in simple terms."},
					{"role": "user", "content": question}
				],
				max_tokens=300
			)

			answer = response.choices[0].message.content.strip()
			st.success("✅ MathBot says:")
			st.write(answer)

		except Exception as e:
			st.error(f"❌ Error: {e}")
