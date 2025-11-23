import streamlit as st
from datetime import datetime
import requests
import json

BASE_URL = "http://localhost:8000"

# Page config with custom theme
st.set_page_config(
    page_title="✈️ WanderMind AI",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for stunning UI
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&family=Inter:wght@300;400;500;600&display=swap');
    
    /* Global Styles */
    * {
        font-family: 'Inter', sans-serif;
    }
    
    h1, h2, h3 {
        font-family: 'Poppins', sans-serif;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Animated gradient background */
    .stApp {
        background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
    }
    
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Glassmorphic container */
    .glass-container {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.3);
        padding: 2rem;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        margin: 1rem 0;
    }
    
    /* Hero section */
    .hero {
        text-align: center;
        padding: 3rem 0 2rem 0;
        animation: fadeInDown 1s ease-out;
    }
    
    .hero h1 {
        font-size: 3.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    .hero p {
        font-size: 1.3rem;
        color: #2d3748;
        font-weight: 500;
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
    
    /* Input form styling */
    .stTextInput > div > div > input {
        background: rgba(255, 255, 255, 0.9);
        border: 2px solid rgba(255, 255, 255, 0.3);
        border-radius: 15px;
        padding: 1rem;
        font-size: 1.1rem;
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 15px;
        padding: 0.75rem 2rem;
        font-size: 1.1rem;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
    }
    
    /* Result card */
    .result-card {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        padding: 2rem;
        margin: 1.5rem 0;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
        animation: slideInUp 0.6s ease-out;
    }
    
    @keyframes slideInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
    }
    
    /* Loading animation */
    .stSpinner > div {
        border-top-color: #667eea !important;
    }
    
    /* Success/Error messages */
    .stSuccess, .stError {
        border-radius: 15px;
        padding: 1rem;
    }
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 10px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(255, 255, 255, 0.1);
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if "trip_history" not in st.session_state:
    st.session_state.trip_history = []

# Sidebar
with st.sidebar:
    st.markdown("### 🗺️ Trip History")
    if st.session_state.trip_history:
        for i, trip in enumerate(reversed(st.session_state.trip_history[-5:])):
            with st.expander(f"Trip {len(st.session_state.trip_history) - i}"):
                st.write(f"**Query:** {trip['query'][:50]}...")
                st.write(f"**Date:** {trip['timestamp']}")
    else:
        st.info("No trips planned yet!")
    
    st.markdown("---")
    st.markdown("### ⚙️ Settings")
    show_timestamps = st.checkbox("Show timestamps", value=True)
    
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666; font-size: 0.9rem;'>
        <p>Powered by AI 🤖</p>
        <p>Made with ❤️ using Streamlit</p>
    </div>
    """, unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class='hero'>
    <h1>🌍 WanderMind AI</h1>
    <p>Your Intelligent Travel Companion</p>
</div>
""", unsafe_allow_html=True)

# Main content in glassmorphic container
st.markdown("<div class='glass-container'>", unsafe_allow_html=True)

st.markdown("### ✨ Plan Your Perfect Journey")
st.markdown("Tell me about your dream destination, preferences, budget, and dates. I'll create a personalized itinerary just for you!")

# Input form
with st.form(key="trip_form", clear_on_submit=True):
    col1, col2 = st.columns([4, 1])
    
    with col1:
        user_input = st.text_input(
            "Where would you like to go?",
            placeholder="e.g., 5-day Japan trip in April with cherry blossoms, mid-range budget",
            label_visibility="collapsed"
        )
    
    with col2:
        submit_button = st.form_submit_button("✈️ Plan Trip", use_container_width=True)

st.markdown("</div>", unsafe_allow_html=True)

# Handle submission
if submit_button and user_input.strip():
    try:
        with st.spinner("🔮 Crafting your perfect itinerary..."):
            payload = {"query": user_input}
            response = requests.post(f"{BASE_URL}/query", json=payload, timeout=60)
        
        if response.ok:
            answer = response.json().get("answer", "No answer returned.")
            
            # Save to history
            st.session_state.trip_history.append({
                "query": user_input,
                "answer": answer,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
            
            # Display result in beautiful card
            st.markdown("<div class='result-card'>", unsafe_allow_html=True)
            
            # Header
            st.markdown("### 🎉 Your Personalized Trip Plan")
            if show_timestamps:
                st.caption(f"Generated on {datetime.now().strftime('%B %d, %Y at %H:%M')}")
            
            st.markdown("---")
            
            # Trip content
            st.markdown(answer)
            
            st.markdown("---")
            
            # Action buttons
            col1, col2, col3 = st.columns(3)
            
            with col1:
                if st.button("📋 Copy to Clipboard"):
                    st.toast("✅ Copied to clipboard!", icon="✅")
            
            with col2:
                # Download as markdown
                st.download_button(
                    label="📥 Download Plan",
                    data=answer,
                    file_name=f"trip_plan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md",
                    mime="text/markdown"
                )
            
            with col3:
                if st.button("🔄 Plan Another Trip"):
                    st.rerun()
            
            st.markdown("</div>", unsafe_allow_html=True)
            
            # Disclaimer
            st.info("💡 **Note:** This itinerary is AI-generated. Please verify details before making bookings.")
            
        else:
            st.error(f"❌ Failed to generate trip plan. Status: {response.status_code}")
            with st.expander("Error Details"):
                st.code(response.text or "<no response body>")
    
    except requests.exceptions.Timeout:
        st.error("⏱️ Request timed out. The AI is taking longer than expected. Please try again.")
    except requests.exceptions.ConnectionError:
        st.error("🔌 Cannot connect to the backend. Make sure the server is running at " + BASE_URL)
    except Exception as e:
        st.error(f"❌ An unexpected error occurred: {str(e)}")
        with st.expander("Error Details"):
            st.exception(e)

# Footer
st.markdown("""
<div style='text-align: center; margin-top: 3rem; padding: 2rem; color: #2d3748;'>
    <p style='font-size: 0.9rem;'>✨ Start planning your next adventure today! ✨</p>
</div>
""", unsafe_allow_html=True)
