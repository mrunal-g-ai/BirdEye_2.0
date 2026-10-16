# BirdEye 2.0 🦅
> **Autonomous Smart City Intelligence, Computer-Vision Surveillance & Civic Operations Platform**

[![React](https://img.shields.io/badge/React-18.3-61DAFB?logo=react&logoColor=black)](https://react.dev/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.5-3178C6?logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
[![Node.js](https://img.shields.io/badge/Node.js-18+-339933?logo=nodedotjs&logoColor=white)](https://nodejs.org/)
[![Vite](https://img.shields.io/badge/Vite-5.0-646CFF?logo=vite&logoColor=white)](https://vitejs.dev/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind-CSS-06B6D4?logo=tailwindcss&logoColor=white)](https://tailwindcss.com/)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)


---

## 🏆 Hackathon Achievement

<div align="center">

### 🥉 3rd Place — GalxeCode '26 Hackathon

**Project: BirdEye 2.0 | Team RUNTIME**

Recognized for building BirdEye, an AI-powered smart-city
intelligence platform designed to improve civic issue reporting,
urban monitoring, and municipal operations.

<br/>

<!-- Replace these paths with your uploaded image filenames -->

<img src="team-photo.jpg"
     width="85%"
     alt="Team RUNTIME at GalxeCode '26 Hackathon"/>



</div>

---

## 📖 Overview

**BirdEye 2.0** bridges the gap between active citizen reporting, municipal operations, and automated perimeter security. Designed around municipal ward boundaries (Pune Municipal Corporation / Kothrud South Ward 12), BirdEye unifies:

1. **Autonomous CCTV Surveillance**: Continuous multi-camera visual stream monitoring, automated loitering tracking, and blacklisted license plate identification with human-in-the-loop review queues.
2. **Citizen Ingestion & Spatial Deduplication**: PostGIS/Haversine clustering algorithms that collapse redundant citizen reports within a 50-meter radius to prevent duplicate crew dispatches.
3. **"Ask BirdEye" AI Copilot**: Powered by Gemini 3.8 Flash and an offline spatial-proximity engine to answer civic queries, prioritize repair backlogs, and detect nearby hazards.
4. **Dynamic Work Order & Route Optimization**: Open Source Routing Machine (OSRM) integration solving the Traveling Salesperson Problem (TSP) for municipal repair crews.
5. **Real-time Atmospheric Telemetry**: Continuous weather, air quality, and rainfall tracking to predict surface waterlogging and asphalt degradation risks.

---

## 🏛️ System Architecture

```text
┌────────────────────────────────────────────────────────────────────────┐
│                              FRONTEND                                  │
│   React 18 + TypeScript + Tailwind CSS + Leaflet GIS + Framer Motion   │
└────────────────────────────────────┬───────────────────────────────────┘
                                     │
                                HTTP / REST
                                     │
┌────────────────────────────────────▼───────────────────────────────────┐
│                        EXPRESS BACKEND PROXY                           │
│  • Secure API Key Management                                           │
│  • Spatial Math (Haversine 50m Deduplication)                          │
│  • Multi-Source Telemetry Aggregation                                  │
└──────────────┬─────────────────────┬────────────────────┬──────────────┘
               │                     │                    │
    ┌──────────▼──────────┐ ┌────────▼─────────┐ ┌────────▼────────┐
    │ Google GenAI SDK    │ │ Municipal APIs   │ │ Routing Engine  │
    │ • Gemini 3.8 Flash  │ │ • data.gov.in    │ │ • Project OSRM  │
    │ • VLM Verification  │ │ • OpenStreetMap  │ │ • Turn-by-Turn  │
    │ • Spatial Copilot   │ │ • Open-Meteo AQI │ │ • TSP Solver    │
    └─────────────────────┘ └──────────────────┘ └─────────────────┘


```
## Project Structure
```text
BirdEye_2.0/
├── .env.example                 # Template for environment credentials
├── index.html                   # Entry point HTML with meta tags
├── package.json                 # Dependencies and execution scripts
├── server.ts                    # Express backend, Gemini proxy & routing
├── tsconfig.json                # TypeScript compiler configuration
├── vite.config.ts               # Vite configuration & dev server proxy
│
└── src/
    ├── App.tsx                  # Master application orchestrator
    ├── main.tsx                 # React DOM mount point
    ├── index.css                # Global stylesheet & Tailwind CSS tokens
    ├── types/                   # Central TypeScript types & interfaces
    │   └── index.ts
    ├── data/                    # Seed telemetry, ward geometries & baseline data
    │   └── seedData.ts
    ├── services/                # Integration layer
    │   ├── ai-civic/            # Gemini image validation service
    │   ├── ai-security/         # Computer vision surveillance processor
    │   ├── data-sources/        # OSRM, OpenStreetMap, Open-Meteo & data.gov.in
    │   ├── directus/            # Reactive state management store
    │   └── orchestration/       # Routing and dispatch orchestrator
    └── components/              # UI Component Modules
        ├── audit/               # Immutable civic audit logs modal
        ├── citizen/             # Report modal, AskBirdEye Copilot, leaderboards
        ├── command/             # Municipal worklists, analytics & routing panels
        ├── common/              # TopBar, LeftNav, PrivacyCenter & Logo
        ├── datasources/         # Active API registry & key health status
        ├── environmental/       # Atmospheric telemetry bar
        ├── map/                 # Leaflet GIS canvas & cluster rendering
        ├── security/            # CCTV feeds, review queues & snapshot modal
        ├── tour/                # Interactive product walkthrough
        └── workorders/          # Work order tracking & crew dispatch modal
```

# Technical Specification: BirdEye 2.0 Platform 🦅
> **Document Version:** `2.4.0`  
> **Status:** `Approved / Production Architecture`  
> **Classification:** `Engineering & Architecture Specification`  
> **Target Runtime:** `Node.js 18+ (Containerized / Cloud Run) & Modern Evergreen Browsers`

---

## 1. Executive Summary & Scope

**BirdEye 2.0** is an enterprise-grade, full-stack smart city operations platform engineered to synthesize civic infrastructure health, computer-vision surveillance streams, and municipal work-order routing into a unified, explainable operational picture.

The system serves two core operational personas:
1. **Citizens**: Anonymous, cryptographically pseudonymized reporting of physical infrastructure anomalies (potholes, water main ruptures, illumination failures, uncollected solid waste) with real-time AI status explanations.
2. **Municipal Command & Surveillance Operators**: Geospatial incident dispatch, CCTV watchtower monitoring with automated anomaly alerts, vehicle blacklist matching, and dynamic route optimization for field repair crews.

---

## 2. System Architecture & Topology

The platform implements a **Hybrid Edge-Proxy Full-Stack Architecture**, isolating all secret credentials and compute-intensive spatial aggregations behind an Express server while delivering a sub-second reactive interface via React 18.

```text
                                 [ USER AGENT ]
                          (Citizen Mobile / Desktop Admin)
                                      │
                                HTTPS / Port 3000
                                      │
                         ┌────────────▼────────────┐
                         │   NGINX REVERSE PROXY   │
                         └────────────┬────────────┘
                                      │
                         ┌────────────▼────────────┐
                         │      server.ts (Node)   │
                         │    Express 4.x Runtime  │
                         └──────┬────────────┬─────┘
                                │            │
                ┌───────────────┴────┐  ┌────┴─────────────────┐
                ▼                    ▼  ▼                      ▼
    ┌──────────────────────┐  ┌──────────────────┐  ┌───────────────────┐
    │  Static SPA Hosting  │  │ Spatial Query &  │  │  External Gateway │
    │  (Vite Middleware    │  │ Deduplication    │  │  (Proxy Handlers) │
    │   in Dev / dist in   │  │ Engine           │  │                   │
    │   Production)        │  │                  │  │                   │
    └──────────────────────┘  └────────┬─────────┘  └─────────┬─────────┘
                                       │                      │
                       ┌───────────────┼──────────────────────┤
                       ▼               ▼                      ▼
            ┌──────────────────┐ ┌───────────┐ ┌──────────────────────────┐
            │ Google GenAI SDK │ │ OSRM v5   │ │ Municipal Data Services  │
            │ Gemini 3.8 Flash │ │ Routing   │ │ • data.gov.in (OGD)      │
            │ Multimodal LLM   │ │ Engine    │ │ • OSM Overpass API       │
            │                  │ │           │ │ • Open-Meteo Weather/AQI │
            └──────────────────┘ └───────────┘ └──────────────────────────┘
```

## 2.1 Technology Stack Matrix

| Tier | Component | Selection | Justification |
| :--- | :--- | :--- | :--- |
| **Client** | UI/View Framework | React 18.3 (TypeScript) | Concurrent mode, strict type contracts, high ecosystem stability |
| **Styling** | Utility CSS | Tailwind CSS 3.4+ | Zero runtime overhead, deterministic design tokens |
| **Mapping** | Geospatial Canvas | Leaflet 1.9 + Leaflet.heat | Lightweight footprint, custom tile layers, non-blocking marker updates |
| **Server** | Backend API | Node.js + Express 4 | Native asynchronous I/O, rapid JSON parsing, unified language stack |
| **Bundling** | Client / Server | Vite 5 (Client) + esbuild (Server) | Sub-second HMR compilation, single CommonJS artifact (`dist/server.cjs`) |
| **AI / VLM** | Vision & Chat | Google GenAI (gemini-3.8-flash) | Structured JSON outputs, low-latency vision reasoning, high context window |
| **Routing** | Path Planning | Project OSRM (v5 Routing API) | Turn-by-turn road geometry, low-latency Travelling Salesperson (TSP) solution |

## 3. Data Schema & Domain Models

All domain entities are defined in strict TypeScript interfaces under `src/types/index.ts`.

### 3.1 Entity-Relationship Overview

```text
[ Tenant ] ──1:N──> [ IssueCluster ] ──1:N──> [ Issue ] ──1:1──> [ WorkOrder ]
   │                                              │                    │
   ├──1:N──> [ SecurityEvent ]                   N:1                  N:1
   │                                              ▼                    ▼
   └──1:1──> [ EnvironmentalSignal ]    [ MunicipalDepartment ]  [ OptimizedRoute ]
```

### 3.2 Core Data Interfaces

**Issue Model**

```typescript
export interface Issue {
  id: string;
  tenant_id: TenantId;
  title: string;
  category: 'pothole' | 'garbage' | 'streetlight' | 'water';
  priority: 'low' | 'medium' | 'high' | 'critical';
  status: 'reported' | 'assigned' | 'in_progress' | 'resolved';
  location: {
    lat: number;
    lng: number;
    address: string;
    ward_id: string;
  };
  cluster_id?: string;
  contributor_count: number;
  reporter_tokens: string[];       // Ephemeral anonymous hashes (e.g., "#A8F2")
  ai_verification: {
    verified: boolean;
    confidence_score: number;      // 0.00 to 1.00
    detected_category: string;
    severity_score: number;        // 1 to 100
    analysis_notes: string;
  };
  photo_url: string;
  resolution_photo_url?: string;
  department_name: string;
  created_at: string;
  updated_at: string;
}
```

**Surveillance Security Event Model**

```typescript
export interface SecurityEvent {
  id: string;
  tenant_id: TenantId;
  camera_id: string;
  camera_name: string;
  event_type: 'loitering' | 'blacklist_plate' | 'perimeter_breach' | 'unattended_baggage';
  severity: 'info' | 'warning' | 'critical';
  status: 'pending_review' | 'confirmed' | 'dismissed' | 'dispatched';
  timestamp: string;
  coordinates: { lat: number; lng: number };
  snapshot_url: string;
  confidence_score: number;
  metadata: {
    vehicle_plate?: string;
    dwell_time_seconds?: number;
    target_bounding_box?: [number, number, number, number]; // [ymin, xmin, ymax, xmax]
  };
}
```

**Dynamic Work Order Model**

```typescript
export interface WorkOrder {
  id: string;
  issue_id: string;
  department_id: string;
  assigned_crew_id: string;
  status: 'dispatched' | 'en_route' | 'on_site' | 'completed';
  scheduled_start: string;
  estimated_duration_minutes: number;
  priority_score: number;           // Multi-factor weighted score (0-100)
}
```

## 4. Mathematical & Spatial Algorithms

### 4.1 Great-Circle Haversine Distance

All geospatial proximity calculations (incident deduplication, nearby radar, crew routing) execute the spherical Haversine formula on spherical coordinates.

Where:
* $\phi$ = latitudes in radians
* $r$ = mean Earth radius

### 4.2 Spatial Deduplication Pipeline

When an issue is reported at coordinate $C_{new}$:

```text
Input: C_new, Category, DeduplicationRadius = 50.0m
  │
  ├── 1. Filter existing active issues where Status != 'resolved' AND Issue.Category == Category
  ├── 2. Calculate d = Haversine(C_new, Issue.Location)
  │
  ├── IF min(d) <= 50.0m:
  │     ├── Match Found: Target Issue ID = Issue_matched
  │     ├── Increment: Issue_matched.contributor_count += 1
  │     ├── Append: Issue_matched.reporter_tokens.push(AnonymousToken)
  │     ├── Re-calculate Cluster Centroid: 
  │     │     Centroid = ((Lat_old * N + Lat_new) / (N+1), (Lng_old * N + Lng_new) / (N+1))
  │     └── Return: { isDuplicate: true, issue: Issue_matched }
  │
  └── ELSE:
        ├── Instantiate new standalone Issue entity
        ├── Initialize new Cluster entity with Radius = 50m
        └── Return: { isDuplicate: false, issue: Issue_new }
```

### 4.3 Multi-Criteria Urgency Scoring (MCUS)

Work order priority is calculated by an objective weighting matrix to eliminate human bias:

| Variable | Weight | Description | Source |
| :--- | :--- | :--- | :--- |
| **Computer-vision hazard** | 35% | Classification scale (1–100) | Gemini Vision VLM |
| **Roadway classification** | 25% | Arterial = 100, Collector = 70, Local = 40 | OpenStreetMap hierarchy |
| **Unresolved dwell time** | 20% | Penalty exponent | Directus timestamp store |
| **Citizen density** | 20% | Exponent scale | Deduplicated report queue |

## 5. AI & Computer-Vision Architecture

### 5.1 Multimodal Visual Validation Pipeline (`/api/civic/verify`)

Citizens submit base64-encoded JPEG image payloads alongside proposed categories.

```text
[ Base64 Photo ] ────> [ Express API Proxy ] ────> [ Google GenAI SDK ]
                                                           │
                                                  gemini-3.8-flash
                                                           │
                             ┌─────────────────────────────▼─────────────────────────────┐
                             │ Response Schema Enforcement:                              │
                             │ {                                                         │
                             │   "verified": boolean,                                    │
                             │   "detected_category": "pothole"|"garbage"|...,           │
                             │   "confidence_score": float (0.00-1.00),                  │
                             │   "severity_score": int (1-100),                          │
                             │   "analysis_notes": string                                │
                             │ }                                                         │
                             └───────────────────────────────────────────────────────────┘
```

**System Evaluation Rules:**
* **Potholes:** Evaluates surface cavitation depth, asphalt binder loss, edge fracture, and road skid hazard.
* **Garbage:** Evaluates solid waste mass, storm drain blockage probability, and organic decay risk.
* **Streetlights:** Evaluates casing damage, exposed wire hazards, and nighttime public illumination blackout index.
* **Water Leaks:** Evaluates pressurized pipeline rupture versus localized puddle, potable water waste rate, and roadway sub-base undermining risk.

### 5.2 City Copilot Spatial Reasoning (`/api/civic/ai-query`)

Provides contextual natural language processing anchored to the user's real-time geographic coordinates.

```typescript
// Prompt Construction Structure
const prompt = `
System: BirdEye 2.0 AI City Copilot (Pune Municipal Corporation).
User Position: Lat ${userCoords.lat}, Lng ${userCoords.lng}
Active Ward Issues:
${nearbyIssuesList.map(i => `- [${i.id}] ${i.title}: ${i.distanceMeters}m away. Category: ${i.category}, Priority: ${i.priority}`).join('
')}

Query: "${userQuery}"

Task: Output strict JSON answering the user's query, highlighting nearby defects, exact meter distances, and the single highest priority work order to inspect.
`;
```

### 5.3 Resilient Edge-Engine Fallback

If the Gemini API key is missing or the external network encounters an HTTP 429/503 timeout, the system executes an immediate, non-blocking fallback to the Internal Spatial Heuristics Engine:
* Computes radial proximity sorting across all active issues in $C_{new}$.
* Generates natural language summaries using deterministic templates.
* Guarantees uptime for critical operations without UI blocking.

## 6. Surveillance & Computer Vision Loop

### 6.1 CCTV Feed Emulation & Tracking Pipeline

The surveillance engine monitors designated critical infrastructure perimeters using 3 primary streams:
* **Camera 01:** Kothrud Main Arterial Corridor (High-speed traffic)
* **Camera 02:** Paud Road Secondary Junction (Commercial hub)
* **Camera 03:** Transit Interchange Hub (Dense pedestrian activity)

### 6.2 Anomaly Detectors

* **Loitering Detection Engine:** Computes pedestrian dwell time within restricted perimeter polygons. Triggers warning at threshold; escalates to critical review later.
* **Automatic License Plate Matching (ALPR):** Scans vehicle registrations against a municipal hotlist (e.g., stolen vehicles, unauthorized commercial dump trucks). Generates instant bounding box overlay with match confidence.
* **Human-in-the-Loop (HITL) Verification:** To prevent automated false arrests or unlawful dispatches, all CV alerts require a Two-Action Operator Confirmation (Dismiss vs. Confirm & Dispatch) before security notifications are logged.

## 7. External Integrations & Telemetry Ingestion

| Service | Protocol / Endpoint | Ingested Telemetry |
| :--- | :--- | :--- |
| **Open Government Data (OGD) Platform India** | REST / JSON (`api.data.gov.in`) | Municipal department lists and ward GIS boundaries |
| **Open-Meteo Environmental Telemetry Engine** | REST / HTTPS (`api.open-meteo.com/v1/forecast`) | Hourly precipitation, ambient temperature, AQI |
| **OpenStreetMap Overpass** | Overpass QL / POST (`overpass-api.de/api/interpreter`) | Public anchor facilities: schools, hospitals, transit |
| **Project OSRM Routing** | REST / JSON (`router.project-osrm.org`) | Distance matrices, turn geometry, TSP route order |

## 8. State Management Architecture

The frontend application uses a Reactive Store Pattern providing:
* **Optimistic State Updates:** UI reflects incident status changes immediately; rolls back on API rejection.
* **Publish-Subscribe Event Bus:** Components subscribe via `directusStore.subscribe(listener)`, triggering renders only when their specific slice of domain state changes.
* **Immutable Audit Logging:** Every action (`ISSUE_CREATED`, `DUPLICATE_CLUSTERED`, `CV_ALERT_CONFIRMED`, `WORK_ORDER_DISPATCHED`) appends an immutable event log to the chronological audit ledger with an ISO-8601 timestamp.

## 9. Security, Privacy & Compliance Specifications

### 9.1 Zero-Knowledge Citizen Tokenization
* Citizens are never prompted for PII (name, phone number, government ID).
* Upon session creation, an ephemeral SHA-256 derived token hash (e.g., `#A8F2`) is generated in local storage.
* All subsequent civic upvotes and reports are attributed exclusively to this token.

### 9.2 API Key Encapsulation (Defense in Depth)
* **Zero Client-Side Secret Exposure:** No API keys are embedded in frontend source code or transmitted to the browser bundle.
* All calls to Gemini, Open Data platforms, and routing infrastructure are negotiated server-side in `server.ts`.

### 9.3 Frame & Sandbox Permissions
Under `metadata.json`, container permissions are locked down:

```json
{
  "name": "BirdEye 2.0",
  "description": "Smart City & Neighborhood Surveillance Platform",
  "requestFramePermissions": [
    "geolocation"
  ],
  "majorCapabilities": [
    "MAJOR_CAPABILITY_SERVER_SIDE_GEMINI_API"
  ]
}
```

## 10. Build, Packaging & Runtime Execution

### 10.1 Build Pipeline Specification
Production builds execute a two-stage compilation:
* **Client Build:** `vite build` bundles the React SPA into static assets in `dist/`.
* **Server Bundle:** `esbuild server.ts --bundle --platform=node --format=cjs --packages=external --sourcemap --outfile=dist/server.cjs`
  * Bypasses Node ESM relative-import restrictions.
  * Outputs a single, cold-start optimized CommonJS server executable.

### 10.2 Process Lifecycle Commands

```bash
# Start development server (Node + tsx + Vite Middleware)
npm run dev

# Run TypeScript static type checking
npm run lint

# Compile production bundle (Client + Server)
npm run build

# Launch production server
npm run start
```

### 10.3 Performance & SLA Targets

| Metric | Target SLA | Implementation Strategy |
| :--- | :--- | :--- |
| **First Contentful Paint (FCP)** | Optimized | Vite chunk splitting & lazy-loaded modal dialogs |
| **Deduplication Latency** | In-memory | Spatial index & single-pass Haversine evaluation |
| **AI Copilot Latency** | Streaming | Gemini 3.8 Flash streaming with immediate edge fallback |
| **OSRM Route Solve (10 stops)** | Fast | TSP matrix query via OSRM public cluster |

## 11. Revision History

| Version | Date | Author | Description of Changes |
| :--- | :--- | :--- | :--- |
| **1.0.0** | 2026-08-15 | Core Team | Initial prototype architecture & mock mapping layer |
| **2.0.0** | 2026-09-01 | Engineering | PostGIS/Haversine deduplication, OSRM routing, and CCTV watchtower |
| **2.4.0** | 2026-09-12 | AI Systems | Integration of Gemini 3.8 Flash, live spatial copilot radar & edge fallback |

# BirdEye_2.0_Galaxecode_Hackathon_Winner
BirdEye is a privacy-first smart-city platform that transforms anonymous citizen reports and real-world data into verified, deduplicated, prioritized civic issues. With AI verification, intelligent routing, geospatial insights, optimized work orders, environmental intelligence, CCTV analytics, and human-reviewed security alerts.

