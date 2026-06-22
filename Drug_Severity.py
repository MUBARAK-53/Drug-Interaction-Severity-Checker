import streamlit as st
import ast
import pandas as pd

# ─── Page Config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Drug Interaction Detection System",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─── Custom CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    /* Import font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* Dark gradient background */
    .stApp {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        color: #e0e0e0;
    }

    /* Header area */
    .hero-section {
        text-align: center;
        padding: 2rem 1rem 1.5rem 1rem;
    }
    .hero-title {
        font-size: 2.8rem;
        font-weight: 700;
        background: linear-gradient(90deg, #a78bfa, #60a5fa, #34d399);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.3rem;
    }
    .hero-subtitle {
        font-size: 1rem;
        color: #94a3b8;
        font-weight: 400;
        letter-spacing: 0.05em;
    }

    /* Glass card */
    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 16px;
        padding: 1.5rem 2rem;
        backdrop-filter: blur(12px);
        margin-bottom: 1.2rem;
    }

    /* Section label */
    .section-label {
        font-size: 0.78rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.12em;
        color: #94a3b8;
        margin-bottom: 0.4rem;
    }

    /* Info row inside card */
    .info-value {
        font-size: 0.97rem;
        color: #e2e8f0;
        line-height: 1.7;
    }

    /* Severity badges */
    .badge-major {
        display: inline-block;
        background: linear-gradient(135deg, #7f1d1d, #dc2626);
        color: #fff;
        border-radius: 999px;
        padding: 0.35rem 1.1rem;
        font-weight: 700;
        font-size: 1.05rem;
        letter-spacing: 0.04em;
    }
    .badge-moderate {
        display: inline-block;
        background: linear-gradient(135deg, #78350f, #d97706);
        color: #fff;
        border-radius: 999px;
        padding: 0.35rem 1.1rem;
        font-weight: 700;
        font-size: 1.05rem;
        letter-spacing: 0.04em;
    }
    .badge-minor {
        display: inline-block;
        background: linear-gradient(135deg, #14532d, #16a34a);
        color: #fff;
        border-radius: 999px;
        padding: 0.35rem 1.1rem;
        font-weight: 700;
        font-size: 1.05rem;
        letter-spacing: 0.04em;
    }

    /* Divider */
    .styled-divider {
        border: none;
        border-top: 1px solid rgba(255,255,255,0.1);
        margin: 1rem 0;
    }

    /* Selectbox label override */
    label {
        color: #cbd5e1 !important;
        font-weight: 500 !important;
    }

    /* Button */
    .stButton > button {
        background: linear-gradient(135deg, #7c3aed, #2563eb);
        color: white;
        border: none;
        border-radius: 12px;
        font-weight: 600;
        font-size: 1rem;
        padding: 0.65rem 1.5rem;
        transition: all 0.3s ease;
        letter-spacing: 0.04em;
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, #6d28d9, #1d4ed8);
        transform: translateY(-1px);
        box-shadow: 0 6px 24px rgba(124, 58, 237, 0.45);
    }

    /* No interaction box */
    .no-result-box {
        background: rgba(100, 116, 139, 0.12);
        border: 1px dashed rgba(148, 163, 184, 0.4);
        border-radius: 12px;
        padding: 1.5rem;
        text-align: center;
        color: #94a3b8;
        font-size: 0.95rem;
    }

    /* Stats strip */
    .stat-box {
        background: rgba(255,255,255,0.04);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 12px;
        padding: 0.9rem 1.2rem;
        text-align: center;
    }
    .stat-num {
        font-size: 1.6rem;
        font-weight: 700;
        color: #a78bfa;
    }
    .stat-label {
        font-size: 0.78rem;
        color: #64748b;
        text-transform: uppercase;
        letter-spacing: 0.08em;
    }

    /* Hide Streamlit default branding */
    #MainMenu, footer { visibility: hidden; }
</style>
""", unsafe_allow_html=True)


# ─── Data Loading (cached) ───────────────────────────────────────────────────────
@st.cache_data(show_spinner="Loading drug interaction database…")
def load_data():
    df = pd.read_csv("drug_interactions.csv")
    df["ddi_database"] = df["ddi_database"].apply(ast.literal_eval)
    df = pd.json_normalize(df["ddi_database"])
    return df

data = load_data()

# ─── Hero Section ────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-section">
    <div class="hero-title">🏥 Drug Interaction Detection</div>
    <div class="hero-subtitle">AI-Powered Healthcare Assistant · Identify risks before they happen</div>
</div>
""", unsafe_allow_html=True)

# ─── Stats Strip ────────────────────────────────────────────────────────────────
total_drugs = len(set(data["drug_a"]) | set(data["drug_b"]))
total_interactions = len(data)
major_count = (data["severity"] == "Major").sum()
moderate_count = (data["severity"] == "Moderate").sum()
minor_count = (data["severity"] == "Minor").sum()

c1, c2, c3, c4, c5 = st.columns(5)
for col, num, label in zip(
    [c1, c2, c3, c4, c5],
    [total_drugs, total_interactions, major_count, moderate_count, minor_count],
    ["Drugs", "Interactions", "🔴 Major", "🟠 Moderate", "🟢 Minor"],
):
    col.markdown(f"""
    <div class="stat-box">
        <div class="stat-num">{num}</div>
        <div class="stat-label">{label}</div>
    </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ─── Drug Selection ──────────────────────────────────────────────────────────────
drugs = sorted(set(data["drug_a"]) | set(data["drug_b"]))

col_a, col_b = st.columns(2, gap="large")
with col_a:
    drug_a = st.selectbox("💊 Select Drug A", drugs, key="drug_a")
with col_b:
    drug_b = st.selectbox("💊 Select Drug B", drugs, key="drug_b")

st.markdown("<br>", unsafe_allow_html=True)
check = st.button("🔍 Check Interaction", use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

# ─── Result Logic ────────────────────────────────────────────────────────────────
SEVERITY_BADGE = {
    "Major":    '<span class="badge-major">🔴 Major</span>',
    "Moderate": '<span class="badge-moderate">🟠 Moderate</span>',
    "Minor":    '<span class="badge-minor">🟢 Minor</span>',
}

if check:
    # Validate selection
    if drug_a == drug_b:
        st.warning("⚠️ Please select two **different** drugs to check for an interaction.")
    else:
        mask = (
            ((data["drug_a"] == drug_a) & (data["drug_b"] == drug_b)) |
            ((data["drug_a"] == drug_b) & (data["drug_b"] == drug_a))
        )
        result = data[mask]

        if result.empty:
            
            st.markdown(f"""
            <div class="no-result-box">
                <b>No known interaction</b> found between <b>{drug_a}</b> and <b>{drug_b}</b>.<br>
                <span style="color:#64748b; font-size:0.85rem;">
                    This does not guarantee the combination is safe. Always consult a healthcare professional.
                </span>
            </div>
            """, unsafe_allow_html=True)
        else:
            row = result.iloc[0]
            severity = row["severity"]
            badge_html = SEVERITY_BADGE.get(severity, f"<b>{severity}</b>")

            # ── Severity Header ──
            st.markdown(f"""
            <div class="glass-card">
                <div class="section-label">Severity Level</div>
                {badge_html}
                <hr class="styled-divider">
                <div class="section-label">Drugs Involved</div>
                <div class="info-value">
                    <b style="color:#a78bfa">{drug_a}</b>
                    &nbsp;↔&nbsp;
                    <b style="color:#60a5fa">{drug_b}</b>
                </div>
            </div>
            """, unsafe_allow_html=True)

            # ── Mechanism & Effect ──
            col1, col2 = st.columns(2, gap="medium")
            with col1:
                st.markdown(f"""
                <div class="glass-card" style="height:100%">
                    <div class="section-label">⚙️ Mechanism</div>
                    <div class="info-value">{row['mechanism']}</div>
                </div>""", unsafe_allow_html=True)
            with col2:
                st.markdown(f"""
                <div class="glass-card" style="height:100%">
                    <div class="section-label">⚠️ Clinical Effect</div>
                    <div class="info-value">{row['clinical_effect']}</div>
                </div>""", unsafe_allow_html=True)

            # ── Management & Alternative ──
            col3, col4 = st.columns(2, gap="medium")
            with col3:
                st.markdown(f"""
                <div class="glass-card" style="height:100%">
                    <div class="section-label">🩺 Clinical Management</div>
                    <div class="info-value">{row['clinical_management']}</div>
                </div>""", unsafe_allow_html=True)
            with col4:
                safer = row["safer_alternative"] if pd.notna(row["safer_alternative"]) else "None specified"
                st.markdown(f"""
                <div class="glass-card" style="height:100%">
                    <div class="section-label">✅ Safer Alternative</div>
                    <div class="info-value">{safer}</div>
                </div>""", unsafe_allow_html=True)

            # ── Reference ──
            if pd.notna(row.get("reference", None)):
                st.markdown(f"""
                <div class="glass-card">
                    <div class="section-label">📚 Reference</div>
                    <div class="info-value" style="font-size:0.88rem; color:#64748b;">{row['reference']}</div>
                </div>""", unsafe_allow_html=True)
