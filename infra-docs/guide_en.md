##############################################
# 📖 Detailed Guide – infra-docs/
##############################################

## 1. Objective
The `infra-docs/` folder consolidates all institutional and technical documentation
required to:
- Ensure compliance (audit, certification, governance).
- Guarantee traceability (trilingual bitácoras).
- Provide institutional credibility and prepare for external audits.

----------------------------------------------

## 2. Folder `infra-docs/compliance`
This folder contains normative and compliance documents.

📂 infra-docs/compliance/
- kyc_kyb.md             → KYC/KYB procedures (Know Your Customer / Know Your Business).
- sanctions_list.md      → Normalization of sanctions lists.
- audit_requirements.md  → Institutional audit checklist.
- certification_plan.md  → ISO/IEC or equivalent certification plan.
- governance.md          → Governance rules for documentation and technical processes.

👉 **Best practice**:
- Each file should be trilingual (FR/ES/EN).
- Include legal references, local and international standards.
- Update whenever regulatory changes occur.

----------------------------------------------

## 3. Folder `infra-docs/bitacoras`
This folder contains trilingual logs (bitácoras) for each module.

📂 infra-docs/bitacoras/
- cache.md               → Log for the cache module.
- integrity.md           → Log for the integrity module.
- sync.md                → Log for the sync module.
- security.md            → Log for the security module.
- observability.md       → Log for the observability module.
- infra.md               → Log for technical evolutions (CI/CD, deployment).

----------------------------------------------

## 4. Documentation Workflow
1. **Creation**: each module starts with a minimal compliance file + an empty bitácora.
2. **Update**: add an entry to the bitácora at every commit or evolution.
3. **Auditability**: align bitácoras with compliance files.
4. **Institutionalization**: compliance = normative vision, bitácoras = operational reality.

----------------------------------------------

## 5. Expected Outcome
- `infra-docs/compliance` → Norms and institutional rules.
- `infra-docs/bitacoras` → Living and traceable journals.
- Together → credibility, transparency, and audit readiness.

----------------------------------------------

## 6. Conclusion / Synthesis
The `infra-docs/` folder is the **documentary backbone** of the project.  
- The **compliance** section defines rules, standards, and institutional requirements.  
- The **bitácoras** section records daily reality and technical evolution.  

Together, they ensure **complete traceability**, **international credibility**, and **solid audit preparation**.  
This documentation system transforms each technical module into an **institutional asset** ready for certification and external adoption.

##############################################