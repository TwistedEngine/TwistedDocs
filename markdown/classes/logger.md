<!-- HTML Specific Tags -->
<title>(Class) Logger - Twisted Engine Documentation (Master Branch)</title>
<link rel="stylesheet" href="class.css">
<script src="https://cdn.jsdelivr.net/gh/google/code-prettify@master/loader/run_prettify.js"></script>

# Logger

## Methods

<pre class="prettyprint">Logger()</pre>
<ul>- Logger(const Logger &)</ul>

<pre class="prettyprint">void log(<a href="string.html">String</a> p_line)</pre>
<ul>- Appends the provided string to the log text.</ul>

<pre class="prettyprint">void logv(<a href="string.html">String</a> p_line)</pre>
<ul>- Does the same as Logger.log() but prints the provided string.</ul>

<pre class="prettyprint">void print_log()</pre>
<ul>- Prints the current log text.</ul>

<pre class="prettyprint">void write_log()</pre>
<ul>- Writes the log text to a log file.</ul>