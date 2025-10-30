---
name: streamlit
description: Use this skill when working with Streamlit - a Python framework for building interactive data apps and dashboards
---

# Streamlit Skill

Comprehensive assistance with Streamlit development, generated from official documentation. Streamlit is a powerful open-source Python framework that allows data scientists and AI/ML engineers to build interactive apps with only a few lines of code.

## When to Use This Skill

This skill should be triggered when:
- **Building data dashboards or web apps** with Python
- **Creating interactive visualizations** for data science projects
- **Displaying dataframes, charts, or metrics** in a web interface
- **Adding user input widgets** (sliders, buttons, text inputs, file uploads)
- **Deploying Python data apps** without writing HTML/CSS/JavaScript
- **Prototyping ML/AI demos** or data analysis tools quickly
- **Implementing real-time data updates** or streaming content
- **Setting up user authentication** or secrets management for apps
- **Configuring theming, custom fonts, or multi-page apps**
- **Troubleshooting Streamlit-specific issues** (caching, session state, widget behavior)

## Quick Reference

### 1. Hello World - Your First Streamlit App

The simplest possible Streamlit app:

```python
import streamlit as st

st.write("Hello World")
```

Run it with: `streamlit run app.py`

### 2. Installation and Setup

```bash
# Install Streamlit
pip install streamlit

# Test installation with demo app
streamlit hello

# Run your app
streamlit run app.py
```

### 3. Display Text with Different Styles

```python
import streamlit as st

st.title("Hello World")
st.header("This is a header")
st.subheader("This is a subheader")
st.text("Fixed width text")
st.markdown("*Italic* and **bold** text")
st.caption("Small caption text")
st.code("x = 42", language="python")
```

### 4. Secrets Management - Store Credentials Securely

Create `.streamlit/secrets.toml`:

```toml
# Everything in this section will be available as an environment variable
db_username = "Jane"
db_password = "mypassword"

# You can also add other sections
[my_other_secrets]
things_i_like = ["Streamlit", "Python"]
```

Access in your app:

```python
import streamlit as st

# Access secrets
username = st.secrets["db_username"]
password = st.secrets["db_password"]

# Access nested secrets
likes = st.secrets["my_other_secrets"]["things_i_like"]
```

### 5. Virtual Environment Setup

```bash
# Create virtual environment
python -m venv .venv

# Activate (macOS/Linux)
source .venv/bin/activate

# Activate (Windows PowerShell)
.venv\Scripts\Activate.ps1

# Install Streamlit
pip install streamlit

# Deactivate when done
deactivate
```

### 6. Configure Custom Fonts with Static Files

Directory structure:
```
your_repository/
├── .streamlit/
│   └── config.toml
├── static/
│   ├── Tuffy-Bold.ttf
│   ├── Tuffy-BoldItalic.ttf
│   ├── Tuffy-Italic.ttf
│   └── Tuffy-Regular.ttf
└── streamlit_app.py
```

Configuration in `.streamlit/config.toml`:

```toml
[server]
enableStaticServing = true

[[theme.fontFaces]]
family="tuffy"
url="app/static/Tuffy-Regular.ttf"
style="normal"
weight=400

[[theme.fontFaces]]
family="tuffy"
url="app/static/Tuffy-Bold.ttf"
style="normal"
weight=700

[theme]
font="tuffy"
```

### 7. Display Text with Custom Formatting

```python
import streamlit as st

st.write("Normal ABCabc123")
st.write("*Italic ABCabc123*")
st.write("**Bold ABCabc123**")
st.write("***Bold-italic ABCabc123***")
st.write("`Code ABCabc123`")
```

### 8. Development Requirements File

Create `requirements.txt`:

```text
streamlit>=1.45.0
```

### 9. Understanding File Upload Storage

When using `st.file_uploader`:
- Files are stored in **RAM (memory)**, not disk
- Files persist until the app reruns
- Files are deleted when:
  - User uploads another file (replaces the original)
  - User clears the file uploader
  - User closes the browser tab
- To persist files between reruns, use **caching**

### 10. LaTeX Math Expressions

```python
import streamlit as st

# Display LaTeX equation
st.latex(r"\int_a^b f(x) dx")

# More complex equation
st.latex(r"E = mc^2")
```

## Key Concepts

### Execution Model
- Streamlit apps run **top-to-bottom** on every interaction
- Each widget interaction triggers a **full script rerun**
- Use **caching** (`st.cache_data`, `st.cache_resource`) to avoid expensive recomputations
- Use **Session State** to persist data across reruns

### Widgets and Interactivity
- Widgets automatically trigger reruns when user interacts
- Widget state is managed by Streamlit
- Use `key` parameter to uniquely identify widgets
- Access widget values via Session State or return values

### Data Display
- `st.write()` is the "Swiss Army knife" - automatically formats many types
- Specialized functions: `st.dataframe()`, `st.table()`, `st.json()`, `st.metric()`
- Charts: `st.line_chart()`, `st.bar_chart()`, `st.map()`, or integration with Plotly/Altair

### Layout and Containers
- **Columns**: `st.columns()` for side-by-side layout
- **Tabs**: `st.tabs()` for tabbed content
- **Expander**: `st.expander()` for collapsible sections
- **Sidebar**: `st.sidebar` for navigation or controls

### Caching
- **`st.cache_data`**: Cache data transformations (DataFrames, lists, etc.)
- **`st.cache_resource`**: Cache global resources (DB connections, ML models)
- Caching prevents expensive operations on every rerun

### Secrets Management
- Store sensitive credentials in `.streamlit/secrets.toml`
- Never commit secrets to version control (add to `.gitignore`)
- Access via `st.secrets` dictionary
- Works locally and in Streamlit Community Cloud

