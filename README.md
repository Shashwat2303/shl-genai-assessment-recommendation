# SHL GenAI Assessment Recommendation System

A **GenAI-powered Retrieval-Augmented Generation (RAG)** system that recommends the most relevant
**SHL Individual Test Solutions** from a natural language hiring query, job description text,
or JD URL.

This project was developed as part of SHL’s **GenAI Technical Assessment** and demonstrates
end-to-end AI engineering, including data ingestion, semantic retrieval, evaluation, and deployment.

---

## 🚀 Problem Statement

Hiring managers and recruiters often struggle to identify appropriate assessments using
keyword-based filtering. This approach is time-consuming and fails to capture the true
requirements of a role.

The objective of this system is to:
- Understand hiring intent using GenAI techniques
- Retrieve semantically relevant SHL assessments
- Balance recommendations across **technical (K)** and **behavioral/personality (P)** dimensions
- Evaluate performance using objective ranking metrics

---

## 🧠 Solution Overview

The system uses a **Retrieval-Augmented Generation (RAG)** pipeline that combines
semantic embeddings with structured ranking logic.

