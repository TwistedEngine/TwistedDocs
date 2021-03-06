<!-- HTML Specific Tags -->
<title>(Class) String - Twisted Engine Documentation (Master Branch)</title>
<link rel="stylesheet" href="class.css">
<script src="https://cdn.jsdelivr.net/gh/google/code-prettify@master/loader/run_prettify.js"></script>

# String

## Methods

<pre class="prettyprint">String()</pre>
<ul>- String(const String &)</ul>

<pre class="prettyprint">String(char *p_bytes)</pre>
<ul>- Setter: raw_string(p_bytes)</ul>

<pre class="prettyprint">String(int p_int)</pre>
<ul>- Setter: raw_string(p_int)</ul>

<pre class="prettyprint">String(const char *p_bytes)</pre>
<ul>- Setter: raw_string(p_bytes)</ul>

<pre class="prettyprint">void replace(<a href="string.html">String</a> p_auct, <a href="string.html">String</a> p_rep)</pre>
<ul>- Replaces any instance of p_auct in this string with p_rep.</ul>

<pre class="prettyprint"><a href="string.html">String</a> replaced(<a href="string.html">String</a> p_auct, <a href="string.html">String</a> p_rep)</pre>
<ul>- Returns the value of String.replace().</ul>

<pre class="prettyprint"><a href="string.html">String</a> *split(char p_delim)</pre>
<ul>- Returns a string array split by the provided deliminator.</ul>

<pre class="prettyprint">const char *raw() const</pre>
<ul>- Returns the string as a C string.</ul>

<pre class="prettyprint"><a href="https://en.cppreference.com/w/c/types/size_t">size_t</a> size() const</pre>
<ul>- Returns the size of the string.</ul>