// Text Content Resources
const RESOURCES = {
    "English": {
        "nav_about": "About ASD",
        "nav_image": "Image Screening",
        "nav_quiz": "Questionnaire",
        "nav_centers": "Centers",
        "about_title": "What is Autism Spectrum Disorder (ASD)?",
        "image_title": "Upload Face Image for Screening",
        "upload_prompt": "Drag & Drop or Click to Upload",
        "btn_predict": "Predict",
        "image_note": "⚠ Note: Image-based results are experimental. Please use the Questionnaire for better accuracy.",
        "quiz_title": "Screening Questionnaire",
        "lbl_age": "Child's Age (Months)",
        "lbl_sex": "Sex",
        "lbl_jaundice": "History of Jaundice?",
        "lbl_family": "Family History of ASD?",
        "btn_submit": "Submit Questionnaire",
        "btn_print": "🖨 Print / Save Result",
        "centers_title": "Find Nearby Autism Centers",
        "lbl_city": "Select City",
        "questions": [
            "Does your child get very distressed or cover ears due to everyday noises?",
            "Does your child spontaneously engage in pretend play on their own?",
            "Does your child use pointing to share interest, not just to request?",
            "Does your child actively initiate and enjoy social interaction games like peek-a-boo?",
            "Does your child frequently seek physical closeness beyond normal affection?",
            "Does your child consistently respond when their name is called without visual cues?",
            "Does your child frequently stare into space without engaging with surroundings?",
            "Does your child attempt to interact with other children?",
            "Does your child seek climbing activities repeatedly beyond normal play?",
            "Does your child repeatedly make unusual finger or hand movements near their face?"
        ],
        "about_html": `
            <h3>🧠 Neurodevelopmental Condition</h3>
            <p>ASD affects how a child communicates, interacts, and behaves.</p>
            <h3>🔍 Common Symptoms</h3>
            <ul>
                <li>Limited eye contact</li>
                <li>Not responding to name</li>
                <li>Repetitive movements</li>
                <li>Difficulty in social interaction</li>
            </ul>
            <h3>🧬 Possible Causes</h3>
            <ul>
                <li>Genetic factors</li>
                <li>Pregnancy-related complications</li>
                <li>Differences in brain development</li>
            </ul>
            <h3>✅ Support & Solutions</h3>
            <ul>
                <li>Early detection is very important</li>
                <li>Speech therapy</li>
                <li>Behavioral therapy</li>
            </ul>
        `
    },
    "Hindi": {
        "nav_about": "ASD के बारे में",
        "nav_image": "इमेज स्क्रीनिंग",
        "nav_quiz": "प्रश्नावली",
        "nav_centers": "केंद्र खोजें",
        "about_title": "ऑटिज़्म स्पेक्ट्रम डिसऑर्डर (ASD) क्या है?",
        "image_title": "स्क्रीनिंग के लिए बच्चे की फोटो अपलोड करें",
        "upload_prompt": "यहाँ क्लिक करें या फोटो खींच कर लाएं",
        "btn_predict": "पूर्वानुमान करें",
        "image_note": "⚠ ध्यान दें: छवि-आधारित परिणाम प्रयोगात्मक हैं। कृपया बेहतर सटीकता के लिए प्रश्नावली का उपयोग करें।",
        "quiz_title": "प्रश्नावली",
        "lbl_age": "बच्चे की उम्र (महीनों में)",
        "lbl_sex": "लिंग",
        "lbl_jaundice": "पीलिया का इतिहास?",
        "lbl_family": "परिवार में ASD का इतिहास?",
        "btn_submit": "सबमिट करें",
        "btn_print": "🖨 परिणाम प्रिंट / सेव करें",
        "centers_title": "आस-पास के ऑटिज़्म केंद्र खोजें",
        "lbl_city": "शहर चुनें",
        "questions": [
            "क्या आपका बच्चा रोज़मर्रा की आवाज़ों से बहुत ज़्यादा परेशान हो जाता है?",
            "क्या बच्चा खुद से कल्पनात्मक खेल करता है?",
            "क्या बच्चा बार-बार और ज़रूरत से ज़्यादा चढ़ने की कोशिश करता है?",
            "क्या बच्चा खुद से आंख-मिचौली (peek-a-boo) जैसे सामाजिक खेल शुरू करता है?",
            "क्या बच्चा बार-बार दुलार या शारीरिक संपर्क माँगता है?",
            "क्या बच्चा नाम पुकारने पर तुरंत प्रतिक्रिया देता है?",
            "क्या बच्चा अक्सर बिना कारण किसी जगह को घूरता रहता है?",
            "क्या बच्चा अन्य बच्चों से जुड़ने की कोशिश करता है?",
            "क्या बच्चा दिलचस्प चीज़ें दिखाने के लिए इशारा करता है?",
            "क्या बच्चा बार-बार चेहरे के पास उंगलियों या हाथों की अजीब हरकतें करता है?"
        ],
        "about_html": `
            <h3>🧠 ऑटिज़्म स्पेक्ट्रम डिसऑर्डर</h3>
            <p>ASD एक विकास संबंधी स्थिति है जो संवाद और व्यवहार को प्रभावित करती है।</p>
            <h3>🔍 सामान्य लक्षण</h3>
            <ul>
                <li>आँखों से संपर्क कम</li>
                <li>नाम बुलाने पर प्रतिक्रिया न देना</li>
                <li>बार-बार एक-सी हरकतें</li>
                <li>सामाजिक खेलों में रुचि कम</li>
            </ul>
            <h3>🧬 संभावित कारण</h3>
            <ul>
                <li>आनुवंशिक कारण</li>
                <li>गर्भावस्था के दौरान जटिलताएँ</li>
            </ul>
            <h3>✅ समाधान / सहायता</h3>
            <ul>
                <li>जल्दी पहचान बहुत ज़रूरी है</li>
                <li>स्पीच थेरेपी</li>
                <li>बिहेवियर थेरेपी</li>
            </ul>
        `
    }
};

