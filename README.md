# AI-Smart-Photo-Gallery-using-AWS
A fully serverless AI-powered photo gallery using **AWS Free Tier services**.

## **Overview**

This project allows users to:

- Upload images via a web interface.
- Auto-caption images using **Amazon Rekognition**.
- Store images and captions in **AWS S3**.
- Use **Lambda & API Gateway** as the backend.

## **Technologies Used**

| Technology | Purpose |
|------------|---------|
| **AWS S3** | Store uploaded images and generated captions |
| **AWS Lambda (Python)** | Handle backend image processing |
| **Amazon Rekognition** | Detect labels and objects in images |
| **Amazon API Gateway** | Provide REST API interface |
| **HTML, CSS (Inline), JS** | Frontend in a single file |

---

## **Architecture**

Frontend (HTML) ---> API Gateway ---> Lambda ---> S3 + Rekognition

markdown
Copy
Edit

---

## **Setup Instructions**

### **1️⃣ AWS Setup**

- Create S3 buckets:
    - `photo.gallery.upload`
    - `photo.gallery.frontend`
- Create a Lambda function with `lambda_function.py`
- Create API Gateway with resource `/upload` (POST method, Lambda Proxy Integration)
- Deploy the API (Get the **Invoke URL**)

### **2️⃣ Frontend**

- Open `index.html` locally in browser  
- Use:

```bash
python3 -m http.server
or any live server if needed.

Project Structure
bash
Copy
Edit
AI-Smart-Photo-Gallery/
├── index.html          # Frontend (UI + CSS + JS in one file)
├── lambda_function.py  # Backend (Lambda)
├── README.md           # Documentation
Author
Mohammad Aman
