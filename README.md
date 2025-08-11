<h1>Claude Chatbot with Streamlit</h1>

<p>This is a conversational AI chatbot built using <strong>Streamlit</strong> and powered by Anthropic's Claude model API. The chatbot allows users to interact with Claude AI through a user-friendly web interface.</p>

<h2>Features</h2>
<ul>
    <li>Seamless integration with the Anthropic Claude model API.</li>
    <li>User-friendly chat interface built with Streamlit.</li>
    <li>Adjustable creativity and response length via Streamlit sidebar settings.</li>
    <li>Easy-to-use input field for user prompts.</li>
    <li>Display of full chat history in real time.</li>
</ul>

<h2>Table of Contents</h2>
<ul>
    <li><a href="#project-overview">Project Overview</a></li>
    <li><a href="#prerequisites">Prerequisites</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#configuration">Configuration</a></li>
    <li><a href="#project-structure">Project Structure</a></li>
    <li><a href="#contributing">Contributing</a></li>
</ul>

<h2 id="project-overview">Project Overview</h2>
<p>This project is a simple chatbot utilizing Anthropic's Claude AI model for generating conversational responses. The web interface is developed using Streamlit and offers a smooth, interactive chat experience. Users can configure the response creativity and length using the sidebar options.</p>

<h2 id="prerequisites">Prerequisites</h2>
<p>Before running this project, ensure you have the following installed:</p>
<ul>
    <li><strong>Python 3.8+</strong></li>
    <li><strong>pip</strong> (Python package installer)</li>
</ul>

<h2 id="installation">Installation</h2>

<h3>Step 1: Clone the Repository</h3>
<pre><code>git clone https://github.com/devu-13here/New-Repo.git
cd New-Repo
</code></pre>

<h3>Step 2: Create a Virtual Environment</h3>
<p>For <strong>Windows</strong>:</p>
<pre><code>python -m venv venv</code></pre>
<p>For <strong>macOS/Linux</strong>:</p>
<pre><code>python3 -m venv venv</code></pre>

<h3>Step 3: Activate the Virtual Environment</h3>
<p>For <strong>Windows</strong>:</p>
<pre><code>.\venv\Scripts\activate</code></pre>
<p>For <strong>macOS/Linux</strong>:</p>
<pre><code>source venv/bin/activate</code></pre>

<h3>Step 4: Install Required Dependencies</h3>
<p>Once your virtual environment is activated, run the following command to install the necessary Python libraries:</p>
<pre><code>pip install -r requirements.txt</code></pre>

<h2 id="usage">Usage</h2>

<h3>1. Set Your Anthropic API Key</h3>
<p>To use this chatbot, you need an Anthropic API key. You can get one from the <a href="https://console.anthropic.com/">Anthropic Console</a>.</p>
<p>Once you have your key, set it as an environment variable named <code>ANTHROPIC_API_KEY</code>.</p>
<p>For <strong>macOS/Linux</strong>:</p>
<pre><code>export ANTHROPIC_API_KEY="your_anthropic_api_key_here"</code></pre>
<p>For <strong>Windows (Command Prompt)</strong>:</p>
<pre><code>set ANTHROPIC_API_KEY="your_anthropic_api_key_here"</code></pre>
<p>For <strong>Windows (PowerShell)</strong>:</p>
<pre><code>$env:ANTHROPIC_API_KEY="your_anthropic_api_key_here"</code></pre>
<p><strong>Note:</strong> You may need to restart your terminal or IDE for the environment variable to be recognized.</p>

<h3>2. Run the Application</h3>
<p>Start the Streamlit app by running the following command:</p>
<pre><code>streamlit run src/main.py</code></pre>

<h3>3. Interact with the Chatbot</h3>
<p>Open the URL provided by Streamlit (usually <code>http://localhost:8501</code>) in your browser. Type a message in the chat input field and start interacting with the Claude-powered chatbot.</p>

<h2 id="configuration">Configuration</h2>
<p><strong>Anthropic API Key</strong>: The application is configured using the <code>ANTHROPIC_API_KEY</code> environment variable. The official Anthropic Python library, used in this project, automatically detects and uses this variable.</p>
<p><strong>Chat Parameters</strong>: The creativity (temperature) and response length (max tokens) of the chatbot can be adjusted in real-time via sliders in the Streamlit sidebar.</p>

<h2 id="project-structure">Project Structure</h2>
<pre><code>New-Repo/
│
├── src/
│   └── main.py               # Main script for Streamlit chatbot
├── .gitignore
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
└── LICENSE                    # License file (if any)
</code></pre>

<h2 id="contributing">Contributing</h2>
<p>Contributions are welcome! Feel free to submit a pull request or open an issue to improve this project.</p>

<ol>
    <li>Fork the repository.</li>
    <li>Create a feature branch (<code>git checkout -b feature/YourFeature</code>).</li>
    <li>Commit your changes (<code>git commit -am 'Add YourFeature'</code>).</li>
    <li>Push to the branch (<code>git push origin feature/YourFeature</code>).</li>
    <li>Open a pull request.</li>
</ol>

</body>
</html>
