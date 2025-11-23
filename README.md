# 🌍 WanderMind AI - Intelligent Travel Planner

An AI-powered trip planning application that creates personalized travel itineraries using LangGraph, Groq LLM, and multiple integrated APIs.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.51-red)
![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green)
![LangChain](https://img.shields.io/badge/LangChain-Latest-yellow)

## ✨ Features

- **AI-Powered Planning**: Uses Groq's Llama 3.3 70B model with LangGraph for intelligent trip planning
- **Multi-Tool Integration**: 
  - 🌤️ Real-time weather forecasts
  - 📍 Google Places & Tavily search for attractions, restaurants, and activities
  - 💰 Currency conversion
  - 🧮 Budget calculation tools
- **Beautiful UI**: Modern glassmorphism design with animated gradients
- **Trip History**: Automatically saves and displays past trip plans
- **Export Options**: Download trip plans as markdown files
- **Responsive Design**: Works seamlessly on all devices

## 🚀 Demo

![WanderMind AI Demo](demo_screenshot.png)

## 🛠️ Tech Stack

### Backend
- **FastAPI**: High-performance API server
- **LangGraph**: Agentic workflow orchestration
- **LangChain**: LLM integration framework
- **Groq**: Ultra-fast LLM inference

### Frontend
- **Streamlit**: Interactive web interface
- **Custom CSS**: Glassmorphism and gradient animations

### APIs & Services
- OpenWeatherMap API
- Google Places API
- Tavily Search API
- ExchangeRate API

## 📋 Prerequisites

- Python 3.11+
- API Keys for:
  - Groq API
  - OpenWeatherMap
  - Google Places
  - Tavily Search
  - ExchangeRate API

## 🔧 Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/AI_Trip_Planner.git
cd AI_Trip_Planner
```

2. **Create virtual environment**
```bash
python -m venv Trip_planner
source Trip_planner/bin/activate  # On Windows: Trip_planner\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**

Create a `.env` file in the root directory:
```env
GROQ_API_KEY=your_groq_api_key
WEATHER_API_KEY=your_openweathermap_key
GOOGLE_API_KEY=your_google_places_key
TAVILY_API_KEY=your_tavily_key
EXCHANGE_RATE_API_KEY=your_exchangerate_key
```

## 🎯 Usage

1. **Start the backend server**
```bash
python main.py
```
The API will be available at `http://localhost:8000`

2. **Launch the Streamlit UI** (in a new terminal)
```bash
streamlit run app.py
```
The app will open in your browser at `http://localhost:8501`

3. **Plan your trip!**
   - Enter your destination, dates, preferences, and budget
   - Click "Plan Trip"
   - Get a personalized AI-generated itinerary
   - Download or copy your trip plan

## 🏗️ Architecture

```
┌─────────────────┐
│  Streamlit UI   │
│  (Frontend)     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   FastAPI       │
│   (Backend)     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   LangGraph     │
│   Agent         │
└────────┬────────┘
         │
    ┌────┴────┐
    ▼         ▼
┌────────┐ ┌──────────┐
│  LLM   │ │  Tools   │
│ (Groq) │ │ (APIs)   │
└────────┘ └──────────┘
```

## 📁 Project Structure

```
AI_Trip_Planner/
├── agent/
│   └── agentic_workflow.py    # LangGraph agent implementation
├── tools/
│   ├── weather_info_tool.py   # Weather API integration
│   ├── place_search_tool.py   # Places search tools
│   ├── expense_calculator_tool.py
│   └── currency_conversion_tool.py
├── utils/
│   ├── model_loader.py        # LLM configuration
│   ├── weather_info.py
│   ├── place_info_search.py
│   └── currency_convertor.py
├── config/
│   └── config.yaml            # Model configuration
├── main.py                    # FastAPI server
├── app.py                     # Streamlit UI
└── requirements.txt
```

## 🎨 UI Features

- **Animated Gradient Background**: Smooth, flowing color transitions
- **Glassmorphism Design**: Modern frosted glass effect
- **Trip History Sidebar**: View past 5 trip plans
- **Download & Copy**: Export your itinerary easily
- **Responsive Layout**: Beautiful on all screen sizes

## 🔑 Key Components

### Agent Workflow
The LangGraph agent orchestrates multiple tools to:
1. Understand user requirements
2. Search for destinations and attractions
3. Get weather forecasts
4. Calculate budgets and expenses
5. Convert currencies
6. Generate comprehensive itineraries

### Tools
- **Weather Tool**: Real-time weather data and forecasts
- **Place Search**: Google Places + Tavily fallback
- **Calculator**: Budget and expense calculations
- **Currency Converter**: Multi-currency support

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License.

## 👨‍💻 Author

**Your Name**
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)
- GitHub: [@yourusername](https://github.com/yourusername)

## 🙏 Acknowledgments

- Built with [LangChain](https://langchain.com/) and [LangGraph](https://langchain-ai.github.io/langgraph/)
- Powered by [Groq](https://groq.com/) for ultra-fast inference
- UI framework: [Streamlit](https://streamlit.io/)

---

⭐ If you found this project helpful, please give it a star!
