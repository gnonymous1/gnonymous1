import os

# Create widgets directory
os.makedirs("widgets", exist_ok=True)

def generate_svg(filename, width, height, title, content_html, status="SYS_STATUS: ONLINE"):
    # Premium Cyber-Obsidian / Holographic Neon Theme
    svg_template = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" fill="none">
  <defs>
    <linearGradient id="cardBg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#050811"/>
      <stop offset="50%" stop-color="#090d1a"/>
      <stop offset="100%" stop-color="#04060c"/>
    </linearGradient>
    <linearGradient id="borderGrad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#00f2fe"/>
      <stop offset="50%" stop-color="#7928ca"/>
      <stop offset="100%" stop-color="#00f5a0"/>
    </linearGradient>
  </defs>
  <style>
    .card {{
      font-family: 'Fira Code', 'Consolas', 'Courier New', Courier, monospace;
      background: url('#cardBg') #070a14;
      background-color: #070a14;
      border: 1.5px solid #00f2fe;
      border-radius: 8px;
      box-sizing: border-box;
      padding: 15px 20px;
      width: {width - 2}px;
      height: {height - 2}px;
      box-shadow: 0 4px 20px rgba(0, 242, 254, 0.08);
    }}
    .header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid #1e293b;
      padding-bottom: 8px;
      margin-bottom: 12px;
      height: 25px;
    }}
    .dots {{
      display: flex;
      gap: 6px;
      align-items: center;
    }}
    .dot {{
      width: 8px;
      height: 8px;
      border-radius: 50%;
      display: inline-block;
    }}
    .dot-red {{ background: #ff4757; }}
    .dot-yellow {{ background: #ffa502; }}
    .dot-green {{ background: #2ed573; }}
    .title {{
      color: #00f2fe;
      font-size: 13px;
      font-weight: bold;
      letter-spacing: 0.8px;
      text-shadow: 0 0 10px rgba(0, 242, 254, 0.3);
    }}
    .status {{
      color: #00f5a0;
      font-size: 10px;
      font-weight: bold;
      letter-spacing: 0.5px;
    }}
    .content {{
      color: #f1f5f9;
      font-size: 12px;
      line-height: 1.6;
    }}
    .key {{ color: #38bdf8; }}
    .val {{ color: #00f5a0; }}
    .comment {{ color: #64748b; font-style: italic; }}
    .bullet {{ color: #a855f7; margin-right: 5px; font-weight: bold; }}
    .highlight {{ color: #f59e0b; }}
    .table-container {{
      width: 100%;
      border-collapse: collapse;
      margin-top: 5px;
    }}
    .table-header {{
      color: #00f2fe;
      border-bottom: 1.5px solid #38bdf8;
      text-align: left;
      font-size: 11px;
      padding: 6px 8px;
      font-weight: 700;
    }}
    .table-cell {{
      padding: 6px 8px;
      border-bottom: 1px solid #1e293b;
      font-size: 11px;
      color: #cbd5e1;
    }}
    .table-cell-bold {{
      color: #00f2fe;
      font-weight: bold;
    }}
  </style>
  <foreignObject x="0" y="0" width="{width}" height="{height}">
    <div xmlns="http://www.w3.org/1999/xhtml" class="card">
      <div class="header">
        <div class="dots">
          <div class="dot dot-red"></div>
          <div class="dot dot-yellow"></div>
          <div class="dot dot-green"></div>
        </div>
        <div class="title">{title}</div>
        <div class="status">{status}</div>
      </div>
      <div class="content">
        {content_html}
      </div>
    </div>
  </foreignObject>
</svg>"""
    
    filepath = os.path.join("widgets", filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(svg_template)
    print(f"Generated {filename}")

# 1. DOSSIER WIDGET
dossier_content = """
<div style="margin-top: 5px;">
  <span class="comment"># [root@gnonymous1] // SYSTEM ARCHITECT &amp; CTO DOSSIER</span><br/>
  <span class="key">dossier:</span><br/>
  &#160;&#160;<span class="key">identity:</span> <span class="val">Ghulam Nabi Kalhoro (gnkalhoro)</span><br/>
  &#160;&#160;<span class="key">role:</span> <span class="val">Enterprise Solutions Architect &#183; AI Infrastructure Engineer</span><br/>
  &#160;&#160;<span class="key">core_competencies:</span><br/>
  &#160;&#160;&#160;&#160;<span class="bullet">&#9658;</span> <span class="key">Universal AI Gateways:</span> <span class="val">Multi-model routing, token failover, 189+ providers, vibe coding mesh</span><br/>
  &#160;&#160;&#160;&#160;<span class="bullet">&#9658;</span> <span class="key">Kernel Enforcement:</span> <span class="val">eBPF / XDP low-level traffic inspection &amp; prompt injection firewalls</span><br/>
  &#160;&#160;&#160;&#160;<span class="bullet">&#9658;</span> <span class="key">Agentic Ecosystems:</span> <span class="val">Stateful multi-agent DAGs, cognitive wireless defense, autonomous pentesting</span><br/>
  &#160;&#160;&#160;&#160;<span class="bullet">&#9658;</span> <span class="key">Scalable B2G / Enterprise:</span> <span class="val">High-throughput distributed microservices, SHA-256 ledgers, ERP systems</span>
</div>
"""
generate_svg("widget_dossier.svg", 850, 245, "[ 01 // EXECUTIVE DOSSIER ]", dossier_content, "DECRYPT: SUCCESS")

# 3. TECHNICAL MATRIX WIDGETS (Grid widgets: 410px width, 270px height)

# 3.1 Languages
lang_content = """
<div style="margin-top: 5px;">
  <span class="comment"># Core Engineering Stack</span><br/>
  <span class="key">languages:</span><br/>
  &#160;&#160;<span class="key">systems_low_level:</span><br/>
  &#160;&#160;&#160;&#160;<span class="bullet">&#8227;</span> <span class="val">C / C++ (eBPF, XDP, Linux Kernel)</span><br/>
  &#160;&#160;&#160;&#160;<span class="bullet">&#8227;</span> <span class="val">Go (High-Concurrency Daemons, CLI)</span><br/>
  &#160;&#160;&#160;&#160;<span class="bullet">&#8227;</span> <span class="val">Rust, Assembly (x86/ARM)</span><br/>
  &#160;&#160;<span class="key">ai_and_backend:</span><br/>
  &#160;&#160;&#160;&#160;<span class="bullet">&#8227;</span> <span class="val">Python 3.11+ (FastAPI, PyTorch, LangGraph)</span><br/>
  &#160;&#160;&#160;&#160;<span class="bullet">&#8227;</span> <span class="val">TypeScript / Next.js 14/15, TailwindCSS</span><br/>
  &#160;&#160;<span class="key">databases:</span><br/>
  &#160;&#160;&#160;&#160;<span class="bullet">&#8227;</span> <span class="val">PostgreSQL (pgvector), Redis, MinIO</span>
</div>
"""
generate_svg("widget_skills_languages.svg", 410, 270, "[ LANGUAGES &amp; STACK ]", lang_content, "ENV: OPTIMIZED")

# 3.2 AI & Cognitive
ai_content = """
<div style="margin-top: 5px;">
  <span class="comment">// Cognitive AI &amp; Neural Orchestration</span><br/>
  <span class="key">{{</span><br/>
  &#160;&#160;<span class="key">"AGENT_MESH"</span>: <span class="val">"Autonomous Multi-Agent Systems"</span>,<br/>
  &#160;&#160;<span class="key">"FRAMEWORKS"</span>: [<br/>
  &#160;&#160;&#160;&#160;<span class="val">"LangGraph"</span>, <span class="val">"CrewAI"</span>, <span class="val">"LlamaIndex"</span>,<br/>
  &#160;&#160;&#160;&#160;<span class="val">"Pipecat WebRTC"</span>, <span class="val">"LiveKit Clone Bots"</span><br/>
  &#160;&#160;],<br/>
  &#160;&#160;<span class="key">"ROUTING_GATEWAYS"</span>: [<br/>
  &#160;&#160;&#160;&#160;<span class="val">"AIPI (189 Providers)"</span>, <span class="val">"Smart Token Failover"</span><br/>
  &#160;&#160;],<br/>
  &#160;&#160;<span class="key">"VECTOR_GROUNDING"</span>: [<br/>
  &#160;&#160;&#160;&#160;<span class="val">"pgvector HNSW"</span>, <span class="val">"ChromaDB"</span>, <span class="val">"Qdrant"</span><br/>
  &#160;&#160;]<br/>
  <span class="key">}}</span>
</div>
"""
generate_svg("widget_skills_ai.svg", 410, 270, "[ COGNITIVE AI &amp; MESH ]", ai_content, "AGENT: ACTIVE")

# 3.3 Data Science & ML
data_content = """
<div style="margin-top: 5px;">
  <span class="key">class</span> <span class="val">DataScienceEngine</span>:<br/>
  &#160;&#160;<span class="key">def</span> <span class="val">__init__</span>(self):<br/>
  &#160;&#160;&#160;&#160;self.<span class="key">feature_pipeline</span> = <span class="val">"Realtime Streaming"</span><br/>
  &#160;&#160;&#160;&#160;self.<span class="key">ml_modules</span> = [<br/>
  &#160;&#160;&#160;&#160;&#160;&#160;<span class="val">"PyTorch Neural Nets"</span>,<br/>
  &#160;&#160;&#160;&#160;&#160;&#160;<span class="val">"Sentence-Transformers"</span>,<br/>
  &#160;&#160;&#160;&#160;&#160;&#160;<span class="val">"Cohere Neural Rerankers"</span><br/>
  &#160;&#160;&#160;&#160;]<br/>
  &#160;&#160;&#160;&#160;self.<span class="key">vision_engine</span> = <span class="val">"OpenCV RTSP Detection"</span><br/>
  &#160;&#160;&#160;&#160;self.<span class="key">audio_speech</span> = <span class="val">"Whisper ASR + Deepgram"</span>
</div>
"""
generate_svg("widget_skills_data.svg", 410, 270, "[ DATA SCIENCE &amp; ML ]", data_content, "KERN: LOADED")

# 3.4 Web & Microservices
web_content = """
<div style="margin-top: 5px;">
  <span class="comment"># Distributed Real-Time Architecture</span><br/>
  <span class="key">runtime_topology:</span><br/>
  &#160;&#160;<span class="key">gateway:</span> <span class="val">FastAPI (Async Contracts, OpenAPI)</span><br/>
  &#160;&#160;<span class="key">frontend:</span> <span class="val">Next.js 14/15 App Router + Framer</span><br/>
  &#160;&#160;<span class="key">streaming:</span> <span class="val">WebSockets (WSS), WebRTC SFU</span><br/>
  &#160;&#160;<span class="key">telemetry:</span> <span class="val">Prometheus, Grafana, OpenTelemetry</span><br/>
  &#160;&#160;<span class="key">job_queues:</span> <span class="val">Redis Cluster, Celery Worker Mesh</span><br/>
  &#160;&#160;<span class="key">resilience:</span> <span class="val">Circuit Breaker &amp; Adaptive Backoff</span>
</div>
"""
generate_svg("widget_skills_web.svg", 410, 270, "[ REALTIME WEB &amp; API ]", web_content, "PORT: READY")

# 3.5 OS & Cloud
os_content = """
<div style="margin-top: 5px;">
  <span class="key">[OPERATING_SYSTEMS]</span><br/>
  <span class="key">GNU_Linux</span> = <span class="val">Debian, Ubuntu, Kali Linux, eBPF</span><br/>
  <span class="key">Containers</span> = <span class="val">Docker, Docker Compose, Podman</span><br/>
  <br/>
  <span class="key">[CLOUD_INFRASTRUCTURE]</span><br/>
  <span class="key">Cloud_Platforms</span> = <span class="val">GCP (Vertex AI), AWS, Azure</span><br/>
  <span class="key">Edge_WAF</span> = <span class="val">Cloudflare Zero-Trust, CDN Workers</span><br/>
  <span class="key">Load_Balancers</span> = <span class="val">Nginx, HAProxy, Envoy Mesh</span>
</div>
"""
generate_svg("widget_skills_os.svg", 410, 270, "[ OS &amp; CLOUD PLATFORMS ]", os_content, "NODE: ONLINE")

# 3.6 Kernel & Security
sec_content = """
<div style="margin-top: 5px;">
  <span class="comment">/* Sovereign Security &amp; Kernel Filters */</span><br/>
  <span class="key">.security-matrix</span> {{<br/>
  &#160;&#160;<span class="key">packet-enforcement:</span> <span class="val">eBPF filters, XDP hardware bypass;</span><br/>
  &#160;&#160;<span class="key">zero-trust:</span> <span class="val">mTLS, WireGuard, Tailscale mesh;</span><br/>
  &#160;&#160;<span class="key">offensive-ops:</span> <span class="val">Penetration testing, AST command guard;</span><br/>
  &#160;&#160;<span class="key">wireless-defense:</span> <span class="val">PMKID, WPS, Handshake analyzers;</span><br/>
  &#160;&#160;<span class="key">llm-shield:</span> <span class="val">Prompt injection &amp; jailbreak firewalls;</span><br/>
  <span class="key">}}</span>
</div>
"""
generate_svg("widget_skills_security.svg", 410, 270, "[ KERNEL &amp; OFFENSIVE SEC ]", sec_content, "SHIELD: ARMED")

# 3.7 Enterprise Architecture
ent_content = """
<div style="margin-top: 5px;">
  <span class="key">class</span> <span class="val">EnterpriseArchitecture</span>:<br/>
  &#160;&#160;<span class="key">def</span> <span class="val">orchestrate</span>(self):<br/>
  &#160;&#160;&#160;&#160;self.<span class="key">erp_systems</span> = [<span class="val">"Oracle NetSuite"</span>, <span class="val">"SAP HANA"</span>]<br/>
  &#160;&#160;&#160;&#160;self.<span class="key">audit_trail</span> = <span class="val">"SHA-256 Immutable Audit Ledger"</span><br/>
  &#160;&#160;&#160;&#160;self.<span class="key">fintech_gateways</span> = [<br/>
  &#160;&#160;&#160;&#160;&#160;&#160;<span class="val">"Stripe Billing"</span>, <span class="val">"Paymob"</span>,<br/>
  &#160;&#160;&#160;&#160;&#160;&#160;<span class="val">"JazzCash"</span>, <span class="val">"Easypaisa Micro-APIs"</span><br/>
  &#160;&#160;&#160;&#160;]<br/>
  &#160;&#160;&#160;&#160;self.<span class="key">b2g_systems</span> = <span class="val">"High-Volume National Portals"</span>
</div>
"""
generate_svg("widget_skills_enterprise.svg", 410, 270, "[ ENTERPRISE INFRA &amp; ERP ]", ent_content, "LEDGER: INTACT")

# 3.8 Agile & Strategic PM
agile_content = """
<div style="margin-top: 5px;">
  <span class="comment">// Strategic Program &amp; Tech Leadership</span><br/>
  <span class="key">{{</span><br/>
  &#160;&#160;<span class="key">"LEADERSHIP_ROLE"</span>: <span class="val">"CTO &amp; Lead Systems Architect"</span>,<br/>
  &#160;&#160;<span class="key">"GOVERNANCE"</span>: [<br/>
  &#160;&#160;&#160;&#160;<span class="val">"Google Certified Project Management"</span>,<br/>
  &#160;&#160;&#160;&#160;<span class="val">"Scrum &amp; SAFe Agile Delivery"</span>, <span class="val">"SDLC / CI-CD"</span><br/>
  &#160;&#160;],<br/>
  &#160;&#160;<span class="key">"INCUBATION_TRACK"</span>: <span class="val">"6 Cohorts (1,500+ Tech Ventures)"</span>,<br/>
  &#160;&#160;<span class="key">"STAKEHOLDER_OPS"</span>: <span class="val">"B2G, Enterprise Boardroom &amp; Devs"</span><br/>
  <span class="key">}}</span>
</div>
"""
generate_svg("widget_skills_agile.svg", 410, 270, "[ AGILE OPERATIONS &amp; PM ]", agile_content, "COMPLIANCE: OK")

# 4. BLUEPRINTS WIDGET (Height 360 to showcase all public and private flagships)
blueprint_content = """
<div style="margin-top: 5px; font-size: 11px;">
  <table class="table-container">
    <tr>
      <th class="table-header" style="width: 26%;">SYSTEM / REPOSITORY</th>
      <th class="table-header" style="width: 46%;">ARCHITECTURE &amp; TECHNOLOGY FOCUS</th>
      <th class="table-header" style="width: 14%;">ACCESS</th>
      <th class="table-header" style="width: 14%;">STATUS</th>
    </tr>
    <tr>
      <td class="table-cell table-cell-bold">AIPI</td>
      <td class="table-cell">Universal AI Gateway &#183; 189 Providers &#183; Smart Token Failover Mesh</td>
      <td class="table-cell" style="color: #00f5a0;">[PUBLIC]</td>
      <td class="table-cell" style="color: #00f5a0;">Active &#9679;</td>
    </tr>
    <tr>
      <td class="table-cell table-cell-bold">sovereign-root-protocol</td>
      <td class="table-cell">eBPF/XDP Kernel Filter (C) &#183; FastAPI &#183; AI Traffic Firewalls</td>
      <td class="table-cell" style="color: #00f5a0;">[PUBLIC]</td>
      <td class="table-cell" style="color: #00f5a0;">Active &#9679;</td>
    </tr>
    <tr>
      <td class="table-cell table-cell-bold">project-valkyrie</td>
      <td class="table-cell">Autonomous AI Wireless Security Agent &#183; Gemini &#183; PMKID/WPS TUI</td>
      <td class="table-cell" style="color: #00f5a0;">[PUBLIC]</td>
      <td class="table-cell" style="color: #00f5a0;">Active &#9679;</td>
    </tr>
    <tr>
      <td class="table-cell table-cell-bold">pentestgpt-web</td>
      <td class="table-cell">LLM-Powered Penetration Testing UI &#183; Interactive Terminal &#183; Kali</td>
      <td class="table-cell" style="color: #00f5a0;">[PUBLIC]</td>
      <td class="table-cell" style="color: #00f5a0;">Active &#9679;</td>
    </tr>
    <tr>
      <td class="table-cell table-cell-bold">Agentic_PoC</td>
      <td class="table-cell">Autonomous Agentic AI &#183; Neuro-Symbolic Dashboard &#183; LiveKit WebRTC</td>
      <td class="table-cell" style="color: #00f5a0;">[PUBLIC]</td>
      <td class="table-cell" style="color: #00f5a0;">Active &#9679;</td>
    </tr>
    <tr>
      <td class="table-cell table-cell-bold">WAIFI / CameraGPT</td>
      <td class="table-cell">WiFi Suite (GTK3) &#183; Serverless AI Visitor Face Detection (Netlify)</td>
      <td class="table-cell" style="color: #00f5a0;">[PUBLIC]</td>
      <td class="table-cell" style="color: #00f5a0;">Active &#9679;</td>
    </tr>
    <tr>
      <td class="table-cell table-cell-bold">AUTOAI / LinkedIn Lab</td>
      <td class="table-cell">Self-Evolving Multi-Agent Workflows &#183; Autonomous Social Engine</td>
      <td class="table-cell" style="color: #00f5a0;">[PUBLIC]</td>
      <td class="table-cell" style="color: #00f5a0;">Active &#9679;</td>
    </tr>
    <tr>
      <td class="table-cell table-cell-bold">Aspiration-Academy / NHMP</td>
      <td class="table-cell">SaaS LangGraph Subjective Prep &#183; National B2G Ticketing &amp; Analytics</td>
      <td class="table-cell" style="color: #f43f5e;">[PRIVATE]</td>
      <td class="table-cell" style="color: #00f2fe;">Secured &#128274;</td>
    </tr>
  </table>
</div>
"""
generate_svg("widget_blueprints_v2.svg", 850, 360, "[ 03 // DEPLOYED SYSTEMS &amp; ARCHITECTURAL BLUEPRINTS ]", blueprint_content, "NODES: VERIFIED")

# 5. CREDENTIALS WIDGET
credentials_content = """
<div style="font-family: monospace; font-size: 11px; max-height: 380px; overflow-y: hidden;">
  <span class="comment">[VERIFIED_ENTERPRISE_CREDENTIALS_AND_CERTIFICATIONS]</span><br/>
  <span class="key">[2026]</span> <span class="val">BUILD_AI_AGENTS_WITH_ENTERPRISE_DATABASES</span> <span class="comment">// Skills: Agentic Frameworks, Vector DBs, GCP</span><br/>
  <span class="key">[2026]</span> <span class="val">INNOVATING_WITH_CLOUD_AI</span> <span class="comment">// Skills: Enterprise Innovation, Cloud Cognitive Infrastructure</span><br/>
  <span class="key">[2026]</span> <span class="val">INFRASTRUCTURE_AND_APP_MODERNIZATION</span> <span class="comment">// Skills: Modernize Infrastructure &amp; Cloud Apps</span><br/>
  <span class="key">[2026]</span> <span class="val">IT_ENABLED_BUSINESS_TRANSFORMATION</span> <span class="comment">// Skills: Digital Strategy, Executive Architecture</span><br/>
  <span class="key">[2026]</span> <span class="val">GEN_AI_APPLICATIONS_DEVELOPMENT</span> <span class="comment">// Skills: Generative AI, LLM System Architecture</span><br/>
  <span class="key">[2026]</span> <span class="val">GEN_AI_AGENTS_ORGANIZATIONAL_TRANS</span> <span class="comment">// Skills: Autonomous Workforce &amp; Tool Planning</span><br/>
  <span class="key">[2026]</span> <span class="val">ENTERPRISE_AGENTS_USE_CASES</span> <span class="comment">// Skills: Enterprise Agent Mesh, GCP Deployments</span><br/>
  <span class="key">[2026]</span> <span class="val">GEMINI_ENTERPRISE_APPLICATION_DEV</span> <span class="comment">// Skills: Multimodal AI &amp; Real-time Streaming APIs</span><br/>
  <span class="key">[2022]</span> <span class="val">PROFESSIONAL_PROJECT_MANAGEMENT</span> <span class="comment">// Skills: Google Certified PM, Agile, Scrum, Governance</span><br/>
  <span class="key">[2022]</span> <span class="val">CYBERSECURITY_PRINCIPLES_HARDENING</span> <span class="comment">// Skills: Zero-Trust, Linux Hardening, Network Sec</span><br/>
  <span class="key">[2022]</span> <span class="val">IT_INFRASTRUCTURE_SUPPORT_FUNDAMENTALS</span> <span class="comment">// Skills: OS, LAN/WAN Networking, Virtualization</span><br/>
  <span class="key">[2019]</span> <span class="val">ENTERPRISE_NETWORKING_ROUTING</span> <span class="comment">// Skills: High-Throughput Switching, Routing Protocols</span><br/>
  <span class="key">[2013]</span> <span class="val">SYSTEMS_CPP_SOFTWARE_ENGINEERING</span> <span class="comment">// Skills: C++ Systems Software &amp; Low-Level Algorithms</span><br/>
  <span class="key">[2011]</span> <span class="val">ADVANCED_PHP_MYSQL_WEB_SYSTEMS</span> <span class="comment">// Skills: Web Engines, RDBMS, Scalable Datastores</span>
</div>
"""
generate_svg("widget_credentials.svg", 850, 410, "[ 05 // SYSTEM SIGNALS &amp; ECOSYSTEM CREDENTIALS ]", credentials_content, "CERTIFICATES: VERIFIED")

print("All widgets regenerated successfully with Cyber-Obsidian & Neon-Cyan theme.")
