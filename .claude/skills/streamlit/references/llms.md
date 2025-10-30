# Streamlit documentation website

> Streamlit is a powerful open-source Python framework that allows data
scientists and AI/ML engineers to build interactive apps (i.e. data apps)
with only a few lines of code.

## [Get started](/get-started)

Get started with Streamlit, from installation to your first app.

### [Installation](/get-started/installation)

Learn how to install Streamlit with comprehensive guides to use pip, conda, Anaconda Distribution, cloud environments, and command line tools.

- [Use Streamlit Playground](/get-started/installation/streamlit-playground)
  Quick start guide to Streamlit using the Streamlit Playground - no installation required.
- [Install via command line](/get-started/installation/command-line)
  Step-by-step guide to install Streamlit using command line tools and build your first Hello World app.
- [Install via Anaconda Distribution](/get-started/installation/anaconda-distribution)
  Step-by-step guide to install Streamlit using Anaconda Distribution and build your first Hello World app.
- [Use GitHub Codespaces](/get-started/installation/community-cloud)
  Quick start guide to use Community Cloud and GitHub Codespaces for browser-based development without local installation.
- [Use Snowflake](/get-started/installation/streamlit-in-snowflake)
  Quick start guide to use Streamlit in Snowflake for secure development with role-based access control.

### [Fundamentals](/get-started/fundamentals)

Learn Streamlit fundamentals with guides on main concepts and features.

- [Basic concepts](/get-started/fundamentals/main-concepts)
  Learn the fundamental concepts of Streamlit including data flow, widgets, layout, and the development workflow for building interactive apps.
- [Advanced concepts](/get-started/fundamentals/advanced-concepts)
  Learn advanced Streamlit concepts including caching with st.cache_data and st.cache_resource, session state management, and database connections.
- [Additional features](/get-started/fundamentals/additional-features)
  Explore additional Streamlit features including theming, multipage apps, fragments, custom components, and advanced UI customization options.
- [Summary](/get-started/fundamentals/summary)
  A summary of Streamlit's app model including execution flow, data handling, and state management.

### [First steps](/get-started/tutorials)

Build your first Streamlit apps with step-by-step tutorials for creating single-page and multi-page applications.

- [Create an app](/get-started/tutorials/create-an-app)
  Step-by-step tutorial for creating your first Streamlit app.
- [Create a multipage app](/get-started/tutorials/create-a-multipage-app)
  Build your first multipage app.

## [Develop](/develop)

Complete development resources for building beautiful, performant web apps with Streamlit including concepts, API reference, tutorials, and quick references.

### [Concepts](/develop/concepts)

Explore comprehensive guides to Streamlit development concepts including architecture, app design, testing, configuration, connections, custom components, and multipage applications.