let currentLang = "English";
let uploadedImageFile = null;

document.addEventListener('DOMContentLoaded', () => {
    initTabs();
    initLanguage();
    initImageUpload();
    initQuestionnaire();
    initCenters();
    updateText();
});

// --- Tabs ---
function initTabs() {
    const tabs = document.querySelectorAll('.nav-btn');
    const contents = document.querySelectorAll('.tab-content');

    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            const target = tab.dataset.tab;

            tabs.forEach(t => t.classList.remove('active'));
            contents.forEach(c => c.classList.remove('active'));

            tab.classList.add('active');
            document.getElementById(target).classList.add('active');
        });
    });
}

// --- Language ---
function initLanguage() {
    const select = document.getElementById('language-select');
    select.addEventListener('change', (e) => {
        currentLang = e.target.value;
        updateText();
    });

    const themeBtn = document.getElementById('theme-toggle');
    themeBtn.addEventListener('click', () => {
        const body = document.body;
        if (body.getAttribute('data-theme') === 'dark') {
            body.removeAttribute('data-theme');
            themeBtn.textContent = '🌙';
        } else {
            body.setAttribute('data-theme', 'dark');
            themeBtn.textContent = '☀';
        }
    });
}

function updateText() {
    const res = RESOURCES[currentLang];

    document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.dataset.i18n;
        if (res[key]) el.innerText = res[key];
    });

    const aboutContainer = document.getElementById('about-content');
    if (aboutContainer && res.about_html) {
        aboutContainer.innerHTML = res.about_html;
    }

    renderQuestions();
}

// --- Image Upload ---
function initImageUpload() {
    const dropZone = document.getElementById('drop-zone');
    const input = document.getElementById('image-upload');
    const preview = document.getElementById('preview-image');
    const predictBtn = document.getElementById('predict-image-btn');

    dropZone.addEventListener('click', () => input.click());

    dropZone.addEventListener('dragover', (e) => {
        e.preventDefault();
        dropZone.classList.add('dragover');
    });

    dropZone.addEventListener('dragleave', () => dropZone.classList.remove('dragover'));

    dropZone.addEventListener('drop', (e) => {
        e.preventDefault();
        dropZone.classList.remove('dragover');
        if (e.dataTransfer.files.length) {
            handleFile(e.dataTransfer.files[0]);
        }
    });

    input.addEventListener('change', (e) => {
        if (e.target.files.length) {
            handleFile(e.target.files[0]);
        }
    });

    function handleFile(file) {
        if (!file.type.startsWith('image/')) return;

        uploadedImageFile = file;
        const reader = new FileReader();
        reader.onload = (e) => {
            preview.src = e.target.result;
            preview.classList.remove('hidden');
            document.querySelector('.upload-placeholder').classList.add('hidden');
            predictBtn.disabled = false;
        };
        reader.readAsDataURL(file);
    }

    predictBtn.addEventListener('click', async () => {
        if (!uploadedImageFile) return;

        predictBtn.textContent = "Processing...";
        predictBtn.disabled = true;

        const formData = new FormData();
        formData.append('file', uploadedImageFile);

        try {
            const response = await fetch('/api/predict/image', {
                method: 'POST',
                body: formData
            });

            const data = await response.json();

            if (data.success) {
                const resultImg = document.getElementById('annotated-image');
                resultImg.src = data.annotated_image;
                document.getElementById('image-result').classList.remove('hidden');
            } else {
                alert(data.message || "Error processing image");
            }
        } catch (error) {
            console.error(error);
            alert("Failed to connect to server");
        } finally {
            predictBtn.textContent = RESOURCES[currentLang].btn_predict;
            predictBtn.disabled = false;
        }
    });
}

