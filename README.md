# 🤖 Trading Agents - Sistema Multi-Agente de Análisis Financiero

Un sistema avanzado de análisis financiero que utiliza múltiples agentes de IA especializados para proporcionar análisis completos y decisiones de inversión informadas. Compatible con **criptomonedas**, **acciones** e **índices**.

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/streamlit-1.28+-red.svg)](https://streamlit.io/)
[![OpenAI](https://img.shields.io/badge/powered%20by-OpenAI-green.svg)](https://openai.com/)

## ✨ Características Principales

### 🧠 **Inteligencia Colectiva Multi-Agente**
- **Analista de Mercado**: Análisis técnico con indicadores profesionales (RSI, MACD, Bollinger Bands)
- **Analista de Noticias**: Procesamiento de noticias financieras y contexto macroeconómico
- **Analista de Redes Sociales**: Sentimiento del mercado en Reddit y plataformas sociales
- **Analista Fundamental**: Estados financieros, métricas de valoración e indicadores de salud empresarial

### 🥊 **Sistema de Debate y Consensus**
- **Investigadores Bull vs Bear**: Debate argumentado entre perspectivas optimistas y pesimistas
- **Gestor de Investigación**: Evalúa debates y sintetiza recomendaciones
- **Equipo de Gestión de Riesgos**: Tres niveles de análisis (Agresivo, Conservador, Neutral)
- **Juez de Riesgos**: Decisión final equilibrada basada en todos los análisis

### 🎯 **Adaptación Inteligente por Activo**
- **Criptomonedas** (BTC-USD, ETH-USD): Tokenomics, adopción blockchain, análisis de red
- **Acciones** (AAPL, TSLA, NVDA): Análisis fundamental completo, competencia, valoración
- **Índices** (SPY, QQQ, VTI): Análisis sectorial, política monetaria, flujos institucionales

### 🧠 **Memoria y Aprendizaje**
- Los agentes aprenden de decisiones pasadas
- Sistema de memoria persistente con ChromaDB
- Mejora continua basada en experiencias previas

## 🚀 Instalación y Configuración

### Prerrequisitos
- Python 3.10+
- Anaconda/Miniconda (recomendado)
- Claves de API: [OpenAI](https://platform.openai.com/) y [Finnhub](https://finnhub.io/)

### 1. Clonar el Repositorio
```bash
git clone https://github.com/tu-usuario/trading-agents.git
cd trading-agents
```

### 2. Crear Entorno Virtual
```bash
conda create -n trading-agents python=3.11
conda activate trading-agents
```

### 3. Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar Variables de Entorno
Crea un archivo `.env` en la raíz del proyecto:
```bash
# .env
OPENAI_API_KEY=tu_clave_openai_aqui
FINNHUB_API_KEY=tu_clave_finnhub_aqui
```

### 5. Ejecutar la Aplicación
```bash
streamlit run app.py
```

La aplicación se abrirá automáticamente en tu navegador en `http://localhost:8501`

## 🎮 Cómo Usar

### Interfaz Web (Streamlit)
1. **Configurar APIs**: Las claves se cargan automáticamente desde `.env`
2. **Seleccionar Activo**: Elige categoría (Crypto, Acciones, Índices) y ticker específico
3. **Configurar Análisis**: 
   - Modo individual o múltiple
   - Fecha de análisis
   - Modelos de LLM (GPT-4, etc.)
4. **Ejecutar Análisis**: Click en "🚀 Analizar Mercado"
5. **Revisar Resultados**: Decisión final + reportes detallados expandibles

### Línea de Comandos (CLI)
```bash
python cli/main.py --ticker BTC-USD --date 2024-01-15
```

## 📊 Ejemplos de Uso

### Análisis de Criptomoneda
```python
# Analiza Bitcoin con enfoque en tokenomics y adopción
ticker = "BTC-USD"
# Agentes activos: Market, News, Social (sin Fundamental)
```

### Análisis de Acción
```python
# Analiza Apple con análisis fundamental completo
ticker = "AAPL"  
# Agentes activos: Market, News, Social, Fundamental
```

### Análisis de Índice
```python
# Analiza S&P 500 con enfoque macro
ticker = "SPY"
# Agentes activos: Market, News (simplificado)
```

## 🏗️ Arquitectura del Sistema

```
📦 tradingagents/
├── 🧠 agents/           # Agentes especializados
│   ├── analysts/        # Analistas de mercado
│   ├── researchers/     # Investigadores bull/bear
│   ├── managers/        # Gestores y jueces
│   └── risk_mgmt/       # Gestión de riesgos
├── 📊 dataflows/        # Conectores de datos
├── 🔄 graph/           # Lógica de flujo entre agentes
└── ⚙️ utils/           # Utilidades y configuración
```

## 🛠️ Personalización

### Modificar Agentes
Los prompts y comportamientos se pueden ajustar en:
- `tradingagents/agents/` - Cada agente tiene su archivo específico
- `tradingagents/default_config.py` - Configuración global

### Agregar Nuevos Indicadores
- Extender `tradingagents/dataflows/stockstats_utils.py`
- Modificar herramientas en `tradingagents/agents/utils/agent_utils.py`

### Cambiar Modelos LLM
```python
config = {
    "llm_provider": "openai",  # o "anthropic", "google"
    "deep_think_llm": "gpt-4",
    "quick_think_llm": "gpt-4-mini"
}
```

## 📚 Documentación Adicional

- [**Flujo de Análisis**](docs/analysis_flow.md) - Cómo funciona el sistema paso a paso
- [**API Reference**](docs/api_reference.md) - Documentación de funciones
- [**Configuración Avanzada**](docs/advanced_config.md) - Personalización profunda

## 🤝 Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

## ⚠️ Disclaimer

Este software es solo para fines educativos y de investigación. **No constituye asesoramiento financiero**. Las decisiones de inversión deben basarse en su propia investigación y análisis. Los creadores no se hacen responsables de pérdidas financieras.

## 🙏 Reconocimientos

- Basado en el framework [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)
- Powered by [OpenAI GPT Models](https://openai.com/)
- Datos financieros de [Finnhub](https://finnhub.io/) y [Yahoo Finance](https://finance.yahoo.com/)

---
**⭐ Si este proyecto te resultó útil, por favor dale una estrella en GitHub!**