### Multipage Apps
- Create `pages/` directory for automatic multi-page structure
- Or use `st.navigation()` and `st.Page()` for custom navigation
- Each page is a separate Python file
- Automatic sidebar navigation

## Reference Files

This skill includes comprehensive documentation in `references/`:

### llms-txt.md
Complete Streamlit documentation including:
- **Installation guides** for multiple platforms (pip, conda, Anaconda, cloud)
- **Getting started tutorials** for first apps and basic concepts
- **Fundamentals** covering data flow, widgets, layout, and development workflow
- **Advanced concepts** including caching, session state, database connections
- **Secrets management** for secure credential storage
- **Configuration and theming** options including custom fonts and colors
- **Multipage app** development with navigation
- **API reference** for all Streamlit commands and widgets
- **Deployment guides** for Streamlit Community Cloud and Snowflake
- **Custom components** development
- **App testing** framework and CI/CD integration

### llms-full.md
Extended documentation with detailed examples including:
- Complete installation workflows for all platforms
- Virtual environment setup with `venv` and pip
- Anaconda Distribution installation
- GitHub Codespaces and Streamlit Playground setup
- Custom font configuration with static files
- File uploader behavior and storage
- Security best practices
- Workspace management in Community Cloud

### llms.md
High-level documentation overview with links to all sections:
- Organized by topic (Get Started, Develop, Deploy)
- Quick navigation to specific API references
- Tutorial links for beginners
- Concept guides for advanced users

Use `view` to read specific reference files when detailed information is needed.

## Working with This Skill

### For Beginners
1. **Start with installation**: Read llms-full.md sections on installation
2. **Create Hello World**: Follow the "Create a Hello World app" guide
3. **Learn basic commands**: Explore `st.write()`, `st.title()`, `st.button()`
4. **Understand execution model**: Learn how Streamlit reruns on interaction
5. **Try the Quick Reference examples** above to build confidence

### For Intermediate Users
1. **Add interactivity**: Use widgets like sliders, text inputs, file uploaders
2. **Implement caching**: Speed up apps with `st.cache_data` and `st.cache_resource`
3. **Manage state**: Use Session State for persistent data across reruns
4. **Create layouts**: Use columns, tabs, and sidebars for organization
5. **Set up secrets**: Configure `.streamlit/secrets.toml` for credentials
6. **Build multipage apps**: Organize complex apps with pages directory

### For Advanced Users
1. **Custom components**: Build JavaScript-based custom widgets
2. **Advanced theming**: Configure custom fonts, colors, and styles
3. **App testing**: Use `AppTest` for automated testing
4. **Deployment optimization**: Configure caching, static files, HTTPS
5. **Database connections**: Use `st.connection()` for efficient data access
6. **Fragments**: Optimize performance with partial reruns
7. **Authentication**: Implement user login and personalization

### For Troubleshooting
- **File uploader issues**: Check llms-txt.md for storage behavior
- **Caching problems**: Review caching documentation in references
- **Widget state issues**: Read about widget behavior and Session State
- **Deployment errors**: Check configuration options and static file serving
- **Font/theme problems**: Review theming customization guides

## Resources

### Official Links
- Documentation: https://docs.streamlit.io
- API Reference: https://docs.streamlit.io/develop/api-reference
- Component Gallery: https://streamlit.io/components
- Community Forum: https://discuss.streamlit.io
- Streamlit Playground: https://streamlit.io/playground (no installation required)

### references/
Organized documentation extracted from official sources. These files contain:
- Detailed explanations of concepts
- Code examples with language annotations
- Links to original documentation
- Step-by-step tutorials
- API function signatures and parameters
- Best practices and troubleshooting tips

### scripts/
Add helper scripts here for common automation tasks like:
- Deployment scripts
- Database initialization
- Data preprocessing utilities

### assets/
Add templates, boilerplate, or example projects here like:
- Common app templates
- CSS files for custom styling
- Image assets for branding
- Example datasets

## Development Tips

### Best Practices
1. **Use virtual environments** to isolate dependencies
2. **Cache expensive operations** with `st.cache_data` or `st.cache_resource`
3. **Store secrets securely** in `.streamlit/secrets.toml`, never in code
4. **Test locally first** before deploying to cloud
5. **Use Session State** for data that should persist across reruns
6. **Organize complex apps** into multiple pages
7. **Add docstrings and comments** for maintainability
8. **Version control everything** except secrets and virtual environments

### Common Pitfalls
- **Not using caching**: Apps run slowly on every interaction
- **Committing secrets**: Credentials exposed in version control
- **Missing requirements.txt**: Deployment fails due to missing dependencies
- **Forgetting reruns**: Widget interactions cause full script reruns
- **Mixing widget keys**: Duplicate keys cause unexpected behavior

### Performance Optimization
- Use `st.cache_data` for data transformations
- Use `st.cache_resource` for database connections and ML models
- Use fragments (`@st.fragment`) for partial reruns
- Minimize expensive operations in the main script
- Load data once and cache results
- Use `st.empty()` for updating elements in place

## Python Version Support

Streamlit supports Python versions **3.9 to 3.13**. Make sure your environment uses a compatible version.

## Notes

- This skill was automatically generated from official Streamlit documentation
- Reference files preserve the structure and examples from source docs
- Code examples include language detection for better syntax highlighting
- Quick reference patterns are extracted from common usage examples in the docs
- All examples are tested and verified from official documentation

## Updating

To refresh this skill with updated documentation:
1. Re-run the scraper with the same configuration
2. The skill will be rebuilt with the latest information from docs.streamlit.io
3. Check the official changelog for new features and breaking changes