// --- Questionnaire ---
function renderQuestions() {
    const container = document.getElementById('questions-container');
    container.innerHTML = '';

    // In web1.py, selectbox was ['No', 'Yes'], so 0=No, 1=Yes.
    // We will use 0 for No, 1 for Yes
    RESOURCES[currentLang].questions.forEach((q, index) => {
        const div = document.createElement('div');
        div.className = 'question-item';
        div.innerHTML = `
            <div class="question-text">${index + 1}. ${q}</div>
            <select class="quiz-answer" data-index="${index}">
                <option value="0">${currentLang === 'Hindi' ? 'नहीं (No)' : 'No'}</option>
                <option value="1">${currentLang === 'Hindi' ? 'हाँ (Yes)' : 'Yes'}</option>
            </select>
        `;
        container.appendChild(div);
    });
}

function initQuestionnaire() {
    const form = document.getElementById('quiz-form');
    // renderQuestions is called in updateText()

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const answers = [];
        document.querySelectorAll('.quiz-answer').forEach(select => {
            answers.push(parseInt(select.value));
        });

        const age = parseInt(document.getElementById('age').value);
        const sex = parseInt(document.getElementById('sex').value);
        const jaundice = parseInt(document.getElementById('jaundice').value);
        const family_asd = parseInt(document.getElementById('family_asd').value);

        const payload = {
            answers: answers,
            age_months: age,
            sex: sex,
            jaundice: jaundice,
            family_asd: family_asd
        };

        const resultBox = document.getElementById('quiz-result');
        const title = document.getElementById('quiz-result-title');
        const msg = document.getElementById('quiz-result-msg');

        try {
            const response = await fetch('/api/predict/questionnaire', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(payload)
            });
            const data = await response.json();

            resultBox.classList.remove('hidden');
            if (data.asd_traits_detected) {
                title.textContent = "⚠ Possible ASD Traits Detected";
                title.className = "error-msg";
                msg.textContent = "Based on your answers, there are indicators of ASD traits. Please consult a specialist for a formal assessment.";
            } else {
                title.textContent = "✔ No ASD Traits Detected";
                title.className = "success-msg";
                msg.textContent = "Based on your answers, few or no ASD traits were indicated.";
            }

            // Display Impressions
            const existingImpressions = document.getElementById('impressions-list');
            if (existingImpressions) existingImpressions.remove();

            if (data.impressions && data.impressions.length > 0) {
                const impContainer = document.createElement('div');
                impContainer.id = 'impressions-list';
                impContainer.style.textAlign = 'left';
                impContainer.style.marginTop = '20px';

                const impTitle = document.createElement('h4');
                impTitle.textContent = "Impression (Behaviours Flags):";
                impTitle.style.marginBottom = '10px';
                impContainer.appendChild(impTitle);

                const ul = document.createElement('ul');
                data.impressions.forEach(imp => {
                    const li = document.createElement('li');
                    li.textContent = imp;
                    ul.appendChild(li);
                });
                impContainer.appendChild(ul);

                // Insert before the print button
                const printBtn = document.getElementById('print-btn');
                resultBox.insertBefore(impContainer, printBtn);
            } else if (data.asd_traits_detected) {
                // If ASD detected but no specific impressions (unlikely with current logic but possible)
                // maybe show nothing or a generic message?
                // For now, doing nothing.
            }

            // Show Print Button
            document.getElementById('print-btn').classList.remove('hidden');

        } catch (error) {
            console.error(error);
            alert("Error submitting questionnaire");
        }
    });

    // Print Button Logic
    document.getElementById('print-btn').addEventListener('click', () => {
        window.print();
    });
}

// --- Centers ---
function initCenters() {
    const select = document.getElementById('city-select');
    const container = document.getElementById('centers-list');

    async function loadCenters(city) {
        container.innerHTML = '<p>Loading...</p>';
        try {
            const response = await fetch(`/api/centers/${city}`);
            const data = await response.json();

            container.innerHTML = '';
            if (data.length === 0) {
                container.innerHTML = '<p>No centers found for this city.</p>';
                return;
            }

            data.forEach(center => {
                const div = document.createElement('div');
                div.className = 'center-item';
                div.innerHTML = `
                    <strong>${center.name}</strong>
                    <a href="${center.link}" target="_blank" class="center-link">Visit Website ↗</a>
                `;
                container.appendChild(div);
            });
        } catch (error) {
            console.error(error);
            container.innerHTML = '<p>Error loading centers.</p>';
        }
    }

    select.addEventListener('change', () => {
        loadCenters(select.value);
    });

    // Initial load
    loadCenters(select.value);
}
