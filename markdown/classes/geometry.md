<!-- HTML Specific Tags -->
<title>(Class) StructuredGeometry2D - Twisted Engine Documentation (Master Branch)</title>
<link rel="stylesheet" href="class.css">
<script src="https://cdn.jsdelivr.net/gh/google/code-prettify@master/loader/run_prettify.js"></script>

# StructuredGeometry2D

## Methods

<pre class="prettyprint">StructuredGeometry2D()</pre>
<ul>- StructuredGeometry2D(const StructuredGeometry2D &)</ul>

<pre class="prettyprint">StructuredGeometry2D(float *p_vertices, <a href="https://en.cppreference.com/w/c/types/size_t">size_t</a> p_size)</pre>
<ul>- Setter: vertices(p_vertices), size(p_size)</ul>

<pre class="prettyprint">float *get_raw_values() const</pre>
<ul>- Returns the original type of the vertices as a float array.</ul>

<pre class="prettyprint">float *get_raw_values_ptr() const</pre>
<ul>- Returns the original type of the vertices as a pointer of a float array.</ul>

<pre class="prettyprint"><a href="https://en.cppreference.com/w/c/types/size_t">size_t</a> get_length() const</pre>
<ul>- Returns the size provided in the constructor.</ul>

<pre class="prettyprint"><a href="vector2.html">Vector2</a> get_vertex(int p_index) const</pre>
<ul>- Returns the corresponding vertex position at the provided index.</ul>

<pre class="prettyprint">void set_vertex(int p_index, <a href="vector2.html">Vector2</a> p_vertex)</pre>
<ul>- Sets the corresponding vertex position at the provided index.</ul>

<pre class="prettyprint"><a href="geometry.html">StructuredGeometry2D</a> normalized(<a href="vector2.html">Vector2</a> p_space) const</pre>
<ul>- Normalizes every vertex position based on the space vector provided.</ul>
