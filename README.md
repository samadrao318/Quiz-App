# 🚀 Quiz of Programming (Streamlit App)

A simple and interactive **Programming Quiz Application** built using **Python + Streamlit**.  
This quiz includes a timer, auto-next logic, score calculation, and a results dashboard with charts.

---

## Made By Rao Samad

## 🎯 Features

### ✅ Multiple-Choice Quiz  
- Har question ke liye 4 options  
- Radio button se selection system  

### ⏳ 10 Seconds Countdown Timer  
- Har question ke liye 10 sec  
- Time end → question auto next  
- "Timed Out" answer automatically save hota hai  

### 🔁 Manual Next Button  
- User "Next" button se bhi next ja sakta hai  

### 📊 Progress Indicator  
- Live progress bar show hoti hai  
- Total questions ka status dikhata hai  

### 📈 Result Summary + Plotly Chart  
- Quiz complete hone ke baad:
  - Score show hota hai  
  - Correct/Wrong answer table  
  - Plotly bar chart (performance visualization)

### 🎉 Restart System  
- Ek click me quiz phir se start ho jata hai  

---

## 🏗️ Tech Stack

- **Python**
- **Streamlit**
- **Pandas**
- **Plotly**

---

## 📂 Project Structure

```
quiz-app/
│
├── app.py          # Main Streamlit application file
└── README.md       # Project documentation
```

---

## ▶️ How to Run

### 1️⃣ Install required libraries
```bash
pip install streamlit pandas plotly
```

### 2️⃣ Run the app
```bash
streamlit run app.py
```

### 3️⃣ Open in browser  
Normally Streamlit ye open karega:
```
http://localhost:8501
```

---

## 🧠 How It Works (Short Overview)

- Quiz start hote hi timer shuru ho jata hai  
- Har question 10 seconds ke andar attempt karna hota hai  
- Time up ho jaye → next question automatically  
- Manual “Next” button se bhi answer save + next hota hai  
- Last question ke baad results screen show hoti hai  
- Score + answer table + performance bar chart  
- Restart button se quiz reset ho jata hai  

---

## ⭐ Future Updates  
Aage chal kar ye add kiye ja sakte hain:

 
- Admin panel for adding questions  
- Login + save user results  
- Category-wise quizzes  


---


