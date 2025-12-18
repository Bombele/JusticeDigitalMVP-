# Offline-First Engine – ITCAA / FINSIG

## 🇫🇷 Présentation
Ce projet est un **moteur documentaire offline-first** conçu pour garantir la continuité des opérations dans des contextes de coupures électriques et de connectivité instable.  
Chaque poste ou appareil devient un **nœud autonome**, capable de fonctionner hors ligne et de synchroniser ses données dès que la connexion est rétablie.  

### Objectifs
- Continuité documentaire et transactionnelle.
- Traçabilité et auditabilité via journaux d’intégrité.
- Synchronisation différée et résolution de conflits.
- Sécurité institutionnelle (AES-256, signatures).
- Documentation trilingue pour adoption internationale.

---

## 🇪🇸 Presentación
Este proyecto es un **motor documental offline-first** diseñado para garantizar la continuidad de las operaciones en contextos de cortes eléctricos y conectividad inestable.  
Cada dispositivo se convierte en un **nodo autónomo**, capaz de funcionar sin conexión y sincronizar sus datos cuando la red se restablece.  

### Objetivos
- Continuidad documental y transaccional.
- Trazabilidad y auditoría mediante registros de integridad.
- Sincronización diferida y resolución de conflictos.
- Seguridad institucional (AES-256, firmas).
- Documentación trilingüe para adopción internacional.

---

## 🇬🇧 Overview
This project is an **offline-first documentary engine** designed to ensure operational continuity in contexts of power outages and unstable connectivity.  
Each workstation or device becomes an **autonomous node**, able to operate offline and synchronize data once the connection is restored.  

### Goals
- Documentary and transactional continuity.
- Traceability and auditability through integrity logs.
- Deferred synchronization and conflict resolution.
- Institutional security (AES-256, signatures).
- Trilingual documentation for international adoption.

---

## 🏗️ Architecture
- **Client Layer**: Local cache (SQLite/IndexedDB), service worker, persistent queue.
- **Integrity Logs**: Append-only, Merkle trees, institutional signatures.
- **Sync Layer**: Deferred synchronization, conflict resolution, validation.
- **Security**: AES-256 encryption, offline OTP, TLS in transit.
- **Observability**: Local dashboard, exportable logs (CSV/PDF).

---

## 🚀 Getting Started
### Requirements
- Node.js (client layer)
- Python 3.10+ (server layer, FastAPI)
- SQLite / CouchDB
- Docker (optional for deployment)

### Installation
```bash
git clone https://github.com/<your-org>/offline-first.git
cd offline-first