# 🤝 Guía de Contribución

¡Gracias por tu interés en contribuir a Trading Agents! Este documento te ayudará a empezar.

## 🚀 Cómo Contribuir

### 1. Fork y Clone
```bash
# Fork el repositorio en GitHub, luego:
git clone https://github.com/tu-usuario/trading-agents.git
cd trading-agents
```

### 2. Configurar Entorno de Desarrollo
```bash
conda create -n trading-agents-dev python=3.11
conda activate trading-agents-dev
pip install -r requirements.txt
```

### 3. Crear Rama para tu Feature
```bash
git checkout -b feature/mi-nueva-caracteristica
```

## 📋 Tipos de Contribuciones

### 🐛 **Reportar Bugs**
- Usa las [GitHub Issues](https://github.com/tu-usuario/trading-agents/issues)
- Incluye pasos para reproducir el bug
- Especifica tu sistema operativo y versión de Python

### ✨ **Proponer Features**
- Describe el problema que resuelve
- Explica la solución propuesta
- Considera el impacto en la experiencia del usuario

### 🔧 **Mejoras de Código**
- **Nuevos Agentes**: Crear agentes especializados adicionales
- **Conectores de Datos**: Integrar nuevas fuentes financieras
- **Indicadores Técnicos**: Agregar nuevos indicadores de análisis
- **Optimizaciones**: Mejorar rendimiento y eficiencia

## 🎯 Áreas de Interés

### Agentes Nuevos
- Analista de Opciones
- Analista de Commodities  
- Analista de Forex
- Analista de Eventos Corporativos

### Fuentes de Datos
- Alpha Vantage
- IEX Cloud
- Quandl
- Bloomberg API (si disponible)

### Indicadores Técnicos
- Ichimoku Cloud
- Williams %R
- Commodity Channel Index
- Stochastic Oscillator

## 📝 Estándares de Código

### Estilo
```python
# Usar docstrings descriptivos
def analyze_market(ticker: str, date: str) -> dict:
    """
    Analiza el mercado para un ticker específico.
    
    Args:
        ticker: Símbolo del activo (ej. 'BTC-USD')
        date: Fecha en formato 'YYYY-MM-DD'
        
    Returns:
        Diccionario con el análisis completo
    """
    pass
```

### Estructura de Agentes
```python
# tradingagents/agents/analysts/nuevo_agente.py
def create_nuevo_agente(llm, toolkit):
    """Crea un nuevo agente analista."""
    
    system_message = (
        "IMPORTANTE: Responde SIEMPRE en español. "
        "Eres un especialista en..."
    )
    
    # Resto de la implementación
```

### Testing
```python
# tests/test_nuevo_agente.py
def test_nuevo_agente_basic():
    """Prueba básica del nuevo agente."""
    # Implementar test
    pass
```

## 🔄 Proceso de Pull Request

### 1. Antes de Enviar
- [ ] El código funciona localmente
- [ ] Se agregaron tests si es necesario
- [ ] Se actualizó documentación relevante
- [ ] El código sigue los estándares del proyecto

### 2. Descripción del PR
```markdown
## 📝 Descripción
Breve descripción de los cambios.

## 🔧 Tipo de Cambio
- [ ] Bug fix
- [ ] Nueva característica
- [ ] Mejora de rendimiento
- [ ] Documentación

## ✅ Checklist
- [ ] Tests pasan
- [ ] Documentación actualizada
- [ ] Código revisado
```

### 3. Revisión
- Responde a comentarios constructivamente
- Realiza cambios solicitados
- Mantén el PR actualizado con main

## 🛠️ Desarrollo Local

### Ejecutar Tests
```bash
pytest tests/
```

### Linting
```bash
black tradingagents/
flake8 tradingagents/
```

### Ejecutar con Debug
```bash
streamlit run app.py --logger.level=debug
```

## 📞 Obtener Ayuda

- 💬 **Discussions**: Para preguntas generales
- 🐛 **Issues**: Para bugs y features
- 📧 **Email**: Para asuntos privados

## 🎉 Reconocimiento

Los contributors serán reconocidos en:
- README principal
- Sección de reconocimientos
- Release notes cuando aplique

¡Gracias por hacer que Trading Agents sea mejor! 🚀