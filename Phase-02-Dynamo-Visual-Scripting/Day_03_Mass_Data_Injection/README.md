# BIM Automation Debugging & Fire Rating Classification Pipeline

## Project Overview

Built and debugged an enterprise BIM automation workflow capable of auditing **142 Revit door elements** in under **2 seconds** using Dynamo and Revit parameter automation.

The system dynamically:

- Harvests door elements from Revit
- Reads type-based dimensional data
- Applies conditional classification logic
- Writes automated compliance statuses into custom parameters
- Handles null values, grouped elements, and malformed data safely

---

## Core System Pipeline

```text
[All Elements of Category: Doors]
        │
        ▼
[Element.ElementType]
        │
        ▼
[Element.GetParameterValueByName("Width")]
        │
        ▼
[Defensive Logic Block]
(x == null || x == "" ? 0 : x)
        │
        ▼
[Conditional Logic]
(Width < 3.5 Feet)
        │
        ▼
[List.FilterByBoolMask]
        ├── TRUE  → Standard Door - Pass
        └── FALSE → Oversized - Requires Review
```

---

# Deep Dive: 5 Major Debugging Breakthroughs

## 1. Type vs Instance Parameter Resolution

### Problem
All door widths returned `0` or `null`, causing incorrect blanket classification.

### Root Cause
Door width values were stored at the **Type Layer**, not the **Instance Layer**.

### Solution
Inserted an `Element.ElementType` bridge before parameter extraction to access native blueprint metrics correctly.

---

## 2. Case-Sensitive Parameter Access

### Problem
Using `"width"` caused empty parameter returns.

### Root Cause
Revit parameter lookups are case-sensitive.

### Solution

```designscript
"Width";
```

Used the exact database key with proper capitalization.

---

## 3. Defensive Runtime Architecture

### Problem
Null or empty parameter values crashed comparison logic.

### Root Cause
Math comparisons against null values triggered runtime exceptions.

### Solution

```designscript
x == null || x == "" ? 0 : x;
```

Implemented defensive validation before all numerical operations.

---

## 4. Model Group Modification Restrictions

### Problem
Revit blocked parameter updates with:

> "Changes to groups are allowed only in group edit mode."

### Root Cause
Grouped elements inherit dependencies from master assemblies.

### Solution
Applied programmatic ungrouping operations before parameter mutation.

---

## 5. Conditional Stream Logic Calibration

### Problem
Filtering logic produced blank outputs or bulk overwrite behavior.

### Root Cause
Incorrect logical operators and unmapped output streams bypassed filtering.

### Solution
Reconfigured logic using:

- Less Than (`<`) evaluation
- Verified numeric outputs
- Separate true/false data routing streams

---

# Final Output Schema

| Family & Type | Width | Audited By | Fire Rating Status |
|---|---|---|---|
| Single-Flush: 36" x 84" | 3'-0" | Raghav Karol | Standard Door - Pass |
| Single-Flush: Exterior | 3'-0" | Raghav Karol | Standard Door - Pass |
| Double-Flush: 72" x 84" | 6'-0" | Raghav Karol | Oversized - Requires Review |
| Single-Flush Dbl Acting: 36" x 96" | 3'-0" | Raghav Karol | Standard Door - Pass |

---

# Engineering Accomplishments

## Automated BIM Auditing
- Processed 142 building components simultaneously
- Completed full validation cycle in under 2 seconds

## Dynamic Parameter Injection
- Created custom parameter:
  - `Fire_Rating_Status`
- Wrote automated classifications without damaging historical data

## Resilient Automation Architecture
Built a stable Dynamo workflow capable of handling:

- Corrupt parameters
- Empty fields
- Nested model groups
- Runtime exception conditions

without crashing the host environment.

---

# Technologies Used

- Autodesk Revit
- Dynamo
- DesignScript
- BIM Automation
- Parameter Management
- Visual Programming
- Conditional Logic Systems

---

# Key Takeaways

This project demonstrates:

- Advanced BIM automation debugging
- Enterprise-grade defensive scripting
- Revit database architecture understanding
- Parameter-driven compliance workflows
- Production-safe automation engineering

