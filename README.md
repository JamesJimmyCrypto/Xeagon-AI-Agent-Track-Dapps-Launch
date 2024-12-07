# Xeagon: Your All-in-One Web3 Analytics and AI Agent Platform

[![Xeagon Logo](https://github.com/yuvaraj-06/Nonagon/blob/main/logo.png?raw=true)](https://github.com/yuvaraj-06/Nonagon/blob/main/logo.png?raw=true)  
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)
 

---

## 🚀 How to Run the Xeagon Application

### Prerequisites
1. Ensure you have Python 3.7 installed.
2. Set up a virtual environment to manage dependencies.

```bash
python3 -m venv xeagon-env
source xeagon-env/bin/activate
```

### Steps to Run
1. **Clone the Repository**:  
   ```bash
   git clone https://github.com/yuvaraj-06/Xeagon.git
   cd Xeagon
   ```

2. **Install Dependencies**:  
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Environment Variables**:  
   Create a `.env` file in the root directory and add your API keys:  
   ```env
   OPENAI_API_KEY=your_openai_api_key
   GOOGLE_API_KEY=your_google_api_key
   MONGODB_URI=your_mongodb_connection_string
   RAPID_API_KEY=your_rapidapi_key
   ```

4. **Run the Backend Server**:  
   ```bash
   cd api
   uvicorn main:app --reload --port 8080
   ```

5. **Access the API Documentation**:  
   Visit [http://localhost:8080/docs](http://localhost:8080/docs) to explore the available API endpoints.

6. **Run the Frontend Dashboard**:  
   In a new terminal window:  
   ```bash
   cd Dashboard
   npm run dev
   ```

7. **View the Web Application**:  
   Open [http://localhost:8000](http://localhost:8000) in your browser.

8. **Sign Up**:  
   Create an account to explore the platform and its features.

---

## 🧭 Motivation for Xeagon

The blockchain ecosystem generates immense amounts of data across decentralized applications (dApps) and multiple chains. However, these data points are often underutilized, leaving users, developers, and investors struggling to gain actionable insights. **Xeagon** bridges this gap by transforming raw blockchain data into valuable information and analytics, helping stakeholders make informed decisions.

---

## 🌟 Overview of Xeagon

**Xeagon** is a multi-functional analytics dashboard powered by AI-driven agents. It serves as a platform for:  
1. **Analyzing Blockchain Data**: Retrieve and interpret cross-chain data insights using Covalent APIs.  
2. **Providing User Recommendations**: Identify relationships between dApps and suggest new services.  
3. **Empowering Developers**: Offer insights into user behavior for better product design.  
4. **Guiding Investors**: Deliver data-driven recommendations for investments in tokens, NFTs, and dApps.

---

## ⚙️ Features of Xeagon

### AI-Powered Agents
- **Meme Coin Watcher**: Tracks trending meme coins and automates purchases based on criteria.  
- **Social Listener**: Analyzes social media trends (Twitter, Reddit) to identify investment opportunities.  
- **Market Analyzer**: Delivers in-depth market analysis across Ethereum, BSC, Polygon, and Fantom.  
- **Investment Advisor**: Suggests personalized strategies for staking, trading, and portfolio diversification.

### Cross-Chain Analytics
Gain insights into user behavior across dApps, helping users discover complementary projects and enabling investors to assess market trends effectively.

---

## 🛠️ Tech Stack

- **Backend**: FastAPI  
- **Frontend**: Django for web dashboard  
- **Blockchain API**: Covalent API  
- **Database**: MongoDB for session tracking and data storage  
- **AI Models**: OpenAI GPT-4 and Google's Generative AI  
- **Libraries**:  
  - `langchain`: For conversational AI agent development.  
  - `pandas`: For data analysis and mining.

---

## 🔑 Challenges and Solutions

1. **High API Latency**:  
   Pivoted to CSV-based analysis for improved performance and faster insights.  
2. **Limited Data**:  
   Future iterations will onboard individual dApps and currencies using subgraphs to enrich data quality.  
3. **Real-Time Processing**:  
   Leveraged optimized data retrieval techniques to ensure up-to-date analytics.  

---

## 🎯 Getting Started with Xeagon

1. **Sign Up**: Create a new account.  
2. **Activate Agents**: Configure and enable AI agents for your preferred use cases.  
3. **Connect Wallet**: Link your blockchain wallet to access trading and staking features.  
4. **Explore Insights**: Use the dashboard to analyze market trends, discover dApps, and automate strategies.

---

## 🌐 Platform Highlights

### Dashboard Features
- **Agent Management**: View and control AI agents.  
- **Session Insights**: Track interactions and access history.  

### Supported Blockchains
- Ethereum  
- Binance Smart Chain (BSC)  
- Polygon  
- Fantom  

---

**Xeagon** simplifies complex blockchain analytics and integrates cutting-edge AI to unlock the full potential of Web3. Experience the future of decentralized finance today!