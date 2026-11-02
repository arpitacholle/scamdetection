
import re

SCAM_KEYWORDS = {
    "english": [
        "share your otp",
        "send otp",
        "password",
        "bank details",
        "account blocked",
        "click immediately",
        "urgent",
        "act now",
        "registration fee",
        "job fee",
        "interview fee",
        "pay advance",
        "processing fee",
        "you won a prize",
        "claim your reward",
        "free money",
        "guaranteed job",
        "selected without interview",
        "verify your account",
        "send money"
    ],

    "marathi": [
        "ओटीपी सांगा",
        "ओटीपी पाठवा",
        "बँक तपशील",
        "खाते बंद",
        "तात्काळ पैसे भरा",
        "लगेच पैसे पाठवा",
        "नोकरीसाठी पैसे भरा",
        "नोंदणी शुल्क",
        "तुम्ही बक्षीस जिंकले",
        "मोफत पैसे",
        "आगाऊ पैसे भरा",
        "खाते सत्यापित करा"
    ],

    "hindi": [
        "ओटीपी बताएं",
        "ओटीपी भेजें",
        "बैंक विवरण",
        "खाता बंद",
        "तुरंत पैसे भेजें",
        "अभी पैसे जमा करें",
        "नौकरी के लिए पैसे दें",
        "रजिस्ट्रेशन फीस",
        "आपने इनाम जीता है",
        "मुफ्त पैसे",
        "पहले पैसे जमा करें",
        "अपना खाता सत्यापित करें"
    ]
}


def analyze_text(text, category="general"):

    if not text or not text.strip():
        return {
            "verdict": "Invalid Input",
            "risk_score": 0,
            "risk_level": "None",
            "warning_signs": [],
            "category": category
        }

    message = text.lower()
    warning_signs = []
    score = 0

    patterns = [
        (
            ["otp", "password", "बँक तपशील",
             "ओटीपी", "बैंक विवरण", "पासवर्ड"],
            "Sensitive information request",
            3
        ),
        (
            ["registration fee", "job fee",
             "interview fee", "नोकरीसाठी पैसे",
             "रजिस्ट्रेशन फीस", "नोकरी के लिए पैसे"],
            "Possible recruitment fee scam",
            3
        ),
        (
            ["urgent", "immediately", "act now",
             "तात्काळ", "लगेच", "तुरंत", "अभी"],
            "Urgency or pressure tactics",
            2
        ),
        (
            ["prize", "lottery", "free money",
             "बक्षीस", "इनाम", "मुफ्त पैसे"],
            "Suspicious prize or reward claim",
            2
        ),
        (
            ["send money", "pay advance",
             "processing fee", "पैसे पाठवा",
             "पैसे जमा करें"],
            "Possible request for money",
            3
        ),
        (
            ["guaranteed job", "selected without interview",
             "हमीची नोकरी", "बिना इंटरव्यू नौकरी"],
            "Unrealistic job offer",
            2
        )
    ]

    for keywords, warning, points in patterns:
        if any(word in message for word in keywords):
            if warning not in warning_signs:
                warning_signs.append(warning)
                score += points

    # Check additional multilingual keywords
    all_keywords = (
        SCAM_KEYWORDS["english"]
        + SCAM_KEYWORDS["marathi"]
        + SCAM_KEYWORDS["hindi"]
    )

    matched = [word for word in all_keywords if word in message]

    # Avoid duplicate scoring for phrases already detected
    if matched and not warning_signs:
        warning_signs.append("Suspicious words or phrases detected")
        score += 2

    score = min(score, 10)

    if score >= 6:
        verdict = "Likely Scam"
        risk_level = "High"
    elif score >= 3:
        verdict = "Suspicious"
        risk_level = "Medium"
    else:
        verdict = "Likely Safe"
        risk_level = "Low"

    if not warning_signs:
        warning_signs.append("No common scam indicators detected")

    return {
        "verdict": verdict,
        "risk_score": score,
        "risk_level": risk_level,
        "warning_signs": warning_signs,
        "category": category
    }
