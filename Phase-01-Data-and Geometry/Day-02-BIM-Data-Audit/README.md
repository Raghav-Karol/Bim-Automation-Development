# 📊 Day 02: BIM Data Validation & Life-Safety Compliance Audit
**Course Phase:** Phase-01-Data-and-Geometry
**Project Context:** Snowdon Towers Sample Architectural Model
**Status:** Completed & Verified Successfully ✅

---

## 📑 Project Overview & Corporate Scenario
An architectural intern drafted a commercial high-rise building with hundreds of door elements. However, the **Fire Safety Officer** refused to sign off on the building blueprints because the doors completely lacked standard "Fire Rating" codes within the BIM database. Without this critical safety data, the manufacturing factory cannot produce the doors, leaving a multi-million dollar construction project completely stalled.

### 🎯 Objective
Audit the building's door database natively, isolate missing data and compliance errors, engineer a workaround for software-enforced data blocks, and generate a clean, client-ready data validation ledger exported into Microsoft Excel for final compliance sign-off.

---

## 🛠️ Technical Skills & Concepts Mastered Today

### 1. Relational Database Aggregation (Collapsing the Ledger)
* Learned how to manipulate Revit's relational scheduling matrix by toggle-switching **"Itemize every instance"**.
* Utilized sorting parameters based on `Family and Type` to collapse a massive ledger of hundreds of individual doors down to unique manufacturing lines for efficient high-level auditing.

### 2. Data Architecture: Type vs. Instance Parameters
* Mastered the structural difference between **Type Parameters** (global blueprint DNA belonging to the manufacturer's specification) and **Instance Parameters** (local object coordinates and unique placement notes).
* Applied this logic to execute global database edits across the whole skyscraper in single keystrokes rather than modifying individual rows manually.

### 3. Dependency Resolution (Overcoming Model Group Locks)
* Encountered real-world database resistance: Revit threw a critical error (`Changes to groups are allowed only in group edit mode...`) when trying to write instance comments onto doors locked inside repeating modular room groups.
* **The Engineering Workaround:** Developed and deployed a custom native **Project Parameter** (`Audited_By`), mapping it explicitly to the Doors category, and configured its data constraints to **"vary by group instance"**. This cleanly bypassed rigid layout locks without breaking the model's structural groups or contaminating global specification templates.

### 4. Cross-Platform ETL Pipeline (Revit ➡️ Excel)
* Managed data extraction using explicit **Tab-Delimited text formats (`.txt`)** out of the 3D authoring environment.
* Handled advanced spreadsheet importing through Excel's **Text Import Wizard** and re-engineered structured data layouts using **Text-to-Columns** parsing after file migrations.
* Polished raw text data dumps into professional, executive corporate ledgers using styling features like header formatting and **Auto-Fit Column Widths**.

---

## 📊 Final Audited Compliance Matrix Preview

Below is a snapshot of the verified data structure compiled and pushed to the repository:

| Family and Type | Height | Width | Fire Rating | Audited_By |
| :--- | :---: | :---: | :---: | :--- |
| `Door-Curtain-Wall-Double-Storefront` | *\<varies\>* | 6' - 0" | **60 MIN** | Raghav Karol |
| `Door-Curtain-Wall-Single-Storefront` | *\<varies\>* | 3' - 0" | **60 MIN** | Raghav Karol |
| `Door-Passage-Double-Flush: 72" x 84"` | 7' - 0" | 6' - 0" | **90 MIN** | Raghav Karol |
| `Door-Passage-Single-Flush: 36" x 84"` | 7' - 0" | 3' - 0" | **60 MIN** | Raghav Karol |
| `Door-Passage-Single-Flush: 36" x 84" (Cores)` | 7' - 0" | 3' - 0" | **180 MIN** | Raghav Karol |
| `Door-Passage-Single-Flush: 36" x 84" (Exterior)` | 7' - 0" | 3' - 0" | **90 MIN** | Raghav Karol |
| `Door-Passage-Single-Flush: 36" x 84" (Roof)` | 7' - 0" | 3' - 0" | **90 MIN** | Raghav Karol |
| `Door-Passage-Single-Flush: 36" x 96"` | 8' - 0" | 3' - 0" | **60 MIN** | Raghav Karol |
| `Door-Passage-Single-Flush: 36" x 96" (Exterior)` | 8' - 0" | 3' - 0" | **90 MIN** | Raghav Karol |
| `Door-Passage-Single-Flush: 42" x 96" (Exterior)` | 8' - 0" | 3' - 6" | **90 MIN** | Raghav Karol |
| `Door-Opening: 32" x 84"` | 0' - 0" | 0' - 0" | *NR (Air Cutout)* | *Exempt from Rating* |

---

## 📈 Summary of Day 02 Milestones Completed
1. **Morning:** Deep dive into Parameter Hierarchy Theory (Type vs. Instance).
2. **Afternoon:** Built a structural volume-to-cost matrix calculation file (`Wall_Price_Scheduling.xlsx`).
3. **Evening:** Executed the complete Life-Safety Door Quality Audit, implemented structural parameter overrides, and produced final Excel-formatted compliance assets (`Door_Fire_Safety_Audit_Report.xlsx`).

***

*Data validated, verified, and pushed securely to development workspace repository branches.*