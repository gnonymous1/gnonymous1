import os

# Create widgets directory
os.makedirs("widgets", exist_ok=True)

def generate_svg(filename, width, height, title, content_html, status="SYS_STATUS: ONLINE"):
    svg_template = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" fill="none">
  <style>
    .card {{
      font-family: 'Fira Code', 'Consolas', 'Courier New', Courier, monospace;
      background: #000000;
      border: 1px solid #ff0055;
      border-radius: 6px;
      box-sizing: border-box;
      padding: 15px 20px;
      width: {width - 2}px;
      height: {height - 2}px;
    }}
    .header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid #27272a;
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
    .dot-red {{ background: #ef4444; }}
    .dot-yellow {{ background: #eab308; }}
    .dot-green {{ background: #22c55e; }}
    .title {{
      color: #00f0ff;
      font-size: 13px;
      font-weight: bold;
      letter-spacing: 0.5px;
    }}
    .status {{
      color: #ff0055;
      font-size: 10px;
      font-weight: bold;
    }}
    .content {{
      color: #ffffff;
      font-size: 12px;
      line-height: 1.6;
    }}
    .key {{ color: #00f0ff; }}
    .val {{ color: #00ff66; }}
    .comment {{ color: #71717a; }}
    .bullet {{ color: #ff0055; margin-right: 5px; }}
    .highlight {{ color: #eab308; }}
    .table-container {{
      width: 100%;
      border-collapse: collapse;
      margin-top: 5px;
    }}
    .table-header {{
      color: #00f0ff;
      border-bottom: 1px solid #ff0055;
      text-align: left;
      font-size: 11px;
      padding: 4px 8px;
    }}
    .table-cell {{
      padding: 6px 8px;
      border-bottom: 1px solid #27272a;
      font-size: 11px;
      color: #e4e4e7;
    }}
    .table-cell-bold {{
      color: #00ff66;
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
    
    with open(os.path.join("widgets", filename), "w", encoding="utf-8") as f:
        f.write(svg_template)
    print(f"Generated {filename}")

# 1. DOSSIER WIDGET (increased height to 240)
dossier_content = """
<div style="margin-top: 5px;">
  <span class="comment"># [root@gnonymous1] // DECRYPTED_PROFILE: ACTIVE</span><br/>
  <span class="key">dossier:</span><br/>
  &#160;&#160;<span class="key">role:</span> <span class="val">Enterprise IT Expert &amp; Solutions Architect</span><br/>
  &#160;&#160;<span class="key">operational_specialties:</span><br/>
  &#160;&#160;&#160;&#160;<span class="bullet">-</span> <span class="key">Large-Scale Infrastructure:</span> <span class="val">High-concurrency B2G / Corporate cloud platforms</span><br/>
  &#160;&#160;&#160;&#160;<span class="bullet">-</span> <span class="key">Agentic Frameworks:</span> <span class="val">Multi-model orchestrations, neural routing, LangGraph RAG</span><br/>
  &#160;&#160;&#160;&#160;<span class="bullet">-</span> <span class="key">Low-Level Hardening:</span> <span class="val">Kernel network filters via eBPF/XDP bypass routing</span><br/>
  &#160;&#160;&#160;&#160;<span class="bullet">-</span> <span class="key">Fintech Telemetry:</span> <span class="val">Netsuite/ERP sharded workflows, SHA-256 audit ledgers</span><br/>
  &#160;&#160;&#160;&#160;<span class="bullet">-</span> <span class="key">Incubation Governance:</span> <span class="val">Guided 6 tech cohorts (1,500+ products analyzed)</span>
</div>
"""
generate_svg("widget_dossier.svg", 850, 240, "[ 01 // EXECUTIVE DOSSIER ]", dossier_content, "DECRYPT: SUCCESS")

# 3. TECHNICAL MATRIX WIDGETS (Grid widgets: 410px width, increased height to 270)

# 3.1 Languages
lang_content = """
<div style="margin-top: 5px;">
  <span class="comment"># Core Development Stack</span><br/>
  <span class="key">languages:</span><br/>
  &#160;&#160;<span class="key">low_level:</span><br/>
  &#160;&#160;&#160;&#160;<span class="bullet">-</span> <span class="val">C / C++ (Linux Kernel, eBPF)</span><br/>
  &#160;&#160;&#160;&#160;<span class="bullet">-</span> <span class="val">Go, Rust, Assembly</span><br/>
  &#160;&#160;<span class="key">backend_apis:</span><br/>
  &#160;&#160;&#160;&#160;<span class="bullet">-</span> <span class="val">Python (FastAPI, Streamlit)</span><br/>
  &#160;&#160;&#160;&#160;<span class="bullet">-</span> <span class="val">PHP (OOP, Web Engines)</span><br/>
  &#160;&#160;<span class="key">frontend_db:</span><br/>
  &#160;&#160;&#160;&#160;<span class="bullet">-</span> <span class="val">TypeScript, JS (React, Next.js)</span><br/>
  &#160;&#160;&#160;&#160;<span class="bullet">-</span> <span class="val">SQL, PL-SQL (PostgreSQL, MySQL)</span>
</div>
"""
generate_svg("widget_skills_languages.svg", 410, 270, "[ LANGUAGES &amp; STACK ]", lang_content, "ENV: DEPLOYED")

# 3.2 AI & Cognitive
ai_content = """
<div style="margin-top: 5px;">
  <span class="comment">// Neural Agents &amp; Orchestration</span><br/>
  <span class="key">{{</span><br/>
  &#160;&#160;<span class="key">"AI_AGENT_ENGINEERING"</span>:<br/>
  &#160;&#160;&#160;&#160;<span class="val">"Enterprise Multi-Agent Mesh"</span>,<br/>
  &#160;&#160;<span class="key">"AGENTIC_FRAMEWORKS"</span>: [<br/>
  &#160;&#160;&#160;&#160;<span class="val">"LangGraph Stateful Graphs"</span>,<br/>
  &#160;&#160;&#160;&#160;<span class="val">"CrewAI"</span>, <span class="val">"Pipecat WebRTC Streams"</span><br/>
  &#160;&#160;],<br/>
  &#160;&#160;<span class="key">"MODELS_AND_APIS"</span>: [<br/>
  &#160;&#160;&#160;&#160;<span class="val">"Gemini Live"</span>, <span class="val">"GPT-4o"</span>, <span class="val">"Claude 3.5"</span><br/>
  &#160;&#160;],<br/>
  &#160;&#160;<span class="key">"NEURAL_GROUNDING"</span>: [<br/>
  &#160;&#160;&#160;&#160;<span class="val">"pgvector"</span>, <span class="val">"ChromaDB"</span>, <span class="val">"Transformers"</span><br/>
  &#160;&#160;]<br/>
  <span class="key">}}</span>
</div>
"""
generate_svg("widget_skills_ai.svg", 410, 270, "[ COGNITIVE AI &amp; MESH ]", ai_content, "AGENT: ACTIVE")

# 3.3 Data Science & ML
data_content = """
<div style="margin-top: 5px;">
  <span class="key">class</span> <span class="val">DataScienceCore</span>:<br/>
  &#160;&#160;<span class="key">def</span> <span class="val">__init__</span>(self):<br/>
  &#160;&#160;&#160;&#160;self.<span class="key">pipeline</span> = <span class="val">"Feature Engineering"</span><br/>
  &#160;&#160;&#160;&#160;self.<span class="key">ml_modules</span> = [<br/>
  &#160;&#160;&#160;&#160;&#160;&#160;<span class="val">"PyTorch Neural Nets"</span>,<br/>
  &#160;&#160;&#160;&#160;&#160;&#160;<span class="val">"Sentence-Transformers"</span><br/>
  &#160;&#160;&#160;&#160;]<br/>
  &#160;&#160;&#160;&#160;self.<span class="key">vector_search</span> = <span class="val">"pgvector HNSW"</span><br/>
  &#160;&#160;&#160;&#160;self.<span class="key">re_rankers</span> = <span class="val">"Cohere Rerank"</span><br/>
  &#160;&#160;&#160;&#160;self.<span class="key">vision</span> = <span class="val">"OpenCV RTSP Processing"</span>
</div>
"""
generate_svg("widget_skills_data.svg", 410, 270, "[ DATA SCIENCE &amp; ML ]", data_content, "KERN: LOADED")

# 3.4 Web & Microservices
web_content = """
<div style="margin-top: 5px;">
  <span class="comment"># Real-Time Routing Config</span><br/>
  <span class="key">runtime_components:</span><br/>
  &#160;&#160;<span class="key">api_gateway:</span> <span class="val">FastAPI (Async Contracts)</span><br/>
  &#160;&#160;<span class="key">ui_framework:</span> <span class="val">Next.js 15 App Router</span><br/>
  &#160;&#160;<span class="key">transport:</span> <span class="val">WebRTC, WebSockets (WSS)</span><br/>
  &#160;&#160;<span class="key">meetings_api:</span> <span class="val">Recall.ai Virtualization</span><br/>
  &#160;&#160;<span class="key">webrtc_sfu:</span> <span class="val">LiveKit Server Ingestion</span><br/>
  &#160;&#160;<span class="key">caching:</span> <span class="val">Redis Cluster Job Queues</span><br/>
  &#160;&#160;<span class="key">database:</span> <span class="val">PostgreSQL Sharded RLS</span>
</div>
"""
generate_svg("widget_skills_web.svg", 410, 270, "[ REALTIME WEB &amp; API ]", web_content, "PORT: OPEN")

# 3.5 OS & Cloud
os_content = """
<div style="margin-top: 5px;">
  <span class="key">[OPERATING_SYSTEMS]</span><br/>
  <span class="key">GNU_Linux</span> = <span class="val">Ubuntu, Debian, eBPF Sandbox</span><br/>
  <span class="key">Virtualization</span> = <span class="val">VMware ESXi, WSL2, Docker</span><br/>
  <br/>
  <span class="key">[CLOUD_ORCHESTRATION]</span><br/>
  <span class="key">Platforms</span> = <span class="val">GCP (Vertex AI), Azure</span><br/>
  <span class="key">Edge_Routing</span> = <span class="val">Cloudflare WAF/CDN, Workers</span><br/>
  <span class="key">Reverse_Proxy</span> = <span class="val">Nginx, HAProxy Load Balancer</span>
</div>
"""
generate_svg("widget_skills_os.svg", 410, 270, "[ OS &amp; CLOUD PLATFORMS ]", os_content, "NODE: BOUND")

# 3.6 Kernel & Security
sec_content = """
<div style="margin-top: 5px;">
  <span class="comment">/* Zero-Trust Hardening */</span><br/>
  <span class="key">.security-envelope</span> {{<br/>
  &#160;&#160;<span class="key">low-level-routing:</span> <span class="val">eBPF-filters, XDP-pipes;</span><br/>
  &#160;&#160;<span class="key">tunnel-mesh:</span> <span class="val">Tailscale-API, WireGuard;</span><br/>
  &#160;&#160;<span class="key">encryption:</span> <span class="val">mTLS, Custom CA Trust-Blocks;</span><br/>
  &#160;&#160;<span class="key">pen-testing:</span> <span class="val">Kali Linux, Nmap, Metasploit;</span><br/>
  &#160;&#160;<span class="key">scraping-bot:</span> <span class="val">OSINT target recon systems;</span><br/>
  <span class="key">}}</span>
</div>
"""
generate_svg("widget_skills_security.svg", 410, 270, "[ KERNEL &amp; NET SECURITY ]", sec_content, "SHIELD: ARMED")

# 3.7 Enterprise Billing
ent_content = """
<div style="margin-top: 5px;">
  <span class="key">class</span> <span class="val">EnterpriseLogistics</span>:<br/>
  &#160;&#160;<span class="key">def</span> <span class="val">configure_erp</span>(self):<br/>
  &#160;&#160;&#160;&#160;self.<span class="key">erp</span> = <span class="val">"Oracle NetSuite SuiteScript 2.0"</span><br/>
  &#160;&#160;&#160;&#160;self.<span class="key">accounting</span> = [<span class="val">"QuickBooks"</span>, <span class="val">"Xero API"</span>]<br/>
  &#160;&#160;&#160;&#160;self.<span class="key">tax_saas</span> = [<span class="val">"Drake Tax"</span>, <span class="val">"Lacerte SaaS"</span>]<br/>
  &#160;&#160;&#160;&#160;self.<span class="key">payment_gateways</span> = [<br/>
  &#160;&#160;&#160;&#160;&#160;&#160;<span class="val">"Stripe Billing"</span>, <span class="val">"Paymob"</span>,<br/>
  &#160;&#160;&#160;&#160;&#160;&#160;<span class="val">"JazzCash"</span>, <span class="val">"Easypaisa"</span><br/>
  &#160;&#160;&#160;&#160;]<br/>
</div>
"""
generate_svg("widget_skills_enterprise.svg", 410, 270, "[ ENTERPRISE INFRA &amp; ERP ]", ent_content, "LEDGER: INTACT")

# 3.8 Agile & PM
agile_content = """
<div style="margin-top: 5px;">
  <span class="comment">// Project Lifecycle &amp; Governance</span><br/>
  <span class="key">{{</span><br/>
  &#160;&#160;<span class="key">"IT_MANAGEMENT"</span>: <span class="val">"Risk Mitigation &amp; Logistics"</span>,<br/>
  &#160;&#160;<span class="key">"AGILE_METHODOLOGY"</span>: [<br/>
  &#160;&#160;&#160;&#160;<span class="val">"Scrum Framework"</span>, <span class="val">"Sprint Planning"</span>,<br/>
  &#160;&#160;&#160;&#160;<span class="val">"SAFe Agile"</span>, <span class="val">"PLM"</span>, <span class="val">"SDLC"</span><br/>
  &#160;&#160;],<br/>
  &#160;&#160;<span class="key">"SYSTEMS_AUDITING"</span>: <span class="val">"Compliance Tracking"</span>,<br/>
  &#160;&#160;<span class="key">"COLLABORATION"</span>: <span class="val">"Stakeholder Alignment"</span><br/>
  <span class="key">}}</span>
</div>
"""
generate_svg("widget_skills_agile.svg", 410, 270, "[ AGILE OPERATIONS &amp; PM ]", agile_content, "COMPLIANCE: OK")

# 4. BLUEPRINTS WIDGET (increased height to 260)
blueprint_content = """
<div style="margin-top: 5px; font-size: 11px;">
  <table class="table-container">
    <tr>
      <th class="table-header" style="width: 25%; font-size: 10px;">REPOSITORY / NODE</th>
      <th class="table-header" style="width: 45%; font-size: 10px;">ARCHITECTURE &amp; STACK ROLE</th>
      <th class="table-header" style="width: 15%; font-size: 10px;">VISIBILITY</th>
      <th class="table-header" style="width: 15%; font-size: 10px;">STACK STATUS</th>
    </tr>
    <tr>
      <td class="table-cell table-cell-bold">sovereign-root-protocol</td>
      <td class="table-cell">eBPF/XDP filter (C) &#183; FastAPI (Python) &#183; HAProxy mesh</td>
      <td class="table-cell" style="color: #00ff66;">[PUBLIC]</td>
      <td class="table-cell" style="color: #00ff66;">Active</td>
    </tr>
    <tr>
      <td class="table-cell table-cell-bold">Aspiration-Academy</td>
      <td class="table-cell">Next.js 15 &#183; Python FastAPI &#183; LangGraph subjective AI prep</td>
      <td class="table-cell" style="color: #00ff66;">[PUBLIC]</td>
      <td class="table-cell" style="color: #00ff66;">Active</td>
    </tr>
    <tr>
      <td class="table-cell table-cell-bold">Agentic_PoC (GNONE)</td>
      <td class="table-cell">LiveKit WebRTC clone bot &#183; Recall.ai container &#183; Streamlit</td>
      <td class="table-cell" style="color: #ef4444;">[PRIVATE]</td>
      <td class="table-cell" style="color: #00ff66;">Secured</td>
    </tr>
    <tr>
      <td class="table-cell table-cell-bold">ReconPortal / Valkyrie</td>
      <td class="table-cell">OSINT data extraction crawlers &#183; Network Nmap mapper &#183; Docker</td>
      <td class="table-cell" style="color: #00ff66;">[PUBLIC]</td>
      <td class="table-cell" style="color: #00ff66;">Active</td>
    </tr>
    <tr>
      <td class="table-cell table-cell-bold">CameraGPT / WAIFI</td>
      <td class="table-cell">OpenCV RTSP camera stream (AI detection) &#183; Tailscale VPN</td>
      <td class="table-cell" style="color: #00ff66;">[PUBLIC]</td>
      <td class="table-cell" style="color: #00ff66;">Active</td>
    </tr>
  </table>
</div>
"""
generate_svg("widget_blueprints_v2.svg", 850, 320, "[ 03 // DEPLOYED SYSTEMS &amp; SYSTEM BLUEPRINTS ]", blueprint_content, "NODES: MAP_VERIFIED")

# 5. CREDENTIALS WIDGET (increased height to 410)
credentials_content = """
<div style="font-family: monospace; font-size: 11px; max-height: 380px; overflow-y: hidden;">
  <span class="comment">[SYSTEM_CREDENTIALS_VERIFIED_DECRYPTED]</span><br/>
  <span class="key">[2026-05]</span> <span class="val">BUILD_AI_AGENTS_WITH_ENTERPRISE_DATABASES</span> <span class="comment">// Skills: AI Agents, GCP databases</span><br/>
  <span class="key">[2026-05]</span> <span class="val">INNOVATING_WITH_CLOUD_AI</span> <span class="comment">// Skills: Innovation Management, Artificial Intelligence</span><br/>
  <span class="key">[2026-05]</span> <span class="val">INFRASTRUCTURE_AND_APP_MODERNIZATION</span> <span class="comment">// Skills: Modernize Infrastructure &amp; Applications</span><br/>
  <span class="key">[2026-05]</span> <span class="val">IT_ENABLED_BUSINESS_TRANSFORMATION</span> <span class="comment">// Skills: Digital Transformation, IT Strategy</span><br/>
  <span class="key">[2026-04]</span> <span class="val">GEN_AI_APPLICATIONS_DEVELOPMENT</span> <span class="comment">// Skills: Generative AI, App Dev</span><br/>
  <span class="key">[2026-04]</span> <span class="val">GEN_AI_AGENTS_ORGANIZATIONAL_TRANS</span> <span class="comment">// Skills: Gen AI for Service Professionals</span><br/>
  <span class="key">[2026-04]</span> <span class="val">GEN_AI_LANDSCAPES_NAVIGATION</span> <span class="comment">// Skills: Gen AI Core Concepts</span><br/>
  <span class="key">[2026-02]</span> <span class="val">ENTERPRISE_AGENTS_USE_CASES</span> <span class="comment">// Skills: Enterprise Agents, GCP deployments</span><br/>
  <span class="key">[2026-02]</span> <span class="val">GEMINI_ENTERPRISE_APPLICATION_DEV</span> <span class="comment">// Skills: Gemini Enterprise Applications</span><br/>
  <span class="key">[2022-12]</span> <span class="val">PROFESSIONAL_PROJECT_MANAGEMENT</span> <span class="comment">// Skills: Agile, Project Lifecycle, Scrum</span><br/>
  <span class="key">[2022-10]</span> <span class="val">FOUNDATIONS_OF_PROJECT_MANAGEMENT</span> <span class="comment">// Skills: Project Initiation, Agile Operations</span><br/>
  <span class="key">[2022-06]</span> <span class="val">CYBERSECURITY_PRINCIPLES_HARDENING</span> <span class="comment">// Skills: Cybersecurity, Linux Hardening, Network Sec</span><br/>
  <span class="key">[2022-01]</span> <span class="val">IT_INFRASTRUCTURE_SUPPORT_FUNDAMENTALS</span> <span class="comment">// Skills: Operating Systems, Tech Support, Networking</span><br/>
  <span class="key">[2019-12]</span> <span class="val">ENTERPRISE_NETWORKING_ROUTING</span> <span class="comment">// Skills: Routing, LAN/WAN Switching</span><br/>
  <span class="key">[2013-02]</span> <span class="val">SYSTEMS_CPP_SOFTWARE_ENGINEERING</span> <span class="comment">// Skills: C++ Systems Software &amp; Algorithms</span><br/>
  <span class="key">[2011-09]</span> <span class="val">ADVANCED_PHP_MYSQL_WEB_SYSTEMS</span> <span class="comment">// Skills: PHP OOP Web Engines &amp; Relational Databases</span>
</div>
"""
generate_svg("widget_credentials.svg", 850, 410, "[ 05 // SYSTEM SIGNALS &amp; ECOSYSTEM CREDENTIALS ]", credentials_content, "CERTIFICATES: 16_VERIFIED")

print("All widgets generated successfully.")