- [Architecture and execution](/develop/concepts/architecture)
  Explore comprehensive guides about Streamlit's architecture and execution model, including app lifecycle, caching, session state, forms, fragments, and widget behavior.
  - [Running your app](/develop/concepts/architecture/run-your-app)
    Learn how to run Streamlit apps locally, set parameters, configure environment variables, and understand the execution model for development and production.
  - [Streamlit's architecture](/develop/concepts/architecture/architecture)
    Learn about Streamlit's client-server architecture, WebSocket connections, session management, and deployment considerations.
  - [The app chrome](/develop/concepts/architecture/app-chrome)
    Learn about Streamlit's app chrome including the status area, toolbar, and configurable app menu with developer options and deployment features.
  - [Caching](/develop/concepts/architecture/caching)
    Learn about Streamlit's caching mechanisms including st.cache_data and st.cache_resource for improving app performance and managing expensive computations.
  - [Session State](/develop/concepts/architecture/session-state)
    Learn about Session State for sharing variables between reruns, implementing callbacks, and building stateful applications across user sessions.
  - [Forms](/develop/concepts/architecture/forms)
    Learn how to use Streamlit forms with st.form to batch user input, control app reruns, and create efficient interactive interfaces with submit buttons.
  - [Fragments](/develop/concepts/architecture/fragments)
    Learn how to use Streamlit fragments to optimize app performance by rerunning portions of code instead of full scripts, improving efficiency for complex applications.
- [Architecture and execution/ Widget behavior](/develop/concepts/architecture/widget-behavior)
  Learn how Streamlit widgets behave across reruns, handle state persistence, manage user interactions, and control widget lifecycle in your applications.
- [Multipage apps](/develop/concepts/multipage-apps)
  Explore comprehensive guides about creating multipage Streamlit apps with navigation, page management, URL routing, and best practices for organizing complex apps.
  - [Overview](/develop/concepts/multipage-apps/overview)
    Learn about Streamlit's features for creating multipage apps using st.navigation, st.Page, and the pages directory with automatic navigation.
  - [Page and navigation](/develop/concepts/multipage-apps/page-and-navigation)
    Learn how to use the most flexible and preferred method for defining multipage apps.
  - [Pages directory](/develop/concepts/multipage-apps/pages-directory)
    Learn how to create multipage Streamlit apps using the simple pages/ directory approach with automatic page recognition and sidebar navigation.
  - [Working with widgets](/develop/concepts/multipage-apps/widgets)
    Learn how widgets behave across pages in multipage Streamlit apps, including widget state management, IDs, and cross-page interactions.
- [App design](/develop/concepts/design)
  Explore comprehensive guides about app design including animating elements, button behavior, custom styling, dataframe design, multithreading, and timezone handling.
  - [Animate and update elements](/develop/concepts/design/animate)
    Learn how to create dynamic, animated content in Streamlit by updating elements in-place using st.empty, st.add_rows, and other updatable containers without full app reruns.
  - [Button behavior and examples](/develop/concepts/design/buttons)
    Learn about Streamlit button behavior, state management, and practical examples using st.button with st.session_state for interactive applications.
  - [Dataframes](/develop/concepts/design/dataframes)
    Learn how to display and edit tabular data in Streamlit using st.dataframe and st.data_editor, including styling, configuration, and interactive features.
  - [Multithreading](/develop/concepts/design/multithreading)
    Learn about multithreading in Streamlit applications, including limitations, best practices, and techniques for implementing concurrent processes safely.
  - [Using custom classes](/develop/concepts/design/custom-classes)
    Learn best practices for using custom Python classes, dataclasses, and Enums in Streamlit apps, including handling class redefinition and comparison issues across reruns.
  - [Working with timezones](/develop/concepts/design/timezone-handling)
    Learn how Streamlit handles timezones, including best practices for displaying datetime information across different user timezones.
- [Connections, secrets, and authentication](/develop/concepts/connections)
  Explore comprehensive guides to connecting Streamlit apps to data sources, managing secrets securely, implementing user authentication, and following security best practices.
  - [Connecting to data](/develop/concepts/connections/connecting-to-data)
    Learn how to connect Streamlit apps to databases, APIs, and data sources with best practices for data retrieval, caching, and secure data connections.
  - [Secrets management](/develop/concepts/connections/secrets-management)
    Learn how to manage API keys, credentials, and sensitive data in Streamlit apps using native secrets management and environment variables.
  - [User authentication](/develop/concepts/connections/authentication)
    Learn how to implement user authentication and personalization in Streamlit apps with admin controls, user information, and personalized experiences across sessions.
  - [Security reminders](/develop/concepts/connections/security-reminders)
    Learn about essential security practices for Streamlit apps including protecting secrets, secure coding practices, and preventing security vulnerabilities.
- [Custom components](/develop/concepts/custom-components)
  Learn how to build and use custom Streamlit components to extend app functionality with third-party Python modules and custom UI elements.
  - [Intro to custom components](/develop/concepts/custom-components/intro)
    Learn to develop Streamlit custom components with static and bi-directional communication between Python and JavaScript for extended functionality.
  - [Create a Component](/develop/concepts/custom-components/create)
    Step-by-step guide to creating custom Streamlit components from scratch, including setup, development environment, and component structure.
  - [Publish a Component](/develop/concepts/custom-components/publish)
    Learn how to publish Streamlit custom components to PyPI, making them accessible to the Python community and Streamlit users worldwide.
  - [Limitations](/develop/concepts/custom-components/limitations)
    Understand the limitations and constraints of Streamlit custom components including iframe restrictions and differences from base Streamlit functionality.
  - [Component gallery](https://streamlit.io/components)
- [Configuration and theming](/develop/concepts/configuration)
  Explore comprehensive guides about configuring and customizing Streamlit apps including theming, HTTPS setup, static file serving, and custom styling.
  - [Configuration options](/develop/concepts/configuration/options)
    Learn about configuration options including config.toml files, environment variables, command-line flags, and runtime configuration management.
  - [HTTPS support](/develop/concepts/configuration/https-support)
    Configure HTTPS/SSL for Streamlit apps with TLS protocol, SSL termination, reverse proxies, and security best practices for production deployment.
  - [Serving static files](/develop/concepts/configuration/serving-static-files)
    Learn about static file serving in Streamlit to host and serve media files, assets, and resources that support media embedding and custom content.
  - [Customize your theme](/develop/concepts/configuration/theming)
    Learn about theming options in config.toml, including color schemes, fonts, and visual styling.
  - [Customize colors and borders](/develop/concepts/configuration/theming-customize-colors-and-borders)
    Learn how to customize colors, borders, backgrounds, and UI elements in Streamlit apps using theme configuration options and color values.
  - [Customize fonts](/develop/concepts/configuration/theming-customize-fonts)
    Learn how to configure fonts in Streamlit apps by loading custom font files from URLs or static file serving, with configuration options for different text elements.
- [App testing](/develop/concepts/app-testing)
  Explore comprehensive guides about Streamlit's native app testing framework, including setup, examples, and best practices for CI/CD integration.
  - [Get started](/develop/concepts/app-testing/get-started)
    Learn the fundamentals of Streamlit app testing with practical examples covering test structure, AppTest initialization, element retrieval, widget manipulation, and result inspection.
  - [Beyond the basics](/develop/concepts/app-testing/beyond-the-basics)
    Learn Streamlit app testing techniques covering AppTest mutable attributes including secrets, session state, query parameters, and advanced testing patterns.
  - [Automate your tests](/develop/concepts/app-testing/automate-tests)
    Learn how to integrate Streamlit app testing with Continuous Integration systems like GitHub Actions for automated testing workflows.
  - [Example](/develop/concepts/app-testing/examples)
    Complete example of testing a Streamlit login page including authentication logic, secrets management, security best practices, and comprehensive test coverage.
  - [Cheat sheet](/develop/concepts/app-testing/cheat-sheet)
    Quick reference guide for Streamlit app testing with AppTest, covering common testing patterns for text elements, widgets, charts, and interactive components.

### [API reference](/develop/api-reference)

Visually explore a gallery of Streamlit's API.

- [Write and magic](/develop/api-reference/write-magic)
  Display information in Streamlit apps using st.write and magic commands - versatile tools for showing text, data, charts, and more with minimal code.
  - [st.write](/develop/api-reference/write-magic/st.write)
    st.write displays its argument in your app.
  - [st.write_stream](/develop/api-reference/write-magic/st.write_stream)
    st.write_stream displays a stream or generator in your app using a typewriter effect.
  - [magic](/develop/api-reference/write-magic/magic)
    Magic commands in Streamlit allow you to display content without explicit commands - just put Markdown strings, data, or charts on their own line.
- [Text elements](/develop/api-reference/text)
  Display and format text in Streamlit apps with titles, headers, markdown, code blocks, captions, badges, and other text formatting components.
  - [st.title](/develop/api-reference/text/st.title)
    st.title displays text in title formatting.
  - [st.header](/develop/api-reference/text/st.header)
    st.header displays text in header formatting.
  - [st.subheader](/develop/api-reference/text/st.subheader)
    st.subheader displays text in subheader formatting.
  - [st.markdown](/develop/api-reference/text/st.markdown)
    st.markdown displays a string formatted as Markdown.
  - [st.badge](/develop/api-reference/text/st.badge)
    st.badge displays a colored badge or tag.
  - [st.caption](/develop/api-reference/text/st.caption)
    st.caption displays text in small font.
  - [st.code](/develop/api-reference/text/st.code)
    st.code displays a code block with optional syntax highlighting.
  - [st.divider](/develop/api-reference/text/st.divider)
    st.divider displays a horizontal rule in your app.
  - [st.echo](/develop/api-reference/text/st.echo)
    st.echo displays some code on the app, and then execute it.
  - [st.latex](/develop/api-reference/text/st.latex)
    st.latex displays mathematical expressions formatted as LaTeX.
  - [st.text](/develop/api-reference/text/st.text)
    st.text displays plain text without Markdown formatting.
  - [st.help](/develop/api-reference/text/st.help)
    st.help displays object's doc string, nicely formatted.
  - [st.html](/develop/api-reference/text/st.html)
    st.html renders arbitrary HTML strings to your app.
- [Data elements](/develop/api-reference/data)
  Display and interact with raw data in Streamlit using dataframes, tables, metrics, and data editors for quick, interactive data visualization and manipulation.
  - [st.dataframe](/develop/api-reference/data/st.dataframe)
    st.dataframe displays a dataframe as an interactive table.
  - [st.data_editor](/develop/api-reference/data/st.data_editor)
    st.data_editor display a data editor widget that allows you to edit dataframes and many other data structures in a table-like UI.
  - [st.column_config](/develop/api-reference/data/st.column_config)
    Configure data display and interaction in Streamlit dataframes and data editors with st.column_config - supporting text, numbers, charts, images, URLs, and more.
    - [Column](/develop/api-reference/data/st.column_config/st.column_config.column)
      st.column_config.Column configures the display of generic columns with attributes like labels, help text, width, and visibility.
    - [Text column](/develop/api-reference/data/st.column_config/st.column_config.textcolumn)
      st.column_config.TextColumn configures text columns for displaying and editing text data with validation and formatting.
    - [Number column](/develop/api-reference/data/st.column_config/st.column_config.numbercolumn)
      st.column_config.NumberColumn configures number columns for displaying and editing numerical data with formatting options.
    - [Checkbox column](/develop/api-reference/data/st.column_config/st.column_config.checkboxcolumn)
      st.column_config.CheckboxColumn configures checkbox columns for displaying boolean data and interactive true/false selection.
    - [Selectbox column](/develop/api-reference/data/st.column_config/st.column_config.selectboxcolumn)
      st.column_config.SelectboxColumn configures selectbox columns for editing categorical columns or columns with a predefined set of possible values.
    - [Multiselect column](/develop/api-reference/data/st.column_config/st.column_config.multiselectcolumn)
      st.column_config.MultiselectColumn configures multiselect columns for editing categorical columns or columns with a predefined set of possible values.
    - [Datetime column](/develop/api-reference/data/st.column_config/st.column_config.datetimecolumn)
      st.column_config.DatetimeColumn configures datetime columns for displaying and editing datetime values with a formatted text input.
    - [Date column](/develop/api-reference/data/st.column_config/st.column_config.datecolumn)
      st.column_config.DateColumn configures date columns for displaying and editing date values with date picker interface.
    - [Time column](/develop/api-reference/data/st.column_config/st.column_config.timecolumn)
      st.column_config.TimeColumn configures time columns for displaying and editing time values with time picker interface.
    - [JSON column](/develop/api-reference/data/st.column_config/st.column_config.jsoncolumn)
      st.column_config.JsonColumn configures JSON columns for displaying structured JSON data with pretty formatting.
    - [List column](/develop/api-reference/data/st.column_config/st.column_config.listcolumn)
      st.column_config.ListColumn configures list columns for displaying and editing arrays, lists, and sequences of data.
    - [Link column](/develop/api-reference/data/st.column_config/st.column_config.linkcolumn)
      st.column_config.LinkColumn configures link columns for displaying clickable URLs and hyperlinks within dataframe cells.
    - [Image column](/develop/api-reference/data/st.column_config/st.column_config.imagecolumn)
      st.column_config.ImageColumn configures image columns for displaying images directly within dataframe cells from URLs or file paths.
    - [Area chart column](/develop/api-reference/data/st.column_config/st.column_config.areachartcolumn)
      st.column_config.AreaChartColumn configures area chart columns for visualizing time series and numerical data as inline area charts.
    - [Line chart column](/develop/api-reference/data/st.column_config/st.column_config.linechartcolumn)
      st.column_config.LineChartColumn configures line chart columns for visualizing time series and numerical data as inline line charts.
    - [Bar chart column](/develop/api-reference/data/st.column_config/st.column_config.barchartcolumn)
      st.column_config.BarChartColumn configures bar chart columns for displaying numerical data as inline horizontal bar charts.
    - [Progress column](/develop/api-reference/data/st.column_config/st.column_config.progresscolumn)
      st.column_config.ProgressColumn configures progress columns for displaying numerical data as visual progress bars.
  - [st.table](/develop/api-reference/data/st.table)
    st.table displays a static table.
  - [st.metric](/develop/api-reference/data/st.metric)
    st.metric displays a metric in big bold font, with an optional indicator of how the metric changed.
  - [st.json](/develop/api-reference/data/st.json)
    st.json displays object or string as a pretty-printed JSON string.
- [Chart elements](/develop/api-reference/charts)
  Create interactive data visualizations with Streamlit's charting capabilities including simple charts, advanced visualization libraries, and community components.
  - [st.area_chart](/develop/api-reference/charts/st.area_chart)
    st.area_chart displays an interactive area chart.
  - [st.bar_chart](/develop/api-reference/charts/st.bar_chart)
    st.bar_chart displays an interactive bar chart.
  - [st.line_chart](/develop/api-reference/charts/st.line_chart)
    st.line_chart displays an interactive line chart.
  - [st.map](/develop/api-reference/charts/st.map)
    st.map displays an interactive map with points on it.
  - [st.scatter_chart](/develop/api-reference/charts/st.scatter_chart)
    st.scatter_chart displays an interactive scatter chart.
  - [st.altair_chart](/develop/api-reference/charts/st.altair_chart)
    st.altair_chart displays an interactive chart using the Altair library.
  - [st.bokeh_chart](/develop/api-reference/charts/st.bokeh_chart)
    st.bokeh_chart displays an interactive Bokeh chart.
  - [st.graphviz_chart](/develop/api-reference/charts/st.graphviz_chart)
    st.graphviz_chart displays a graph using the dagre-d3 library.
  - [st.plotly_chart](/develop/api-reference/charts/st.plotly_chart)
    st.plotly_chart displays an interactive Plotly chart.
  - [st.pydeck_chart](/develop/api-reference/charts/st.pydeck_chart)
    st.pydeck_chart displays an interactive chart using the PyDeck library.
  - [st.pyplot](/develop/api-reference/charts/st.pyplot)
    st.pyplot displays a matplotlib.pyplot figure.
  - [st.vega_lite_chart](/develop/api-reference/charts/st.vega_lite_chart)
    st.vega_lite_chart displays an interactive chart using the Vega-Lite library.
- [Input widgets](/develop/api-reference/widgets)
  Add interactivity to Streamlit apps with input widgets including buttons, sliders, text inputs, selectboxes, file uploaders, and more interactive components.
  - [st.button](/develop/api-reference/widgets/st.button)
    st.button displays a button widget.
  - [st.download_button](/develop/api-reference/widgets/st.download_button)
    st.download_button displays a download button widget.
  - [st.form_submit_button](https://docs.streamlit.io/develop/api-reference/execution-flow/st.form_submit_button)
  - [st.link_button](/develop/api-reference/widgets/st.link_button)
    st.link_button displays a button that opens a URL in a new tab.
  - [st.page_link](/develop/api-reference/widgets/st.page_link)
    st.page_link displays a link to another page in a multipage app or to an external page.
  - [st.checkbox](/develop/api-reference/widgets/st.checkbox)
    st.checkbox displays a checkbox widget.
  - [st.color_picker](/develop/api-reference/widgets/st.color_picker)
    st.color_picker displays a color picker widget.
  - [st.feedback](/develop/api-reference/widgets/st.feedback)
    st.feedback displays a widget for users to select a sentiment or rating.
  - [st.multiselect](/develop/api-reference/widgets/st.multiselect)
    st.multiselect displays a drop-down select widget where users can select multiple options.
  - [st.pills](/develop/api-reference/widgets/st.pills)
    st.pills displays a select widget where options display as pill buttons.
  - [st.radio](/develop/api-reference/widgets/st.radio)
    st.radio displays a radio button widget.
  - [st.segmented_control](/develop/api-reference/widgets/st.segmented_control)
    st.segmented_control displays a select widget where options display in a segmented button.
  - [st.selectbox](/develop/api-reference/widgets/st.selectbox)
    st.selectbox displays a drop-down select widget.
  - [st.select_slider](/develop/api-reference/widgets/st.select_slider)
    st.select_slider displays a slider widget to select items from a list.
  - [st.toggle](/develop/api-reference/widgets/st.toggle)
    st.toggle displays a toggle widget.
  - [st.number_input](/develop/api-reference/widgets/st.number_input)
    st.number_input displays a numeric input widget.
  - [st.slider](/develop/api-reference/widgets/st.slider)
    st.slider displays a slider widget for numerical values.
  - [st.date_input](/develop/api-reference/widgets/st.date_input)
    st.date_input displays a date input widget.
  - [st.time_input](/develop/api-reference/widgets/st.time_input)
    st.time_input displays a time input widget.
  - [st.chat_input](https://docs.streamlit.io/develop/api-reference/chat/st.chat_input)
  - [st.text_area](/develop/api-reference/widgets/st.text_area)
    st.text_area displays a multi-line text input widget.
  - [st.text_input](/develop/api-reference/widgets/st.text_input)
    st.text_input displays a single-line text input widget.
  - [st.audio_input](/develop/api-reference/widgets/st.audio_input)
    st.audio_input displays a widget to upload audio from a microphone.
  - [st.camera_input](/develop/api-reference/widgets/st.camera_input)
    st.camera_input displays a widget to upload images from a camera.
  - [st.data_editor](https://docs.streamlit.io/develop/api-reference/data/st.data_editor)
  - [st.file_uploader](/develop/api-reference/widgets/st.file_uploader)
    st.file_uploader displays a file uploader widget.
- [Media elements](/develop/api-reference/media)
  Embed images, videos, audio files, PDFs, and logos directly into your Streamlit apps with easy-to-use media commands.
  - [st.audio](/develop/api-reference/media/st.audio)
    st.audio displays an audio player.
  - [st.image](/develop/api-reference/media/st.image)
    st.image displays an image or list of images.
  - [st.logo](/develop/api-reference/media/st.logo)
    st.logo displays an image in the upper-left corner of your app and its sidebar.
  - [st.pdf](/develop/api-reference/media/st.pdf)
    st.pdf displays a PDF viewer.
  - [st.video](/develop/api-reference/media/st.video)
    st.video displays a video player.
- [Layouts and containers](/develop/api-reference/layout)
  Control how elements are arranged on screen with Streamlit's layout and container components including columns, expanders, sidebars, tabs, and containers.
  - [st.columns](/develop/api-reference/layout/st.columns)
    st.columns inserts containers laid out as side-by-side columns.
  - [st.container](/develop/api-reference/layout/st.container)
    st.container inserts a multi-element container that can arrange its contents vertically or horizontally.
  - [st.dialog](https://docs.streamlit.io/develop/api-reference/execution-flow/st.dialog)
  - [st.empty](/develop/api-reference/layout/st.empty)
    st.empty inserts a single-element container.
  - [st.expander](/develop/api-reference/layout/st.expander)
    st.expander inserts a multi-element container that can be expanded and collapsed.
  - [st.form](https://docs.streamlit.io/develop/api-reference/execution-flow/st.form)
  - [st.popover](/develop/api-reference/layout/st.popover)
    st.popover displays a button that opens a multi-element popover container.
  - [st.sidebar](/develop/api-reference/layout/st.sidebar)
    st.sidebar displays items in a sidebar.
  - [st.tabs](/develop/api-reference/layout/st.tabs)
    st.tabs displays a set of tabs and inserts associated containers.
- [Chat elements](/develop/api-reference/chat)
  Build conversational apps and chat interfaces using Streamlit's chat elements including st.chat_input and st.chat_message for interactive messaging experiences.
  - [st.chat_input](/develop/api-reference/chat/st.chat_input)
    st.chat_input displays a chat input widget.
  - [st.chat_message](/develop/api-reference/chat/st.chat_message)
    st.chat_message displays a user or agent icon and inserts a chat message container into the app.
  - [st.status](https://docs.streamlit.io/develop/api-reference/status/st.status)
  - [st.write_stream](https://docs.streamlit.io/develop/api-reference/write-magic/st.write_stream)
- [Status elements](/develop/api-reference/status)
  Display progress bars, status messages, notifications, and celebratory animations in your Streamlit apps.
  - [st.success](/develop/api-reference/status/st.success)
    st.success displays a success message.
  - [st.info](/develop/api-reference/status/st.info)
    st.info displays an informational message.
  - [st.warning](/develop/api-reference/status/st.warning)
    st.warning displays warning message.
  - [st.error](/develop/api-reference/status/st.error)
    st.error displays an error message.
  - [st.exception](/develop/api-reference/status/st.exception)
    st.exception displays an exception.
  - [st.progress](/develop/api-reference/status/st.progress)
    st.progress displays a progress bar.
  - [st.spinner](/develop/api-reference/status/st.spinner)
    st.spinner temporarily displays a message while executing a block of code.
  - [st.status](/develop/api-reference/status/st.status)
    st.status inserts a mutable expander element.
  - [st.toast](/develop/api-reference/status/st.toast)
    st.toast briefly displays a toast message in the upper-right corner.
  - [st.balloons](/develop/api-reference/status/st.balloons)
    st.balloons displays celebratory balloons!
  - [st.snow](/develop/api-reference/status/st.snow)
    st.snow displays celebratory snowflakes!
- [Third-party components](https://streamlit.io/components)
- [Authentication and user info](/develop/api-reference/user)
  Add user authentication and personalization in your apps with login, logout, and user information access.
  - [st.login](/develop/api-reference/user/st.login)
    st.login redirects the user to the configured authentication provider to log in.
  - [st.logout](/develop/api-reference/user/st.logout)
    st.logout removes the user's identity information and starts a clean session.
  - [st.user](/develop/api-reference/user/st.user)
    st.user returns information about the logged-in user.
- [Navigation and pages](/develop/api-reference/navigation)
  Create multipage Streamlit applications with navigation components for page switching, page management, and programmatic navigation control.
  - [st.navigation](/develop/api-reference/navigation/st.navigation)
    st.navigation declares the set of available pages available to the user in a multipage app.
  - [st.Page](/develop/api-reference/navigation/st.page)
    st.Page initializes a StreamlitPage object for multipage apps.
  - [st.page_link](https://docs.streamlit.io/develop/api-reference/widgets/st.page_link)
  - [st.switch_page](/develop/api-reference/navigation/st.switch_page)
    st.switch_page programmatically switches the active page.
- [Execution flow](/develop/api-reference/execution-flow)
  Control your app’s execution flow with forms, fragments, dialogs, and more.
  - [st.dialog](/develop/api-reference/execution-flow/st.dialog)
    st.dialog opens a multi-element modal overlay.
  - [st.form](/develop/api-reference/execution-flow/st.form)
    st.form creates a form that batches elements together with one or more submit buttons.
  - [st.form_submit_button](/develop/api-reference/execution-flow/st.form_submit_button)
    st.form_submit_button displays a form submit button.
  - [st.fragment](/develop/api-reference/execution-flow/st.fragment)
    st.fragment is a decorator that allows a function to rerun independently from the rest of the script.
  - [st.rerun](/develop/api-reference/execution-flow/st.rerun)
    st.rerun stops the current script run and immediately reruns the script.
  - [st.stop](/develop/api-reference/execution-flow/st.stop)
    st.stop immediately stops the current script run.
- [Caching and state](/develop/api-reference/caching-and-state)
  Optimize performance and manage state in Streamlit apps with st.cache_data, st.cache_resource, session state, and query parameters for efficient applications.
  - [st.cache_data](/develop/api-reference/caching-and-state/st.cache_data)
    st.cache_data is used to cache functions that return data (e.g. dataframe transforms, database queries, ML inference).
  - [st.cache_resource](/develop/api-reference/caching-and-state/st.cache_resource)
    st.cache_resource is used to cache functions that return shared, global resources (e.g. database connections, ML models).
  - [st.session_state](/develop/api-reference/caching-and-state/st.session_state)
    st.session_state is a way to share variables between reruns, for each user session.
  - [st.context](/develop/api-reference/caching-and-state/st.context)
    st.context displays a read-only dict of cookies and headers.
  - [st.query_params](/develop/api-reference/caching-and-state/st.query_params)
    st.query_params reads and manipulates query parameters in the browser's URL bar.
  - [st.experimental_get_query_params](/develop/api-reference/caching-and-state/st.experimental_get_query_params)
    st.experimental_get_query_params returns query parameters currently showing in the browser's URL bar.
  - [st.experimental_set_query_params](/develop/api-reference/caching-and-state/st.experimental_set_query_params)
    st.experimental_set_query_params sets query parameters shown in the browser's URL bar.
- [Connections and secrets](/develop/api-reference/connections)
  Connect to data sources and databases in Streamlit using st.connection, built-in connections, and secure secrets management for seamless data integration.
  - [st.secrets](/develop/api-reference/connections/st.secrets)
    st.secrets provides a dictionary-like interface to access secrets stored in a secrets.toml file for credential management.
  - [secrets.toml](/develop/api-reference/connections/secrets.toml)
    secrets.toml is a TOML file for storing secrets, API keys, and credentials for your Streamlit app.
  - [st.connection](/develop/api-reference/connections/st.connection)
    st.connection creates a connection to a data source or API for accessing external data in your Streamlit app.
  - [SnowflakeConnection](/develop/api-reference/connections/st.connections.snowflakeconnection)
    st.connections.SnowflakeConnection provides a connection to Snowflake data warehouse for querying and data operations.
  - [SQLConnection](/develop/api-reference/connections/st.connections.sqlconnection)
    st.connections.SQLConnection provides a connection to SQL databases using SQLAlchemy for querying relational data.
  - [BaseConnection](/develop/api-reference/connections/st.connections.baseconnection)
    st.connections.BaseConnection is the base class for creating custom connections to data sources and APIs.
  - [SnowparkConnection](/develop/api-reference/connections/st.connections.snowparkconnection)
    st.connections.SnowparkConnection provides a connection to Snowflake using Snowpark (deprecated, use SnowflakeConnection).
- [Custom components](/develop/api-reference/custom-components)
  Use Streamlit's custom components to create and integrate custom UI elements in your app.
  - [st.components.v1​.declare_component](/develop/api-reference/custom-components/st.components.v1.declare_component)
    st.components.v1.declare_component creates and registers a custom component for use in your Streamlit app.
  - [st.components.v1.html](/develop/api-reference/custom-components/st.components.v1.html)
    st.components.v1.html displays an HTML string in an iframe within your Streamlit app.
  - [st.components.v1.iframe](/develop/api-reference/custom-components/st.components.v1.iframe)
    st.components.v1.iframe embeds web content in an iframe.
- [Configuration](/develop/api-reference/configuration)
  Configure Streamlit apps with config.toml files, page settings, and runtime configuration management for customized app behavior and appearance.
  - [config.toml](/develop/api-reference/configuration/config.toml)
    Complete reference guide for Streamlit's config.toml configuration file, including all available sections and options for customizing your Streamlit application settings.
  - [st.get_option](/develop/api-reference/configuration/st.get_option)
    st.get_option retrieves a single configuration option.
  - [st.set_option](/develop/api-reference/configuration/st.set_option)
    st.set_option updates a single configuration option (from a small list of options that can be updated at runtime).
  - [st.set_page_config](/develop/api-reference/configuration/st.set_page_config)
    st.set_page_config configures the default settings of the page.
- [App testing](/develop/api-reference/app-testing)
  Run headless tests on your Streamlit app with a built-in testing framework to simulate user input.
  - [st.testing.v1.AppTest](/develop/api-reference/app-testing/st.testing.v1.apptest)
    The AppTest class simulates Streamlit apps in automated tests and provides methods to manipulate and inspect app contents programmatically.
  - [Testing element classes](/develop/api-reference/app-testing/testing-element-classes)
    Testing element classes include Block, Element, ChatMessage, Column, and Tab for accessing and inspecting Streamlit app components in tests.
- [Command line](/develop/api-reference/cli)
  Run Streamlit apps and manage configuration using the command-line interface for app execution, cache management, and system diagnostics.
  - [streamlit cache](/develop/api-reference/cli/cache)
    streamlit cache clear removes persisted files from the on-disk Streamlit cache.
  - [streamlit config](/develop/api-reference/cli/config)
    streamlit config show displays all available configuration options with descriptions and values.
  - [streamlit docs](/develop/api-reference/cli/docs)
    streamlit docs opens the Streamlit documentation in your default browser.
  - [streamlit hello](/develop/api-reference/cli/hello)
    streamlit hello runs an example Streamlit app to verify installation and demonstrate features.
  - [streamlit help](/develop/api-reference/cli/help)
    streamlit help displays all available CLI commands and their usage information.
  - [streamlit init](/develop/api-reference/cli/init)
    streamlit init creates the files for a new Streamlit app project including requirements.txt and streamlit_app.py.
  - [streamlit run](/develop/api-reference/cli/run)
    streamlit run starts your Streamlit app with optional configuration and script arguments.
  - [streamlit version](/develop/api-reference/cli/version)
    streamlit version prints Streamlit's version number.

### [Tutorials](/develop/tutorials)

Explore step-by-step tutorials for building Streamlit apps including authentication, database connections, data visualization, and advanced features.

- [Authentication and personalization](/develop/tutorials/authentication)
  Learn to implement user authentication in Streamlit apps using OpenID Connect (OIDC) with providers like Google and Microsoft for personalized experiences.
  - [Google Auth Platform](/develop/tutorials/authentication/google)
    Learn how to authenticate users with Google's OpenID Connect (OIDC) service
  - [Microsoft Entra](/develop/tutorials/authentication/microsoft)
    Learn how to authenticate users with Microsoft Entra and Microsoft Identity Platform for work, school, and personal accounts in Streamlit apps.
- [Chat and LLM apps](/develop/tutorials/chat-and-llm-apps)
  Learn to build LLM applications with Streamlit including conversational apps, chat interfaces, response feedback, and response revision features.
  - [Build a basic LLM chat app](/develop/tutorials/chat-and-llm-apps/build-conversational-apps)
    Learn to build conversational LLM applications with Streamlit using chat elements, session state, and Python to create ChatGPT-like experiences.
  - [Build an LLM app using LangChain](/develop/tutorials/chat-and-llm-apps/llm-quickstart)
    Learn to build an LLM-powered Streamlit app using LangChain and OpenAI, with step-by-step instructions and a deployment guide.
  - [Get chat response feedback](/develop/tutorials/chat-and-llm-apps/chat-response-feedback)
    Learn to collect user feedback on LLM responses in Streamlit chat apps using st.feedback widget for sentiment collection and response improvement.
  - [Validate and edit chat responses](/develop/tutorials/chat-and-llm-apps/validate-and-edit-chat-responses)
    Learn to build a Streamlit chat app that lets users validate, correct, and improve LLM chat responses with multi-stage response editing workflows.
- [Configuration and theming](/develop/tutorials/configuration-and-theming)
  Learn to customize Streamlit app themes and configurations including external fonts, static fonts, variable fonts, and visual styling options.
  - [Use external font files](/develop/tutorials/configuration-and-theming/external-fonts)
    Learn how to use externally hosted fonts and font fallbacks to customize typography in Streamlit apps with variable font files and external resources.
  - [Use static font files](/develop/tutorials/configuration-and-theming/static-fonts)
    Learn how to use static font files to customize typography in Streamlit apps with self-hosted font files and multiple font weight configurations.
  - [Use variable font files](/develop/tutorials/configuration-and-theming/variable-fonts)
    Learn how to use variable font files to customize typography in Streamlit apps with self-hosted font files and advanced font configuration options.
- [Connect to data sources](/develop/tutorials/databases)
  Step-by-step tutorials for connecting Streamlit apps to databases and APIs including SQL databases, cloud storage, and popular services.
  - [AWS S3](/develop/tutorials/databases/aws-s3)
    Learn how to connect to AWS S3 from your Streamlit apps using FilesConnection, s3fs library, and secrets management.
  - [BigQuery](/develop/tutorials/databases/bigquery)
    Learn how to connect Streamlit apps to Google BigQuery for querying large datasets using service account authentication and st.connection.
  - [Firestore](https://blog.streamlit.io/streamlit-firestore/)
  - [Google Cloud Storage](/develop/tutorials/databases/gcs)
    Learn how to access and manage files on Google Cloud Storage from Streamlit apps using FilesConnection, gcsfs library, and secrets management.
  - [Microsoft SQL Server](/develop/tutorials/databases/mssql)
    Learn how to connect Streamlit apps to remote Microsoft SQL Server databases using pyodbc library and secrets management for enterprise SQL access.
  - [MongoDB](/develop/tutorials/databases/mongodb)
    Learn how to connect Streamlit apps to remote MongoDB databases using PyMongo library and secrets management for NoSQL document databases.
  - [MySQL](/develop/tutorials/databases/mysql)
    Learn how to connect Streamlit apps to remote MySQL databases using st.connection and secrets management for SQL queries and data access.
  - [Neon](/develop/tutorials/databases/neon)
    Learn how to connect Streamlit apps to Neon serverless PostgreSQL databases with instant branching, automatic scaling, and managed hosting.
  - [PostgreSQL](/develop/tutorials/databases/postgresql)
    Learn how to connect Streamlit apps to remote PostgreSQL databases using st.connection and secrets management for database queries.
  - [Private Google Sheet](/develop/tutorials/databases/private-gsheet)
    Learn how to connect Streamlit apps to private Google Sheets using st.connection, GSheetsConnection, service accounts, and secrets management.
  - [Public Google Sheet](/develop/tutorials/databases/public-gsheet)
    Learn how to connect Streamlit apps to public Google Sheets for data access using st.connection, GSheetsConnection, and secrets management.
  - [Snowflake](/develop/tutorials/databases/snowflake)
    Learn how to connect Streamlit apps to Snowflake databases using st.connection, Snowpark library, and secrets management for cloud data warehouse access.
  - [Supabase](/develop/tutorials/databases/supabase)
    Learn how to connect Streamlit apps to Supabase (open source Firebase alternative) using st.connection, Supabase Connector, and PostgreSQL backend.
  - [Tableau](/develop/tutorials/databases/tableau)
    Learn how to connect Streamlit apps to Tableau for accessing data and visualizations using tableauserverclient library and secrets management.
  - [TiDB](/develop/tutorials/databases/tidb)
    Learn how to connect Streamlit apps to TiDB distributed SQL databases using st.connection and secrets management for cloud-native database access.
  - [TigerGraph](/develop/tutorials/databases/tigergraph)
    Learn how to connect Streamlit apps to TigerGraph graph databases using pyTigerGraph library and secrets management for graph analytics.
- [Elements](/develop/tutorials/elements)
  Tutorials for working with Streamlit elements including charts, dataframes, selections, and interactive components for rich user interfaces.
  - [Annotate an Altair chart](/develop/tutorials/elements/annotate-an-altair-chart)
    Learn how to annotate Altair charts in Streamlit with text, images, and emojis using layered charts for enhanced data visualization.
  - [Get dataframe row-selections](/develop/tutorials/elements/dataframe-row-selections)
    Learn how to get row selections from users in Streamlit dataframes using st.dataframe selection features for interactive data exploration.
- [Execution flow](/develop/tutorials/execution-flow)
  Master Streamlit's execution model with tutorials on fragments, reruns, and execution control for optimal app performance and user experience.
  - [Rerun your app from a fragment](/develop/tutorials/execution-flow/trigger-a-full-script-rerun-from-a-fragment)
    Learn how to trigger a full script rerun from within a Streamlit fragment using st.rerun for advanced execution flow control and state management.
  - [Create a multiple-container fragment](/develop/tutorials/execution-flow/create-a-multiple-container-fragment)
    Learn how to create Streamlit fragments that span multiple containers using st.empty() to prevent element accumulation during fragment reruns.
  - [Start and stop a streaming fragment](/develop/tutorials/execution-flow/start-and-stop-fragment-auto-reruns)
    Learn how to create streaming fragments with time intervals, and programmatically start and stop auto-reruns for live data monitoring and streaming applications.
- [Multipage apps](/develop/tutorials/multipage)
  Learn to build multipage Streamlit applications with custom navigation, dynamic navigation, and advanced page management techniques.
  - [Dynamic navigation](/develop/tutorials/multipage/dynamic-navigation)
    Learn how to create a dynamic, conditional navigation menu in your multipage app.

### [Quick reference](/develop/quick-reference)

Access quick references including API cheat sheets, prerelease features, and comprehensive release notes for Streamlit development.

- [Cheat sheet](/develop/quick-reference/cheat-sheet)
  Comprehensive Streamlit API cheat sheet with all widgets, layout elements, data display, and utility functions for quick reference during development.
- [Release notes](/develop/quick-reference/release-notes)
  A changelog of highlights and fixes for the latest version of Streamlit.
  - [2025](/develop/quick-reference/release-notes/2025)
    A changelog of highlights and fixes for each version of Streamlit released in 2025.
  - [2024](/develop/quick-reference/release-notes/2024)
    A changelog of highlights and fixes for each version of Streamlit released in 2024.
  - [2023](/develop/quick-reference/release-notes/2023)
    A changelog of highlights and fixes for each version of Streamlit released in 2023.
  - [2022](/develop/quick-reference/release-notes/2022)
    A changelog of highlights and fixes for each version of Streamlit released in 2022.
  - [2021](/develop/quick-reference/release-notes/2021)
    A changelog of highlights and fixes for each version of Streamlit released in 2021.
  - [2020](/develop/quick-reference/release-notes/2020)
    A changelog of highlights and fixes for each version of Streamlit released in 2020.
  - [2019](/develop/quick-reference/release-notes/2019)
    A changelog of highlights and fixes for each version of Streamlit released in 2019.
- [Pre-release features](/develop/quick-reference/prerelease)
  Explore Streamlit's experimental and beta features before they become stable, including bleeding-edge functionality and upcoming enhancements.

### [Quick reference/ Roadmap](https://roadmap.streamlit.app)

## [Deploy](/deploy)

Deploy your Streamlit apps to various platforms including Community Cloud, Snowflake, and other cloud providers with comprehensive guides.

### [Concepts](/deploy/concepts)

Learn fundamental deployment concepts including dependencies, secrets management, and app startup for Streamlit applications.

- [Dependencies](/deploy/concepts/dependencies)
  Learn how to manage Python dependencies, requirements.txt files, and package installation when deploying Streamlit apps to cloud platforms.
- [Secrets](/deploy/concepts/secrets)
  Learn best practices for managing secrets, credentials, and API keys securely when deploying Streamlit apps to production environments.

### [Streamlit Community Cloud](/deploy/streamlit-community-cloud)

Deploy and manage Streamlit apps for free with Community Cloud - connect to GitHub, deploy in minutes, and share with the world.

- [Get started](/deploy/streamlit-community-cloud/get-started)
  Get started with Streamlit Community Cloud - create your account, connect GitHub, and deploy your first app with step-by-step guides.
  - [Quickstart](/deploy/streamlit-community-cloud/get-started/quickstart)
    Quick start guide to create your Community Cloud account, deploy a sample app, and start editing with GitHub Codespaces in minutes.
  - [Create your account](/deploy/streamlit-community-cloud/get-started/create-your-account)
    Learn how to create your Streamlit Community Cloud account using email, Google, or GitHub authentication methods.
  - [Connect your GitHub account](/deploy/streamlit-community-cloud/get-started/connect-your-github-account)
    Connect your GitHub account to Community Cloud to deploy apps from public and private repositories with proper permissions.
  - [Explore your workspace](/deploy/streamlit-community-cloud/get-started/explore-your-workspace)
    Learn how to navigate your Community Cloud workspace, switch between workspaces, and manage your apps and profile.
  - [Deploy from a template](/deploy/streamlit-community-cloud/get-started/deploy-from-a-template)
    Learn how to deploy a Streamlit app from a template using Community Cloud's template picker with GitHub Codespaces integration.
  - [Fork and edit a public app](/deploy/streamlit-community-cloud/get-started/fork-and-edit-a-public-app)
    Learn how to fork and edit public Streamlit apps from Community Cloud with GitHub Codespaces for immediate development.
  - [Trust and security](/deploy/streamlit-community-cloud/get-started/trust-and-security)
    Learn about Streamlit Community Cloud's security model including authentication, data protection, encryption, and compliance measures.
- [Deploy your app](/deploy/streamlit-community-cloud/deploy-your-app)
  Complete guide to preparing and deploying your Streamlit app on Community Cloud with file organization, dependencies, and secrets management.
  - [File organization](/deploy/streamlit-community-cloud/deploy-your-app/file-organization)
    Learn how to organize your files, dependencies, and configuration for successful Community Cloud deployment including subdirectories and multiple apps.
  - [App dependencies](/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies)
    Learn how to manage Python and external dependencies for your Community Cloud app using requirements.txt, packages.txt, and other package managers.
  - [Secrets management](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management)
    Learn how to securely manage secrets, credentials, and API keys for your Community Cloud app using the secrets management interface.
  - [Deploy!](/deploy/streamlit-community-cloud/deploy-your-app/deploy)
    Step-by-step guide to deploy your Streamlit app on Community Cloud including repository selection, configuration, and deployment process.
- [Manage your app](/deploy/streamlit-community-cloud/manage-your-app)
  Learn how to manage your deployed Streamlit apps including editing, analytics, settings, and resource optimization on Community Cloud.
  - [App analytics](/deploy/streamlit-community-cloud/manage-your-app/app-analytics)
    Learn how to view and analyze your Streamlit app's viewership data including total viewers, unique visitors, and privacy considerations.
  - [App settings](/deploy/streamlit-community-cloud/manage-your-app/app-settings)
    Learn how to configure your Streamlit app settings including URL customization, sharing permissions, and secrets management.
  - [Delete your app](/deploy/streamlit-community-cloud/manage-your-app/delete-your-app)
    Learn how to delete your Streamlit app from Community Cloud and understand when deletion might be necessary.
  - [Edit your app](/deploy/streamlit-community-cloud/manage-your-app/edit-your-app)
    Learn how to edit your deployed Streamlit app using GitHub Codespaces or any development environment with automatic deployment updates.
  - [Favorite your app](/deploy/streamlit-community-cloud/manage-your-app/favorite-your-app)
    Learn how to favorite and unfavorite your Streamlit apps in Community Cloud to quickly access them from your workspace.
  - [Reboot your app](/deploy/streamlit-community-cloud/manage-your-app/reboot-your-app)
    Learn how to reboot your Streamlit app on Community Cloud to clear memory, force fresh builds, and resolve issues.
  - [Rename your app in GitHub](/deploy/streamlit-community-cloud/manage-your-app/rename-your-app)
    Learn how to safely rename your GitHub repository or change app coordinates without losing access to your Streamlit app.
  - [Upgrade Python](/deploy/streamlit-community-cloud/manage-your-app/upgrade-python)
    Learn how to upgrade your Streamlit app's Python version on Community Cloud by deleting and redeploying with advanced settings.
  - [Upgrade Streamlit](/deploy/streamlit-community-cloud/manage-your-app/upgrade-streamlit)
    Learn how to upgrade your Streamlit library version on Community Cloud using dependency files or rebooting your app.
- [Share your app](/deploy/streamlit-community-cloud/share-your-app)
  Learn how to share your deployed Streamlit app publicly or privately, invite viewers, and add GitHub badges for better discoverability.
  - [Embed your app](/deploy/streamlit-community-cloud/share-your-app/embed-your-app)
    Learn how to embed your Streamlit app in websites, blogs, and platforms using iframe and oEmbed methods with customizable options.
  - [Search indexability](/deploy/streamlit-community-cloud/share-your-app/indexability)
    Learn how to optimize your Streamlit app for search engines with custom subdomains, descriptive titles, and meta descriptions.
  - [Share previews](/deploy/streamlit-community-cloud/share-your-app/share-previews)
    Learn how to create compelling share previews for social media with custom titles and descriptions for your Streamlit app.
- [Manage your account](/deploy/streamlit-community-cloud/manage-your-account)
  Manage your Streamlit Community Cloud account including email updates, GitHub connections, and account deletion options.
  - [Sign in and sign out](/deploy/streamlit-community-cloud/manage-your-account/sign-in-sign-out)
    Learn how to sign in to and sign out of Streamlit Community Cloud using Google, GitHub, or email authentication methods.
  - [Workspace settings](/deploy/streamlit-community-cloud/manage-your-account/workspace-settings)
    Learn how to access and manage your Streamlit Community Cloud workspace settings including linked accounts, limits, and support resources.
  - [Manage your GitHub connection](/deploy/streamlit-community-cloud/manage-your-account/manage-your-github-connection)
    Learn how to manage your GitHub connection to Community Cloud including adding organization access, revoking permissions, and handling account changes.
  - [Update your email](/deploy/streamlit-community-cloud/manage-your-account/update-your-email)
    Learn how to update your email address on Streamlit Community Cloud using account merging or GitHub account changes.
  - [Delete your account](/deploy/streamlit-community-cloud/manage-your-account/delete-your-account)
    Learn how to permanently delete your Streamlit Community Cloud account and all associated apps and data.
- [Status and limitations](/deploy/streamlit-community-cloud/status)
  Learn about Community Cloud status, limitations, GitHub OAuth scope, Python environments, configuration overrides, and IP addresses.

### [Snowflake](/deploy/snowflake)

Deploy Streamlit apps in Snowflake for enterprise-grade security and data integration with native apps and container services.

### [Other platforms](/deploy/tutorials)

Step-by-step deployment guides for various cloud platforms including Community Cloud, Docker, and Kubernetes.

- [Docker](/deploy/tutorials/docker)
  Learn how to containerize and deploy your Streamlit app using Docker with step-by-step instructions for corporate networks and cloud deployment.
- [Kubernetes](/deploy/tutorials/kubernetes)
  Learn how to deploy your Streamlit app using Kubernetes with Google Container Registry, OAuth authentication, and TLS support.

## [Knowledge base](/knowledge-base)

Explore troubleshooting guides for common problems.

### [FAQ](/knowledge-base/using-streamlit)

Explore answers to frequently asked questions about developing a Streamlit app.

### [Installing dependencies](/knowledge-base/dependencies)

Explore common dependency and environment problems, and see possible solutions.

### [Deployment issues](/knowledge-base/deploy)

Explore common deployment problems and solutions.