import streamlit as st
import numpy as np
import cv2
from PIL import Image
import joblib

from recognize import detect_faces, predict_faces  

rf_model = joblib.load("random_forest_model.pkl")

columns = ['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10', 'Age','Sex','Jaundice','Family_ASD']

# Questions
questions_en = [
    "Does your child get very distressed or cover ears due to everyday noises that most children tolerate? "
    "(e.g., crying, screaming, or running away when hearing a vacuum cleaner, mixer, or loud music — not just mild dislike)",

    "Does your child spontaneously engage in pretend play on their own? "
    "(e.g., pretending to feed a doll, talking to toys, or acting like a doctor — not just copying when shown once)",

    "Does your child seek climbing activities repeatedly beyond normal play? "
    "(e.g., constantly climbing furniture or unsafe heights even after being stopped, not just enjoying playground equipment)",

    "Does your child actively initiate and enjoy social interaction games like peek-a-boo? "
    "(e.g., brings hands to face to start the game, laughs and repeats it — not confusing it with hide-and-seek)",

    "Does your child frequently seek physical closeness beyond normal affection? "
    "(e.g., repeatedly coming for hugs throughout the day for comfort or regulation, not just enjoying cuddling with parents)",

    "Does your child consistently respond when their name is called without visual cues? "
    "(e.g., turns head or acknowledges — not responding only when touched or after multiple calls)",

    "Does your child frequently stare into space without engaging with surroundings? "
    "(e.g., fixed gaze for several seconds/minutes, hard to redirect — not daydreaming briefly)",

    "Does your child attempt to interact with other children*? "
    "(e.g., watching, approaching, sharing toys, copying actions — not just playing alongside without interaction)",

    "Does your child use pointing to share interest, not just to request? "
    "(e.g., pointing at a plane to show it to you, checking your reaction — not only pointing to ask for objects)",

    "Does your child repeatedly make unusual finger or hand movements near their face? "
    "(e.g., hand flapping, finger flicking close to eyes, occurring often and without purpose)"
]

questions_hi = [
    "क्या आपका बच्चा रोज़मर्रा की आवाज़ों से बहुत ज़्यादा परेशान हो जाता है? "
    "(जैसे कान ढक लेना, रोना, भाग जाना — न कि सिर्फ़ आवाज़ पसंद न होना)",

    "क्या बच्चा खुद से कल्पनात्मक खेल करता है? "
    "(जैसे गुड़िया को खाना खिलाना, खिलौनों से बात करना — न कि सिर्फ़ सिखाने पर नकल करना)",

    "क्या बच्चा बार-बार और ज़रूरत से ज़्यादा चढ़ने की कोशिश करता है? "
    "(जैसे फर्नीचर या ऊँचाई पर चढ़ना, मना करने के बाद भी)",

    "क्या बच्चा खुद से आंख-मिचौली (peek-a-boo) जैसे सामाजिक खेल शुरू करता है? "
    "(हाथ से आंख ढककर खेल शुरू करना — न कि छुपन-छुपाई समझना)",

    "क्या बच्चा बार-बार दुलार या शारीरिक संपर्क माँगता है? "
    "(दिन में कई बार गले लगने आना — न कि सामान्य माता-पिता का प्यार पसंद करना)",

    "क्या बच्चा नाम पुकारने पर तुरंत प्रतिक्रिया देता है? "
    "(सिर घुमाना या देखना — न कि कई बार बुलाने पर या छूने पर)",

    "क्या बच्चा अक्सर बिना कारण किसी जगह को घूरता रहता है? "
    "(कुछ सेकंड या मिनट तक, ध्यान हटाना मुश्किल)",

    "क्या बच्चा अन्य बच्चों से जुड़ने की कोशिश करता है? "
    "(खिलौने साझा करना, देखना, पास जाना — न कि अकेले खेलते रहना)",

    "क्या बच्चा दिलचस्प चीज़ें दिखाने के लिए इशारा करता है? "
    "(जैसे हवाई जहाज़ दिखाकर आपकी प्रतिक्रिया देखना — न कि सिर्फ़ चीज़ माँगना)",

    "क्या बच्चा बार-बार"
    " चेहरे के पास उंगलियों या हाथों की अजीब हरकतें करता है? "
    "(जैसे हाथ हिलाना, उंगलियाँ फड़फड़ाना)"
]

# -------------------------------------------------------------------
# ASD Awareness Content
# -------------------------------------------------------------------
def get_asd_content(language):
    if language == "Hindi":
        return """
### 🧠 ऑटिज़्म स्पेक्ट्रम डिसऑर्डर (ASD) क्या है?

**ASD एक "मस्तिष्क और तंत्रिका तंत्र का विकास", जिसमें बच्चे का सामाजिक व्यवहार, संवाद और सीखने का तरीका अलग हो सकता है।

#### 🔍 सामान्य लक्षण
- आँखों से संपर्क कम
- नाम बुलाने पर प्रतिक्रिया न देना
- बार-बार एक-सी हरकतें
- सामाजिक खेलों में रुचि कम

#### 🧬 संभावित कारण
- आनुवंशिक कारण
- गर्भावस्था के दौरान जटिलताएँ
- मस्तिष्क विकास में अंतर

#### ✅ समाधान / सहायता
- जल्दी पहचान बहुत ज़रूरी है
- स्पीच थेरेपी
- बिहेवियर थेरेपी
- माता-पिता का सहयोग

📌 **ध्यान दें:** हर बच्चा अलग होता है। यह टूल केवल *जाँच परीक्षण* के लिए है।

➡️ **ऊपर दिए गए टैब से इमेज या प्रश्नावली द्वारा टेस्ट करें**
"""
    else:
        return """
### 🧠 What is Autism Spectrum Disorder (ASD)?

**ASD is a neurodevelopmental condition** that affects how a child communicates, interacts, and behaves.

#### 🔍 Common Symptoms
- Limited eye contact
- Not responding to name
- Repetitive movements
- Difficulty in social interaction

#### 🧬 Possible Causes
- Genetic factors
- Pregnancy-related complications
- Differences in brain development

#### ✅ Support & Solutions
- Early detection is very important
- Speech therapy
- Behavioral therapy
- Strong parental support

📌 **Note:** Every child is unique. This tool is only for *screening* purposes.

➡️ **Take a test using Image Upload or Questionnaire tabs above**
"""

