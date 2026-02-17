import streamlit as st
import pandas as pd
import time

# --- V4.0 ULTRA CONFIGURATION ---
st.set_page_config(page_title="SENTINEL V4.0 | HARI ADMIN", page_icon="⚡", layout="wide")

# Custom Cyberpunk CSS
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #00ff41; font-family: 'Courier New', monospace; }
    .stMetric { background: #000; border: 1px solid #00ff41; border-radius: 5px; box-shadow: 0 0 10px #00ff41; }
    .stSidebar { background-color: #000; border-right: 1px dotted #00ff41; }
    .stButton>button { background: transparent; color: #00ff41; border: 1px solid #00ff41; width: 100%; }
    .stButton>button:hover { background: #00ff41; color: black; }
    </style>
    """, unsafe_allow_html=True)

# --- AUTHENTICATION LOGIC ---
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

def check_login(user, pwd):
    if user == "Admin_Hari" and pwd == "Hari786":
        st.session_state['authenticated'] = True
    else:
        st.error("ACCESS DENIED: INVALID CREDENTIALS")

# --- APP ROUTING ---
if not st.session_state['authenticated']:
    # --- LOGIN SCREEN ---
    st.title("⚡ SENTINEL V4.0: SECURE GATEWAY")
    col1, col2, col3 = st.columns([1,2,1])
    
    with col2:
        st.markdown("### ENTER ENCRYPTION KEY")
        u = st.text_input("ADMIN_ID")
        p = st.text_input("ACCESS_KEY", type="password")
        if st.button("INITIATE PROTOCOL"):
            with st.spinner("Decrypting..."):
                time.sleep(1.5)
                check_login(u, p)
                if st.session_state['authenticated']:
                    st.rerun()
else:
    # --- ADMIN DASHBOARD ---
    st.sidebar.title("🛠️ COMMANDS")
    if st.sidebar.button("TERMINATE SESSION"):
        st.session_state['authenticated'] = False
        st.rerun()

    st.title("📟 SYSTEM STATUS: ONLINE")
    st.subheader(f"Welcome back, Commander Hari.")

    # Live Metrics
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Current Bounty", "$12,450", "+$1,200")
    m2.metric("Servers Hacked", "14", "Active")
    m3.metric("Firewall Level", "MAX", "Secure")
    m4.metric("Threat Level", "0.01%", "Low")

    # Target Management
    st.markdown("---")
    st.markdown("### 🎯 ACTIVE MISSIONS")
    
    df = pd.DataFrame({
        "TARGET": ["Google VRP", "Firebase DB", "Cloud Shell RCE"],
        "PROGRESS": ["85%", "100%", "40%"],
        "PRIORITY": ["HIGH", "CRITICAL", "MEDIUM"],
        "STATUS": ["Intercepting", "Verified", "Scanning"]
    })
    st.table(df)

    # Secret Chat Simulation
    with st.expander("💬 INTERNAL COMMS (Encrypted)"):
        st.text_area("Message Log", value="Aether: Bhai, Google ka bug check kiya?\nHari: Haan, payload ready hai. Shaam ko report submit karenge.")
        st.text_input("Send Message:", placeholder="Type encrypted message...")

    # System Logs
    st.markdown("### 📜 SYSTEM LOGS")
    st.code("""
    [INFO] 12:45:01 - Proxy connection established via Tokyo.
    [WARN] 12:46:15 - Port 443 scanning detected.
    [SUCCESS] 12:48:22 - Admin_Hari authenticated from Secure Node.
    """, language='bash')

st.markdown("<br><br><center><p style='color:#333; font-size:10px;'>SECURED BY LTPRO INDIA | ENCRYPTION: AES-256</p></center>", unsafe_allow_html=True)
