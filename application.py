import streamlit as st
from google import genai
from PIL import Image


API_KEY = "your_api_key"  # < Paste key here
client = genai.Client(api_key=API_KEY)


st.set_page_config(page_title="Vajra-AI: Cyber Defense", page_icon="🛡️", layout="centered")

# Custom CSS for Cyberpunk Look
st.markdown("""
<style>
    /* Google Font Import */
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Rajdhani:wght@500&display=swap');

    /* Main Background */
    .stApp {
        background-color: #050505;
        background-image: radial-gradient(circle at 50% 50%, #1a1a2e 0%, #000000 100%);
    }

    /* Text Colors */
    h1, h2, h3, p, div, span, label {
        color: #e0e0e0 !important;
    }
    
    /* Headers */
    h1 {
        font-family: 'Orbitron', sans-serif;
        color: #00f2ff !important;
        text-shadow: 0 0 10px #00f2ff;
        text-align: center;
        font-size: 3rem !important;
    }

    /* Tabs Styling - Fixed Visibility */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        justify-content: center;
        background-color: transparent;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #111;
        border: 1px solid #333;
        color: #fff;
        border-radius: 5px;
        padding: 10px 20px;
        font-family: 'Orbitron', sans-serif;
    }
    .stTabs [aria-selected="true"] {
        background-color: rgba(0, 242, 255, 0.1);
        border: 1px solid #00f2ff;
        color: #00f2ff !important;
        box-shadow: 0 0 10px rgba(0, 242, 255, 0.3);
    }

    /* Input & Uploader */
    .stTextArea textarea {
        background-color: #0a0a0a !important;
        color: #00f2ff !important;
        border: 1px solid #333 !important;
    }
    .stFileUploader {
        border: 1px dashed #00f2ff;
        border-radius: 10px;
        padding: 20px;
    }

    /* Buttons */
    .stButton>button {
        width: 100%;
        background: linear-gradient(45deg, #0b1c2c, #000);
        color: #00f2ff !important;
        border: 1px solid #00f2ff;
        font-family: 'Orbitron', sans-serif;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background: #00f2ff;
        color: #000 !important;
        box-shadow: 0 0 20px #00f2ff;
    }

    /* Result Box */
    .verdict-box {
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid;
        margin-top: 20px;
        background: rgba(255, 255, 255, 0.05);
    }
</style>
""", unsafe_allow_html=True)


st.markdown("<h1>VAJRA-AI</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>🛡️ The Indestructible Shield Against Cyber Fraud</h3>", unsafe_allow_html=True)


tab1, tab2 = st.tabs(["📝 TEXT DECODER", "👁️ VISION SCANNER"])

with tab1:
    st.markdown("#### 📡 Intercept Suspicious Message")
    user_text = st.text_area("", placeholder="Paste SMS, Email or WhatsApp message here...", height=150)
    
    if st.button("INITIATE SCAN 🔍", key="btn_text"):
        if user_text:
            with st.spinner("⚡ AI NEURAL NETWORK ANALYZING..."):
                try:
                
                    response = client.models.generate_content(
                        model="gemini-flash-latest",
                        contents=f"""
                        You are Vajra-AI. Analyze this text for fraud.
                        Text: {user_text}
                        Output format:
                        Risk Score: (0-100%)
                        Verdict: (SAFE or SCAM)
                        Reason: (Short technical reason)
                        Hindi Explanation: (Simple explanation)
                        """
                    )
                    
                
                    st.markdown(f"""
                    <div class="verdict-box" style="border-color: #00f2ff;">
                        <h3 style="color: #00f2ff !important;">🔍 ANALYSIS REPORT</h3>
                        <p style="color: #fff !important; font-size: 1.1rem; white-space: pre-line;">{response.text}</p>
                    </div>
                    """, unsafe_allow_html=True)

                except Exception as e:
                    st.error(f"System Error: {e}")
        else:
            st.warning("⚠️ INPUT DATA MISSING")


with tab2:
    st.markdown("#### 📸 Upload Evidence (Screenshot/QR)")
    

    uploaded_file = st.file_uploader("Drop image here...", type=["jpg", "png", "jpeg"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Evidence Loaded", use_column_width=True)
        
        if st.button("SCAN VISUALS 📸", key="btn_img"):
            with st.spinner("⚡ VISION API PROCESSING..."):
                try:
                    response = client.models.generate_content(
                        model="gemini-flash-latest",
                        contents=["Analyze this image for financial fraud (Fake QR, Phishing URL). Give Verdict and Hindi Explanation.", image]
                    )
                    
                    st.markdown(f"""
                    <div class="verdict-box" style="border-color: #00ff88;">
                        <h3 style="color: #00ff88 !important;">👁️ VISUAL REPORT</h3>
                        <p style="color: #fff !important; white-space: pre-line;">{response.text}</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                except Exception as e:
                    st.error(f"Error: {e}")