# -------------------------------------------------------------------
# Autism Centers (Sample Data)
# -------------------------------------------------------------------
autism_centers = {
    "Mumbai": [
        ("Ummeed Child Development Center", "https://ummeed.org"),
        ("Sethu Center", "https://sethu.in")
    ],
    "Delhi": [
        ("Action for Autism", "https://actionforautism.org"),
        ("VIMHANS", "https://vimhans.com")
    ],
    "Pune": [
        ("Sparsh Autism Center", "https://sparshpune.org")
    ]
}

# -------------------------------------------------------------------
# Page Config
# -------------------------------------------------------------------
st.set_page_config(page_title="Autism Screening System", page_icon="🧠", layout="wide")

st.title("🧠 Autism Screening System")
st.write("A simple and accessible tool for early screening support")

# Language Selector
language = st.sidebar.selectbox("🌐 Select Language / भाषा चुनें", ["English", "Hindi"])

# -------------------------------------------------------------------
# Tabs
# -------------------------------------------------------------------
tab1, tab2, tab3, tab4 = st.tabs([
    "ℹ About ASD",
    "📸 Image Screening",
    "📋 Questionnaire",
    "📍 Autism Centers"
])
def get_text(label, language):
    text = {
        "image_title": {
            "English": "Upload Face Image for Screening",
            "Hindi": "स्क्रीनिंग के लिए बच्चे की फोटो अपलोड करें"
        },
        "questionnaire_title": {
            "English": "Answer these questions",
            "Hindi": "इन प्रश्नों के उत्तर दें"
        },
        "upload_warning": {
            "English": "No face detected. Please upload a clear image.",
            "Hindi": "चेहरा नहीं मिला। कृपया साफ़ फोटो अपलोड करें।"
        },
        "predict_button": {
            "English": "Predict",
            "Hindi": "पूर्वानुमान करें"
        }
    }
    return text[label][language]
# -------------------------------------------------------------------
# TAB 1 – ASD Awareness
# -------------------------------------------------------------------
with tab1:
    st.markdown(get_asd_content(language))

# -------------------------------------------------------------------
# TAB 2 – Image Screening
# -------------------------------------------------------------------
with tab2:
    st.subheader(get_text("image_title", language))

    uploaded_file = st.file_uploader(
        "Upload a Face Image / फोटो अपलोड करें",
        type=["jpg", "png", "jpeg"]
    )

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        image_np = np.array(image)

        st.image(image, caption="Uploaded Image", width=350)

        faces, gray = detect_faces(image_np)

        if len(faces) == 0:
            st.warning(get_text("upload_warning", language))
        else:
            result_image = predict_faces(image_np, faces, gray)
            st.image(result_image, caption="Recognized Face(s)")

            st.info(
                "⚠ **Note:** Image-based results may sometimes be inaccurate. "
                "For better accuracy, please complete the **Questionnaire Test (Tab 3)**.  "
                

                "⚠ **ध्यान दें:** छवि-आधारित परिणाम कभी-कभी गलत हो सकते हैं। "
                "बेहतर सटीकता के लिए, कृपया **प्रश्नावली परीक्षण (टैब 3)** पूरा करें।"
            )

# -------------------------------------------------------------------
# TAB 3 – Questionnaire
# -------------------------------------------------------------------
with tab3:
    st.subheader("Answer the Questions")

    questions = questions_hi if language == "Hindi" else questions_en
    answers = []

    for q in questions:
        ans = st.selectbox(q, ["No", "Yes"])
        answers.append(1 if ans == "Yes" else 0)

    age_months = st.number_input("Child's Age (in MONTHS)", min_value=6, max_value=180, value=36)
    sex = st.selectbox("Sex", ["Male", "Female"])
    jaundice = st.selectbox("History of Jaundice?", ["No", "Yes"])
    family_asd = st.selectbox("Family history of ASD?", ["No", "Yes"])

    answers.extend([
        age_months,
        1 if sex == "Male" else 0,
        1 if jaundice == "Yes" else 0,
        1 if family_asd == "Yes" else 0
    ])

    if st.button("Predict"):
        arr = np.array(answers).reshape(1, -1)
        pred = rf_model.predict(arr)[0]

        if pred == 1:
            st.error("⚠ ASD Traits Detected")
        else:
            st.success("✔ No ASD Traits Detected")

# -------------------------------------------------------------------
# TAB 4 – Autism Centers
# -------------------------------------------------------------------
with tab4:
    st.subheader("Find Nearby Autism Centers/आस-पास के ऑटिज़्म केंद्र खोजें")

    city = st.selectbox("Select City", list(autism_centers.keys()))

    for center, link in autism_centers[city]:
        st.markdown(f"**{center}**  \n🌐 {link}")