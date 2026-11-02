

import os
import sys

# Find the main ScamDetection project folder
BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

# Add the project folder to Python's import path
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

import streamlit as st

# Import backend AFTER adding the project folder to sys.path
from backend.detector import analyze_text

# Page configuration (only once)
st.set_page_config(
    page_title="ScamDetection",
    page_icon="🛡️",
    layout="centered"
)


# ---------------- TRANSLATIONS ----------------

translations = {
    "English": {
        "safe": "No common scam indicators detected.",
        "tagline": "Think before you trust.",
        "description": "Analyze suspicious SMS messages, emails and job offers.",
        "scan": "Scan a suspicious message",
        "warning": "Never paste real passwords, OTPs or private banking details.",
        "category": "Select message category",
        "general": "General message",
        "sms": "SMS / Text message",
        "email": "Email",
        "job": "Job offer",
        "placeholder": "Paste your suspicious message here...",
        "button": "Analyze Message",
        "result": "Scan Results",
        "risk": "Risk Score",
        "level": "Risk Level",
        "warnings": "Warning Signs",
        "theme": "Choose Theme",
        "language": "Choose Language",
        "empty": "Please enter a message first.",
        "disclaimer": "This tool provides an indicative risk assessment, not a guarantee."
    },

    "Marathi": {
        "tagline": "विश्वास ठेवण्यापूर्वी विचार करा.",
        "description": "संशयास्पद SMS, ईमेल आणि नोकरीच्या संदेशांची तपासणी करा.",
        "scan": "संशयास्पद संदेश तपासा",
        "warning": "खरे पासवर्ड, OTP किंवा बँक तपशील टाकू नका.",
        "category": "संदेशाचा प्रकार निवडा",
        "general": "सामान्य संदेश",
        "sms": "SMS / मजकूर संदेश",
        "email": "ईमेल",
        "job": "नोकरीची ऑफर",
        "placeholder": "तुमचा संशयास्पद संदेश येथे टाका...",
        "button": "संदेश तपासा",
        "result": "तपासणीचा निकाल",
        "risk": "धोक्याचा स्कोअर",
        "level": "धोक्याची पातळी",
        "warnings": "धोक्याची चिन्हे",
        "theme": "थीम निवडा",
        "language": "भाषा निवडा",
        "empty": "कृपया आधी संदेश लिहा.",
        "disclaimer": "हे साधन केवळ संभाव्य धोक्याचे मूल्यांकन देते."
    },

    "Hindi": {
        "tagline": "भरोसा करने से पहले सोचें।",
        "description": "संदिग्ध SMS, ईमेल और नौकरी के संदेशों की जांच करें।",
        "scan": "संदिग्ध संदेश की जांच करें",
        "warning": "असली पासवर्ड, OTP या बैंक की जानकारी न डालें।",
        "category": "संदेश का प्रकार चुनें",
        "general": "सामान्य संदेश",
        "sms": "SMS / टेक्स्ट संदेश",
        "email": "ईमेल",
        "job": "नौकरी का प्रस्ताव",
        "placeholder": "अपना संदिग्ध संदेश यहां डालें...",
        "button": "संदेश की जांच करें",
        "result": "जांच का परिणाम",
        "risk": "जोखिम स्कोर",
        "level": "जोखिम स्तर",
        "warnings": "चेतावनी के संकेत",
        "theme": "थीम चुनें",
        "language": "भाषा चुनें",
        "empty": "कृपया पहले संदेश लिखें।",
        "disclaimer": "यह टूल केवल संभावित जोखिम का आकलन देता है।"
    }
}

# ---------------- RESULT TRANSLATIONS ----------------

result_translations = {
    "Marathi": {
        "Likely Scam": "बहुधा फसवणूक",
        "Suspicious": "संशयास्पद",
        "Likely Safe": "बहुधा सुरक्षित",
        "High": "उच्च",
        "Medium": "मध्यम",
        "Low": "कमी",
        "Sensitive information request": "वैयक्तिक माहिती मागितली जात आहे",
        "Possible recruitment fee scam": "नोकरीसाठी पैसे मागण्याची शक्यता",
        "Urgency or pressure tactics": "तातडीचा दबाव टाकला जात आहे",
        "Suspicious prize or reward claim": "संशयास्पद बक्षीस किंवा इनाम",
        "Possible request for money": "पैसे मागण्याची शक्यता",
        "Unrealistic job offer": "अवास्तव नोकरीची ऑफर",
        "No common scam indicators detected": "फसवणुकीची सामान्य चिन्हे आढळली नाहीत",
        "Suspicious words or phrases detected": "संशयास्पद शब्द आढळले"
    },

    "Hindi": {
        "Likely Scam": "संभावित धोखाधड़ी",
        "Suspicious": "संदिग्ध",
        "Likely Safe": "संभावित सुरक्षित",
        "High": "उच्च",
        "Medium": "मध्यम",
        "Low": "कम",
        "Sensitive information request": "गोपनीय जानकारी मांगी जा रही है",
        "Possible recruitment fee scam": "नौकरी के नाम पर पैसे मांगने की संभावना",
        "Urgency or pressure tactics": "जल्दबाजी का दबाव बनाया जा रहा है",
        "Suspicious prize or reward claim": "संदिग्ध इनाम का दावा",
        "Possible request for money": "पैसे मांगने की संभावना",
        "Unrealistic job offer": "अवास्तविक नौकरी का प्रस्ताव",
        "No common scam indicators detected": "धोखाधड़ी के सामान्य संकेत नहीं मिले",
        "Suspicious words or phrases detected": "संदिग्ध शब्द मिले"
    }
}


