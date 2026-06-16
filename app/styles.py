STYLE = '''
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=JetBrains+Mono:wght@300;400;500&display=swap');

/* ── Root ── */
:root {
    --bg:           #05050d;
    --surface:      #0d0d1a;
    --surface-2:    #141423;
    --surface-3:    #1c1c30;
    --border:       #1e1e35;
    --border-hover: #3a3a6a;
    --accent:       #6d28d9;
    --accent-mid:   #8b5cf6;
    --accent-glow:  #a78bfa;
    --accent-2:     #0891b2;
    --accent-2-bright: #22d3ee;
    --text:         #f0f0fa;
    --text-dim:     #9090c0;
    --text-muted:   #5c5c8a;
    --success:      #10b981;
    --warning:      #f59e0b;
    --danger:       #ef4444;
}

/* ── Global Reset ── */
html, body, [class*="css"] {
    font-family: 'JetBrains Mono', monospace;
    background-color: var(--bg) !important;
    color: var(--text) !important;
}

.stApp {
    background: var(--bg) !important;
}

/* Subtle grid overlay */
.stApp::before {
    content: '';
    position: fixed;
    inset: 0;
    background-image:
        linear-gradient(rgba(109, 40, 217, 0.025) 1px, transparent 1px),
        linear-gradient(90deg, rgba(109, 40, 217, 0.025) 1px, transparent 1px);
    background-size: 44px 44px;
    pointer-events: none;
    z-index: 0;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: var(--surface) !important;
    border-right: 1px solid var(--border) !important;
}

[data-testid="stSidebar"] * {
    color: var(--text) !important;
}

/* ── Headings ── */
h1, h2, h3, h4, h5, h6 {
    font-family: 'Syne', sans-serif !important;
    color: var(--text) !important;
    letter-spacing: -0.02em;
}

/* ── Hero Title ── */
.hero-title {
    font-family: 'Syne', sans-serif;
    font-size: clamp(2rem, 5vw, 3.5rem);
    font-weight: 800;
    line-height: 1.1;
    margin: 0;
    letter-spacing: -0.03em;
    color: var(--text);
}

/* Shimmer text effect */
.hero-title .glow {
    color: var(--accent-glow);
    text-shadow:
        0 0 40px rgba(167, 139, 250, 0.7),
        0 0 80px rgba(167, 139, 250, 0.25),
        0 0 120px rgba(167, 139, 250, 0.1);
}

.hero-title .cyan {
    color: var(--accent-2-bright);
    text-shadow:
        0 0 40px rgba(34, 211, 238, 0.6),
        0 0 80px rgba(34, 211, 238, 0.2);
}

.hero-sub {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    color: var(--text-muted);
    letter-spacing: 0.22em;
    text-transform: uppercase;
    margin-top: 0.5rem;
}

/* ── Cards ── */
.card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 1.25rem 1.4rem;
    margin-bottom: 1rem;
    position: relative;
    overflow: hidden;
    transition: border-color 0.2s ease;
}

.card:hover {
    border-color: var(--border-hover);
}

/* Glowing top edge line */
.card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 1px;
    background: linear-gradient(90deg,
        transparent 0%,
        var(--accent-glow) 40%,
        var(--accent-2-bright) 70%,
        transparent 100%);
    opacity: 0.5;
}

/* Left accent bar */
.card::after {
    content: '';
    position: absolute;
    top: 0; left: 0;
    width: 2px; height: 100%;
    background: linear-gradient(180deg, var(--accent-glow), var(--accent-2));
    opacity: 0.7;
}

.card-title {
    font-family: 'Syne', sans-serif;
    font-size: 0.65rem;
    font-weight: 700;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: var(--text-muted);
    margin-bottom: 0.85rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.card-content {
    font-size: 0.85rem;
    line-height: 1.75;
    color: var(--text-dim);
}

/* ── Metric Cards ── */
.metric-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 1rem 1.1rem;
    transition: border-color 0.2s ease;
}

.metric-card:hover {
    border-color: var(--border-hover);
}

.metric-label {
    font-size: 0.62rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: var(--text-muted);
    margin-bottom: 0.4rem;
}

.metric-value {
    font-family: 'Syne', sans-serif;
    font-size: 1.75rem;
    font-weight: 700;
    color: var(--accent-glow);
    line-height: 1;
    text-shadow: 0 0 20px rgba(167, 139, 250, 0.4);
}

.metric-value.cyan {
    color: var(--accent-2-bright);
    text-shadow: 0 0 20px rgba(34, 211, 238, 0.35);
}

.metric-value.green {
    color: var(--success);
    text-shadow: 0 0 20px rgba(16, 185, 129, 0.3);
}

.metric-change {
    font-size: 0.65rem;
    color: var(--success);
    margin-top: 0.35rem;
    letter-spacing: 0.04em;
}

/* ── Badges ── */
.badge {
    display: inline-block;
    padding: 0.18rem 0.55rem;
    border-radius: 4px;
    font-size: 0.6rem;
    font-weight: 600;
    letter-spacing: 0.1em;
    text-transform: uppercase;
}

.badge-purple {
    background: rgba(109, 40, 217, 0.2);
    color: var(--accent-glow);
    border: 1px solid rgba(139, 92, 246, 0.28);
}

.badge-cyan {
    background: rgba(8, 145, 178, 0.15);
    color: var(--accent-2-bright);
    border: 1px solid rgba(34, 211, 238, 0.22);
}

.badge-green {
    background: rgba(16, 185, 129, 0.12);
    color: var(--success);
    border: 1px solid rgba(16, 185, 129, 0.22);
}

.badge-warn {
    background: rgba(245, 158, 11, 0.12);
    color: var(--warning);
    border: 1px solid rgba(245, 158, 11, 0.22);
}

/* ── Status Rows ── */
.status-bar {
    display: flex;
    align-items: center;
    gap: 0.7rem;
    padding: 0.55rem 0.9rem;
    background: var(--surface-2);
    border-radius: 7px;
    margin-bottom: 0.4rem;
    border: 1px solid var(--border);
    font-size: 0.78rem;
    color: var(--text-dim);
    transition: border-color 0.2s;
}

.status-bar:hover {
    border-color: var(--border-hover);
}

.status-dot {
    width: 6px;
    height: 6px;
    border-radius: 50%;
    flex-shrink: 0;
}

.dot-active {
    background: var(--accent-glow);
    box-shadow: 0 0 8px rgba(167, 139, 250, 0.9);
    animation: pulse 1.6s ease-in-out infinite;
}

.dot-done    { background: var(--success); box-shadow: 0 0 6px rgba(16,185,129,0.5); }
.dot-pending { background: var(--border); }
.dot-warn    { background: var(--warning); box-shadow: 0 0 6px rgba(245,158,11,0.5); animation: pulse 1.6s ease-in-out infinite; }

@keyframes pulse {
    0%, 100% { opacity: 1; transform: scale(1); }
    50%       { opacity: 0.4; transform: scale(0.85); }
}

/* ── Chat ── */
.chat-container {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 1rem 1.2rem;
    max-height: 400px;
    overflow-y: auto;
    margin-bottom: 0.75rem;
}

.chat-msg {
    margin-bottom: 1rem;
    display: flex;
    flex-direction: column;
    gap: 0.18rem;
}

.chat-label {
    font-size: 0.6rem;
    font-weight: 700;
    letter-spacing: 0.16em;
    text-transform: uppercase;
}

.chat-bubble {
    display: inline-block;
    padding: 0.55rem 0.9rem;
    border-radius: 9px;
    font-size: 0.82rem;
    line-height: 1.6;
    max-width: 88%;
}

.user-label  { color: var(--accent-glow); }
.bot-label   { color: var(--accent-2-bright); }

.user-bubble {
    background: rgba(109, 40, 217, 0.18);
    border: 1px solid rgba(139, 92, 246, 0.24);
    align-self: flex-end;
}

.bot-bubble {
    background: rgba(8, 145, 178, 0.12);
    border: 1px solid rgba(34, 211, 238, 0.2);
    align-self: flex-start;
}

/* ── Inputs ── */
.stTextInput > div > div > input,
.stSelectbox > div > div,
.stTextArea > div > div > textarea {
    background: var(--surface-2) !important;
    border: 1px solid var(--border) !important;
    border-radius: 8px !important;
    color: var(--text) !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.82rem !important;
    transition: border-color 0.2s, box-shadow 0.2s !important;
}

.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
    border-color: var(--accent-mid) !important;
    box-shadow: 0 0 0 3px rgba(109, 40, 217, 0.18) !important;
    outline: none !important;
}

/* ── Buttons ── */
.stButton > button {
    background: linear-gradient(135deg, var(--accent) 0%, #4c1d95 100%) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 8px !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 700 !important;
    font-size: 0.8rem !important;
    letter-spacing: 0.07em !important;
    text-transform: uppercase !important;
    padding: 0.55rem 1.5rem !important;
    transition: all 0.2s ease !important;
    box-shadow: 0 4px 20px rgba(109, 40, 217, 0.3) !important;
}

.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 30px rgba(109, 40, 217, 0.5) !important;
}

.stButton > button:active {
    transform: translateY(0) !important;
}

/* Secondary button */
.stButton > button[kind="secondary"] {
    background: var(--surface-2) !important;
    border: 1px solid var(--border) !important;
    box-shadow: none !important;
}

.stButton > button[kind="secondary"]:hover {
    border-color: var(--border-hover) !important;
    box-shadow: none !important;
}

/* ── Divider ── */
hr {
    border: none !important;
    border-top: 1px solid var(--border) !important;
    margin: 1.5rem 0 !important;
}

/* ── Transcript / Code Box ── */
.transcript-box {
    background: var(--surface-2);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 1.1rem 1.25rem;
    font-size: 0.78rem;
    line-height: 1.85;
    max-height: 300px;
    overflow-y: auto;
    color: var(--text-muted);
    white-space: pre-wrap;
    word-break: break-word;
}

/* ── Streamlit overrides ── */
.stProgress > div > div > div  { background: var(--accent-mid) !important; }
.stSpinner > div               { border-top-color: var(--accent-mid) !important; }
[data-testid="stMarkdownContainer"] p { color: var(--text) !important; }
label { color: var(--text-muted) !important; font-size: 0.78rem !important; letter-spacing: 0.04em !important; }

/* ── Scrollbar ── */
::-webkit-scrollbar       { width: 4px; height: 4px; }
::-webkit-scrollbar-track { background: var(--bg); }
::-webkit-scrollbar-thumb { background: var(--border-hover); border-radius: 2px; }
::-webkit-scrollbar-thumb:hover { background: var(--accent-mid); }
</style>
'''

