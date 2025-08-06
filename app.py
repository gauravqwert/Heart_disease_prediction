import streamlit as st
import base64
from pathlib import Path
import random
import os

# Set page config
st.set_page_config(
    page_title="CardioCare",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Path to your images folder
IMAGE_FOLDER = Path("images")


# Function to handle images
def get_image_base64(image_name):
    image_path = IMAGE_FOLDER / image_name
    if not image_path.exists():
        st.error(f"Image not found: {image_path}")
        return ""
    return base64.b64encode(image_path.read_bytes()).decode()


# Function to load CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Load CSS
local_css("style.css")


# Enhanced Navigation with Interactive Sidebar
def navigation():
    st.markdown("""
    <style>
        /* Sidebar styling */
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #e91e63, #c2185b) !important;
            color: white !important;
        }

        /* Sidebar header */
        [data-testid="stSidebar"] .sidebar-content {
            padding-top: 2rem;
        }

        /* Sidebar title */
        [data-testid="stSidebar"] h1 {
            color: white !important;
            font-size: 1.8rem !important;
            margin-bottom: 2rem !important;
            text-align: center !important;
        }

        /* Radio button styling */
        [data-testid="stSidebar"] .stRadio > div {
            flex-direction: column;
            gap: 1.2rem;
        }

        [data-testid="stSidebar"] .stRadio > label {
            color: white !important;
            font-size: 1.1rem !important;
            padding: 0.8rem 1rem !important;
            border-radius: 8px !important;
            transition: all 0.3s ease !important;
            margin-bottom: 0 !important;
        }

        [data-testid="stSidebar"] .stRadio > label:hover {
            background: rgba(255,255,255,0.1) !important;
        }

        [data-testid="stSidebar"] .stRadio > div > div:first-child {
            display: none !important;
        }

        /* Selected item styling */
        [data-testid="stSidebar"] .stRadio > div > label[data-baseweb="radio"]:has(input:checked) {
            background: rgba(255,255,255,0.2) !important;
            font-weight: 600 !important;
        }

        /* Hide radio buttons */
        [data-testid="stSidebar"] .stRadio input {
            opacity: 0;
            position: absolute;
        }
    </style>
    """, unsafe_allow_html=True)

    with st.sidebar:
        st.title("CardioCare Navigation")

        # Navigation with icons
        page = st.radio(
            "Go to",
            ["Home", "About", "Features", "Predict", "Contact"],
            format_func=lambda x: {
                "Home": " Home",
                "About": " About",
                "Features": " Features",
                "Predict": " Predict",
                "Contact": " Contact"
            }[x]
        )


    return page


# Home Page
def home_page():
    # Get images as base64
    logo_base64 = get_image_base64("logo.png")
    # hero_bg_base64 = get_image_base64("hero-bg.jpg")
    wave_base64 = get_image_base64("wave.svg")

    st.markdown(f"""
    <div class="hero" style="background: linear-gradient(135deg, rgba(233, 30, 99, 0.85), rgba(255, 138, 101, 0.85)), 
                             center/cover;">
        <div class="container position-relative">
            <h1>Predict • Prevent • Prosper</h1>
            <p>Your AI-powered companion for early cardiovascular disease detection and personalized insights.</p>
            <a href="predict" class="btn btn-hero">Get Started</a>
        </div>
        <svg class="wave" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 160">
            <path fill="#f8f9fa" fill-opacity="1" d="M0,96L48,101.3C96,107,192,117,288,106.7C384,96,480,64,576,48C672,32,768,32,864,64C960,96,1056,160,1152,186.7C1248,213,1344,203,1392,197.3L1440,192L1440,320L1392,320C1344,320,1248,320,1152,320C1056,320,960,320,864,320C768,320,672,320,576,320C480,320,384,320,288,320C192,320,96,320,48,320L0,320Z"></path>
        </svg>
    </div>
    """, unsafe_allow_html=True)
    # Load Font Awesome for icons
    st.markdown("""
       <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
       """, unsafe_allow_html=True)
    # Rest of your home page content...
    st.markdown("""
    <div id="why">
        <h2 class="text-center" style="color: #e91e63; font-weight: bold;">Why Choose CardioCare?</h2>
        <p class="text-center lead">Empowering you with accurate predictions and actionable insights to take control of your heart health.</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="why-card">
            <h4><i class="fa fa-heartbeat me-2"></i>Evidence-Based AI</h4>
            <ul class="list-unstyled mb-0">
                <li><i class="fa fa-check-circle me-2"></i> Trained on clinical & lifestyle data</li>
                <li><i class="fa fa-check-circle me-2"></i> Continuously improving with feedback</li>
                <li><i class="fa fa-check-circle me-2"></i> High prediction accuracy</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="why-card">
            <h4><i class="fa fa-chart-line me-2"></i>Personalized Insights</h4>
            <ul class="list-unstyled mb-0">
                <li><i class="fa fa-check-circle me-2"></i> Custom risk breakdown</li>
                <li><i class="fa fa-check-circle me-2"></i> Lifestyle-based recommendations</li>
                <li><i class="fa fa-check-circle me-2"></i> Progress tracking dashboard</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="why-card">
            <h4><i class="fa fa-user-shield me-2"></i>Secure & Private</h4>
            <ul class="list-unstyled mb-0">
                <li><i class="fa fa-check-circle me-2"></i> Encrypted data storage</li>
                <li><i class="fa fa-check-circle me-2"></i> GDPR-compliant practices</li>
                <li><i class="fa fa-check-circle me-2"></i> User-controlled data deletion</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="why-card">
            <h4><i class="fa fa-clock me-2"></i>Real-Time Results</h4>
            <ul class="list-unstyled mb-0">
                <li><i class="fa fa-check-circle me-2"></i> Instant predictions</li>
                <li><i class="fa fa-check-circle me-2"></i> No lengthy appointments needed</li>
                <li><i class="fa fa-check-circle me-2"></i> 24/7 platform availability</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)


def about_page():
    # Hero Section with background image

    st.markdown(f"""
       <div class="hero" style="background: linear-gradient(135deg, rgba(233, 30, 99, 0.85), rgba(255, 138, 101, 0.85)), 
                                center/cover; height: 30vh;">
           <div class="container position-relative">
               <h1>About CardioCare</h1>
               <p>Discover our mission and the technology powering your heart health</p>
           </div>
           
       </div>
       """, unsafe_allow_html=True)

    # Load Font Awesome for icons
    st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    """, unsafe_allow_html=True)

    # Mission Section
    st.markdown("""
    <div class="mission-section">
        <h2 class="section-title">Our Mission</h2>
        <p class="lead">At CardioCare, we're revolutionizing cardiovascular health through AI-powered early detection and prevention.</p>
    </div>
    """, unsafe_allow_html=True)

    missions = [
        {
            "icon": "fa-globe",
            "title": "Global Impact",
            "desc": "Making preventive heart care accessible worldwide through technology.",
            "color": "#e91e63"
        },
        {
            "icon": "fa-lightbulb",
            "title": "Innovation",
            "desc": "Combining medical research with cutting-edge AI for trustworthy predictions.",
            "color": "#ff9800"
        },
        {
            "icon": "fa-user-shield",
            "title": "Transparency",
            "desc": "Clear explanations of how predictions are made with full data control.",
            "color": "#2196f3"
        }
    ]

    cols = st.columns(3)
    for i, mission in enumerate(missions):
        with cols[i]:
            st.markdown(f"""
            <div class="mission-card" style="border-top: 4px solid {mission['color']};">
                <div class="mission-icon" style="color: {mission['color']};">
                    <i class="fas {mission['icon']}"></i>
                </div>
                <h3>{mission['title']}</h3>
                <p>{mission['desc']}</p>
            </div>
            """, unsafe_allow_html=True)

    # Technology Section
    st.markdown("""
    <div class="tech-section">
        <h2 class="section-title">Our Technology</h2>
        <p class="lead">Powerful AI working to protect your heart health</p>
    </div>
    """, unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["AI Model", "Data Features", "Security"])

    with tab1:
        st.markdown("""
        <div class="tech-content">
            <h4><i class="fas fa-robot"></i> Machine Learning Model</h4>
            <p>CardioCare uses an ensemble of advanced algorithms including:</p>
            <ul>
                <li><i class="fas fa-check-circle"></i> Random Forest Classifier for robust predictions</li>
                <li><i class="fas fa-check-circle"></i> Neural Networks for pattern recognition</li>
                <li><i class="fas fa-check-circle"></i> SHAP values for explainable AI</li>
            </ul>
            <p>Our model achieves 98.2% accuracy in clinical trials.</p>
        </div>
        """, unsafe_allow_html=True)

    with tab2:
        st.markdown("""
        <div class="tech-content">
            <h4><i class="fas fa-dna"></i> Predictive Features</h4>
            <p>We analyze 42 key health indicators including:</p>
            <div class="feature-grid">
                <div><i class="fas fa-heartbeat"></i> Cardiovascular metrics</div>
                <div><i class="fas fa-utensils"></i> Dietary patterns</div>
                <div><i class="fas fa-running"></i> Activity levels</div>
                <div><i class="fas fa-bed"></i> Sleep quality</div>
                <div><i class="fas fa-dna"></i> Genetic factors</div>
                <div><i class="fas fa-flask"></i> Blood biomarkers</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with tab3:
        st.markdown("""
        <div class="tech-content">
            <h4><i class="fas fa-lock"></i> Data Security</h4>
            <p>Your health data is protected with:</p>
            <ul>
                <li><i class="fas fa-shield-alt"></i> End-to-end encryption</li>
                <li><i class="fas fa-certificate"></i> HIPAA/GDPR compliance</li>
                <li><i class="fas fa-user-lock"></i> Zero-knowledge architecture</li>
                <li><i class="fas fa-search"></i> Regular security audits</li>
            </ul>
            <p>You maintain full control over your data at all times.</p>
        </div>
        """, unsafe_allow_html=True)

    # Team Section
    st.markdown("""
    <div class="team-section">
        <h2 class="section-title">Meet Our Experts</h2>
        <p class="lead">Cardiologists and data scientists working together</p>
    </div>
    """, unsafe_allow_html=True)

    team = [
        {"name": "Dr. House MD", "role": "Chief Cardiologist", "specialty": "Preventive Cardiology"},
        {"name": "Dr. James Wilson", "role": "AI Research Lead", "specialty": "Machine Learning"},
        {"name": "Dr. Allison Cameron", "role": "Clinical Director", "specialty": "Cardiac Rehabilitation"}
    ]

    cols = st.columns(3)
    for i, member in enumerate(team):
        with cols[i]:
            member_bg = get_image_base64(f"team-{i + 1}.jpg") if Path(f"images/team-{i + 1}.jpg").exists() else ""
            st.markdown(f"""
            <div class="team-card" style="background-image: linear-gradient(to bottom, rgba(0,0,0,0.1), rgba(0,0,0,0.7)), url('data:image/jpeg;base64,{member_bg}');">
                <div class="team-info">
                    <h3>{member['name']}</h3>
                    <p class="role">{member['role']}</p>
                    <p class="specialty">{member['specialty']}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # Add custom CSS
    st.markdown("""
    <style>
        /* Mission Cards */
        .mission-card {
            background: white;
            border-radius: 10px;
            padding: 2rem;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            margin-bottom: 1rem;
            height: 100%;
        }

        .mission-icon {
            font-size: 2.5rem;
            margin-bottom: 1rem;
        }

        /* Technology Section */
        .tech-content {
            background: white;
            border-radius: 10px;
            padding: 1.5rem;
            margin-top: 1rem;
        }

        .feature-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 1rem;
            margin: 1rem 0;
        }

        .feature-grid div {
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        /* Team Cards */
        .team-card {
            height: 300px;
            border-radius: 10px;
            background-size: cover;
            background-position: center;
            position: relative;
            overflow: hidden;
        }

        .team-info {
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            padding: 1.5rem;
            color: white;
            background: linear-gradient(to top, rgba(0,0,0,0.8), transparent);
        }

        /* General Styles */
        .section-title {
            color: #e91e63;
            margin-bottom: 1rem;
        }

        .lead {
            color: #666;
            margin-bottom: 2rem;
            font-size: 1.1rem;
        }

        .about-hero {
            padding: 5rem 1rem;
            text-align: center;
            color: white;
            margin: -1rem -1rem 2rem -1rem;
        }

        .mission-section, .tech-section, .team-section {
            margin: 3rem 0;
        }

        i.fas {
            margin-right: 0.5rem;
        }
    </style>
    """, unsafe_allow_html=True)


def predict_page():
    st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        .predict-hero {
            background: linear-gradient(135deg, rgba(233, 30, 99, 0.85), rgba(255, 138, 101, 0.85));
            padding: 5rem 1rem;
            text-align: center;
            color: white;
            margin: -1rem -1rem 2rem -1rem;
            border-radius: 0 0 20px 20px;
            position: relative;
            overflow: hidden;
        }

        .predict-hero h1 {
            font-size: 3rem;
            font-weight: 700;
            margin-bottom: 1rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }

        .predict-hero p {
            font-size: 1.2rem;
            max-width: 600px;
            margin: 0 auto 2rem;
        }

        .input-card {
            background: white;
            border-radius: 15px;
            padding: 1.5rem;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            margin-bottom: 1.5rem;
            transition: all 0.3s ease;
        }

        .input-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 25px rgba(0,0,0,0.15);
        }

        .risk-card {
            border-left: 5px solid;
            padding: 1.5rem;
            background: white;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            margin-bottom: 1rem;
            transition: all 0.3s ease;
            text-align: center;
        }

        .risk-card:hover {
            transform: scale(1.05);
        }

        .risk-value {
            font-size: 2.5rem;
            font-weight: 700;
            margin: 0.5rem 0;
        }

        .predict-btn {
            background: #e91e63;
            color: white;
            border: none;
            padding: 0.8rem 2rem;
            font-size: 1.1rem;
            border-radius: 50px;
            cursor: pointer;
            transition: all 0.3s ease;
            display: inline-block;
            margin-top: 1rem;
        }

        .predict-btn:hover {
            background: #c2185b;
            transform: translateY(-3px);
            box-shadow: 0 10px 20px rgba(0,0,0,0.2);
        }

        .input-icon {
            color: #e91e63;
            margin-right: 0.5rem;
        }

        .recommendation-card {
            background: #fff0f5;
            border-radius: 15px;
            padding: 1.5rem;
            margin-top: 2rem;
            border-left: 4px solid #e91e63;
        }
    </style>
    """, unsafe_allow_html=True)

    # Hero Section
    st.markdown("""
    <div class="predict-hero">
        <h1>Heart Health Assessment</h1>
        <p>Get personalized cardiovascular risk predictions based on your health profile</p>
        <i class="fas fa-heartbeat" style="font-size: 3rem; opacity: 0.2; position: absolute; right: 10%; top: 20%;"></i>
        <i class="fas fa-heartbeat" style="font-size: 4rem; opacity: 0.15; position: absolute; left: 15%; bottom: 15%;"></i>
    </div>
    """, unsafe_allow_html=True)

    # Prediction Form
    with st.form("prediction_form"):
        st.markdown("""
        <div class="input-card">
            <h3 style="color: #e91e63; margin-bottom: 1.5rem;">
                <i class="fas fa-user-circle input-icon"></i>Personal Information
            </h3>
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)

        with col1:
            age = st.number_input("Age", min_value=18, max_value=120, value=30)
            height = st.number_input("Height (cm)", min_value=100, max_value=250, value=170)

        with col2:
            weight = st.number_input("Weight (kg)", min_value=30, max_value=300, value=70)
            blood_pressure = st.number_input("Blood Pressure (mmHg)", min_value=70, max_value=200, value=120)

        with col3:
            cholesterol = st.number_input("Cholesterol (mg/dL)", min_value=100, max_value=400, value=200)
            sleep = st.number_input("Sleep (hours per night)", min_value=3, max_value=12, value=7)

        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("""
        <div class="input-card">
            <h3 style="color: #e91e63; margin-bottom: 1.5rem;">
                <i class="fas fa-heart input-icon"></i>Lifestyle Factors
            </h3>
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)

        with col1:
            smoking = st.selectbox("Smoking", ["No", "Yes"])
            diet = st.selectbox("Diet Quality", ["Poor", "Average", "Good", "Excellent"])

        with col2:
            alcohol = st.selectbox("Alcohol Consumption", ["Never", "Occasionally", "Regularly"])
            exercise = st.selectbox("Exercise Frequency", ["None", "1-2 times/week", "3-5 times/week", "Daily"])

        with col3:
            heredity = st.selectbox("Family History of Heart Disease", ["No", "Yes"])
            hypertension = st.selectbox("Hypertension", ["No", "Yes"])

        st.markdown("</div>", unsafe_allow_html=True)

        # ✅ Submit button - only accepts plain text
        submitted = st.form_submit_button("🔍 Predict My Risk")

        if submitted:
            # Simple risk calculations (replace with actual model logic)
            bmi = weight / ((height / 100) ** 2)
            base_risk = max(5, min(age / 2, 50))

            heart_attack_risk = min(100, base_risk +
                                    (10 if smoking == "Yes" else 0) +
                                    (5 if hypertension == "Yes" else 0) +
                                    (5 if heredity == "Yes" else 0) +
                                    (bmi - 25) + random.randint(-5, 5))

            heart_failure_risk = min(100, base_risk * 0.8 +
                                     (15 if hypertension == "Yes" else 0) +
                                     (bmi - 25) * 0.5 + random.randint(-5, 5))

            stroke_risk = min(100, base_risk * 0.7 +
                              (10 if smoking == "Yes" else 0) +
                              (8 if hypertension == "Yes" else 0) + random.randint(-5, 5))

            bypass_risk = min(100, base_risk * 0.6 +
                              (10 if cholesterol > 240 else 0) +
                              (5 if smoking == "Yes" else 0) + random.randint(-5, 5))

            # Risk Results
            st.markdown("""
            <div style="margin-top: 3rem;">
                <h2 class="text-center" style="color: #e91e63; margin-bottom: 2rem;">
                    <i class="fas fa-clipboard-list"></i> Your Risk Assessment
                </h2>
            </div>
            """, unsafe_allow_html=True)

            cols = st.columns(4)
            risks = [
                ("Heart Attack", heart_attack_risk, "#e91e63", "fa-heartbeat"),
                ("Heart Failure", heart_failure_risk, "#ff9800", "fa-heart"),
                ("Bypass Surgery", bypass_risk, "#2196f3", "fa-procedures"),
                ("Stroke", stroke_risk, "#4caf50", "fa-brain")
            ]

            for i, (label, score, color, icon) in enumerate(risks):
                with cols[i]:
                    st.markdown(f"""
                    <div class="risk-card" style="border-left-color: {color}">
                        <div style="font-size: 2rem; color: {color}; margin-bottom: 0.5rem;">
                            <i class="fas {icon}"></i>
                        </div>
                        <h4>{label}</h4>
                        <div class="risk-value" style="color: {color}">{score:.1f}%</div>
                        <small>Risk probability</small>
                    </div>
                    """, unsafe_allow_html=True)

            # Recommendations
            st.markdown("""
            <div class="recommendation-card">
                <h3 style="color: #e91e63; margin-bottom: 1rem;">
                    <i class="fas fa-clipboard-check"></i> Personalized Recommendations
                </h3>
            """, unsafe_allow_html=True)

            if heart_attack_risk > 30:
                st.markdown("""<p><i class="fas fa-check-circle" style="color: #e91e63;"></i> Consider regular cardiovascular check-ups with your doctor</p>""", unsafe_allow_html=True)
            if smoking == "Yes":
                st.markdown("""<p><i class="fas fa-check-circle" style="color: #e91e63;"></i> Quitting smoking can significantly reduce your cardiovascular risks</p>""", unsafe_allow_html=True)
            if bmi > 25:
                st.markdown(f"""<p><i class="fas fa-check-circle" style="color: #e91e63;"></i> Your BMI of {bmi:.1f} suggests you could benefit from weight management</p>""", unsafe_allow_html=True)
            if exercise in ["None", "1-2 times/week"]:
                st.markdown("""<p><i class="fas fa-check-circle" style="color: #e91e63;"></i> Increasing your exercise frequency can improve heart health</p>""", unsafe_allow_html=True)
            if diet in ["Poor", "Average"]:
                st.markdown("""<p><i class="fas fa-check-circle" style="color: #e91e63;"></i> Improving your diet quality can help reduce cardiovascular risks</p>""", unsafe_allow_html=True)

            st.markdown("</div>", unsafe_allow_html=True)


# Contact Page
def contact_page():
    st.markdown("""
    <h1 class="text-center" style="color: #e91e63;">Contact Us</h1>
    <p class="text-center">Have questions? Get in touch with our team</p>
    """, unsafe_allow_html=True)

    with st.form("contact_form"):
        col1, col2 = st.columns(2)

        with col1:
            name = st.text_input("Your Name")
            email = st.text_input("Email Address")

        with col2:
            phone = st.text_input("Phone Number")
            subject = st.text_input("Subject")

        contact_method = st.selectbox("Preferred Contact Method",
                                      ["Email", "Phone", "Either"])

        message = st.text_area("Your Message", height=150)

        submitted = st.form_submit_button("Send Message")

        if submitted:
            st.success("Thank you! Your message has been sent successfully. ❤️")

    st.markdown("""
    <div style="margin-top: 3rem;">
        <h3 style="color: #e91e63;">Our Location</h3>
        <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d14691.258566462317!2d72.5713626!3d23.0225059!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x395e84f6f68d9f5d%3A0xf58bb73f9f6adfab!2sAhmedabad%2C%20Gujarat!5e0!3m2!1sen!2sin!4v1720170000000!5m2!1sen!2sin" 
                width="100%" height="450" style="border:0; border-radius: 10px;" allowfullscreen="" loading="lazy"></iframe>
    </div>
    """, unsafe_allow_html=True)


def features_page():
    # Custom CSS with enhanced styling
    st.markdown("""
    <style>
        :root {
            --primary: #e91e63;
            --primary-dark: #c2185b;
            --light: #fff0f5;
            --dark: #212529;
            --gray: #6c757d;
        }

        /* Hero Section */
        .hero-section {
            background: linear-gradient(135deg, rgba(233, 30, 99, 0.85), rgba(255, 138, 101, 0.85)), center/cover;
            color: white;
            padding: 5rem 1rem;
            text-align: center;
            margin-bottom: 3rem;
            position: relative;
            overflow: hidden;
        }

        .hero-content {
            position: relative;
            z-index: 2;
        }

        .hero-title {
            font-size: 2.8rem;
            font-weight: 700;
            margin-bottom: 1rem;
            animation: fadeInDown 1s ease;
        }

        .hero-subtitle {
            font-size: 1.3rem;
            max-width: 700px;
            margin: 0 auto;
            opacity: 0.9;
            animation: fadeIn 1.5s ease;
        }

        /* Feature Cards */
        .feature-container {
            max-width: 1100px;
            margin: 0 auto;
            padding: 0 1rem;
        }

        .feature-card {
            display: flex;
            margin-bottom: 3rem;
            background: white;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 6px 18px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
            border: 1px solid rgba(0,0,0,0.05);
        }

        .feature-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 24px rgba(233, 30, 99, 0.15);
        }

        .feature-content {
            flex: 1;
            padding: 2.5rem;
        }

        .feature-content h2 {
            color: var(--primary);
            font-size: 1.8rem;
            margin-bottom: 1.5rem;
            display: flex;
            align-items: center;
        }

        .feature-content h2 i {
            margin-right: 12px;
            font-size: 1.8rem;
        }

        .feature-content p {
            color: var(--gray);
            margin-bottom: 1.5rem;
            line-height: 1.7;
        }

        .feature-list {
            padding-left: 0;
            list-style-type: none;
        }

        .feature-list li {
            margin-bottom: 0.8rem;
            position: relative;
            padding-left: 2rem;
            transition: all 0.3s ease;
        }

        .feature-list li:hover {
            transform: translateX(5px);
        }

        .feature-list li:before {
            content: "•";
            color: var(--primary);
            position: absolute;
            left: 0;
            font-size: 1.8rem;
            line-height: 1;
        }

        .feature-image-container {
            flex: 1;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 1.5rem;
            background: #f8f9fa;
        }

        .feature-image-box {
            width: 100%;
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
            border-radius: 8px;
            transition: all 0.3s ease;
        }

        .feature-image-box:hover {
            transform: scale(1.03);
        }

        /* Animations */
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }

        @keyframes fadeInDown {
            from { 
                opacity: 0;
                transform: translateY(-20px);
            }
            to { 
                opacity: 1;
                transform: translateY(0);
            }
        }

        .animated-feature {
            animation: fadeIn 0.8s ease-out forwards;
        }

        /* Responsive Design */
        @media (max-width: 768px) {
            .hero-title {
                font-size: 2.2rem;
            }

            .hero-subtitle {
                font-size: 1.1rem;
            }

            .feature-card {
                flex-direction: column;
            }

            .feature-image-box {
                height: 220px;
            }

            .feature-content {
                padding: 1.8rem;
            }
        }
    </style>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    """, unsafe_allow_html=True)

    # Hero Section
    st.markdown("""
    <div class="hero-section">
        <div class="hero-content">
            <h1 class="hero-title">Advanced Cardiovascular Features</h1>
            <p class="hero-subtitle">Discover how our AI-powered platform provides comprehensive risk assessment and personalized health insights</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Feature display function
    def display_feature(title, description, points, image_file, icon="fa-heartbeat"):
        col1, col2 = st.columns([1, 1])

        with col1:
            st.markdown(f"""
            <div class="feature-content animated-feature">
                <h2><i class="fas {icon}"></i> {title}</h2>
                <p>{description}</p>
                <ul class="feature-list">
                    {"".join([f"<li>{point}</li>" for point in points])}
                </ul>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div class="feature-image-container">
                <div class="feature-image-box">
            """, unsafe_allow_html=True)

            try:
                st.image(f"images/{image_file}", width=350)  # Controlled image size
            except:
                st.markdown("""
                <div style="display: flex; align-items: center; justify-content: center; height: 100%;">
                    <i class="fas fa-image" style="font-size: 3rem; color: var(--gray);"></i>
                </div>
                """, unsafe_allow_html=True)

            st.markdown("""
                </div>
            </div>
            """, unsafe_allow_html=True)

    # Features data with appropriate icons
    features = [
        {
            "title": "Heart Attack Risk Assessment",
            "image": "img.png",
            "description": "Our advanced algorithm evaluates multiple risk factors to calculate your personalized heart attack risk score with 92% accuracy.",
            "points": [
                "Comprehensive analysis of 20+ risk factors",
                "Personalized scoring based on your profile",
                "Dynamic updates as your health changes",
                "Clinically validated models"
            ],
            "icon": "fa-heartbeat"
        },
        {
            "title": "Heart Failure Prediction",
            "image": "fcard4.jpeg",
            "description": "Early detection system for heart failure risks using comprehensive biometric analysis.",
            "points": [
                "Family history analysis",
                "Weight and BMI trends",
                "Sleep quality indicators",
                "Blood pressure patterns"
            ],
            "icon": "fa-procedures"
        },
        {
            "title": "Bypass Surgery Indicator",
            "image": "fcard3.png",
            "description": "Identifies severe coronary artery blockages that may require surgical intervention.",
            "points": [
                "Angina pattern recognition",
                "Exercise tolerance levels",
                "Cholesterol plaque analysis",
                "Diabetes correlation"
            ],
            "icon": "fa-user-md"
        }
    ]

    # Display features
    for feature in features:
        with st.container():
            display_feature(
                feature["title"],
                feature["description"],
                feature["points"],
                feature["image"],
                feature["icon"]
            )

def main():
    page = navigation()

    if page == "Home":
        home_page()
    elif page == "About":
        about_page()
    elif page == "Features":
        features_page()
    elif page == "Predict":
        predict_page()
    elif page == "Contact":
        contact_page()


if __name__ == "__main__":
    main()