def translate_result(value, language):
    return result_translations.get(language, {}).get(value, value)


# ---------------- SESSION STATE ----------------

if "theme" not in st.session_state:
    st.session_state.theme = "Light"

if "language" not in st.session_state:
    st.session_state.language = "English"


# ---------------- SIDEBAR ----------------

st.sidebar.title("⚙️ Settings")

st.sidebar.subheader("🌐 Language")

language = st.sidebar.selectbox(
    "Choose Language",
    ["English", "Marathi", "Hindi"],
    index=["English", "Marathi", "Hindi"].index(
        st.session_state.language
    ),
    label_visibility="collapsed"
)

st.session_state.language = language

st.sidebar.subheader("🎨 Appearance")

theme = st.sidebar.radio(
    "Choose Theme",
    ["Light", "Dark"],
    index=["Light", "Dark"].index(
        st.session_state.theme
    )
)

st.session_state.theme = theme

t = translations[language]


# ---------------- THEME COLORS ----------------

if theme == "Dark":
    background = "#171326"
    card = "#241D38"
    text = "#FFFFFF"
    secondary = "#D6C9E8"
    input_bg = "#302746"
else:
    background = "#F7F3FF"
    card = "#FFFFFF"
    text = "#2E1065"
    secondary = "#6B5B7B"
    input_bg = "#FFFFFF"


# ---------------- CSS ----------------

st.markdown(f"""
<style>
.stApp {{
    background: {background};
    color: {text};
}}

.main .block-container {{
    max-width: 850px;
    padding-top: 2rem;
}}

h1, h2, h3, p, label {{
    color: {text} !important;
}}

.brand {{
    text-align: center;
    font-size: 34px;
    font-weight: 800;
    color: #8B5CF6;
}}

.subtitle {{
    text-align: center;
    font-size: 17px;
    color: {secondary};
}}

.stTextArea textarea {{
    background: {input_bg} !important;
    color: {text} !important;
    border: 1px solid #A78BFA !important;
}}

.stButton button {{
    background: #7C3AED;
    color: white;
    border-radius: 10px;
    border: none;
    width: 100%;
    font-weight: bold;
    min-height: 45px;
}}

.stButton button:hover {{
    background: #5B21B6;
    color: white;
}}

</style>
""", unsafe_allow_html=True)


# ---------------- MAIN HEADER ----------------

st.markdown(
    '<div class="brand">🛡️ TRUSTCHECK AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    f'<div class="subtitle">{t["tagline"]}</div>',
    unsafe_allow_html=True
)

st.write("")
st.write(t["description"])

st.divider()


# ---------------- SCAN SECTION ----------------

st.subheader("🔎 " + t["scan"])

st.warning("⚠️ " + t["warning"])

category_options = {
    t["general"]: "general",
    t["sms"]: "sms",
    t["email"]: "email",
    t["job"]: "job"
}

selected_category = st.selectbox(
    t["category"],
    list(category_options.keys())
)

message = st.text_area(
    t["placeholder"],
    height=180,
    max_chars=10000
)


# ---------------- ANALYZE BUTTON ----------------

if st.button("🔍 " + t["button"]):

    if not message.strip():
        st.warning(t["empty"])

    else:
        try:
            # Directly call the detector.
            # No separate FastAPI server is required.
            data = analyze_text(
                message,
                category_options[selected_category]
            )

            st.divider()
            st.subheader("📊 " + t["result"])

            # Verdict
            verdict = data.get("verdict", "Unknown")
            translated_verdict = translate_result(verdict, language)

            if verdict == "Likely Scam":
                st.error("🚨 " + translated_verdict)

            elif verdict == "Suspicious":
                st.warning("⚠️ " + translated_verdict)

            else:
                st.success("✅ " + translated_verdict)

            # Risk score and risk level
            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    t["risk"],
                    str(data.get("risk_score", 0)) + "/10"
                )

            with col2:
                risk_level = data.get("risk_level", "Unknown")

                st.metric(
                    t["level"],
                    translate_result(risk_level, language)
                )

            # Warning signs
            st.subheader("⚠️ " + t["warnings"])

            warning_signs = data.get("warning_signs", [])

            if warning_signs:
                for warning in warning_signs:
                    st.write(
                        "• " + translate_result(warning, language)
                    )
            else:
                st.write(t["safe"] if "safe" in t else
                         "No warning signs returned.")

            st.caption(t["disclaimer"])

        except Exception as error:
            st.error("Analysis error: " + str(error))


# ---------------- FOOTER ----------------

st.divider()

st.markdown(
    "<center>🛡️ TRUSTCHECK AI · Stay alert. Stay protected.</center>",
    unsafe_allow_html=True
)
