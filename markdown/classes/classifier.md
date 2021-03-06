<!-- HTML Specific Tags -->
<title>(Class) Classifier - Twisted Engine Documentation (Master Branch)</title>
<link rel="stylesheet" href="class.css">
<script src="https://cdn.jsdelivr.net/gh/google/code-prettify@master/loader/run_prettify.js"></script>

# Classifier

## Methods

<pre class="prettyprint">Classifier()</pre>
<ul>- Classifier(const Classifier &)</ul>

<pre class="prettyprint">Classifier(String p_name)</pre>
<ul>- Setter: name(p_name)</ul>

<pre class="prettyprint">Classifier *get_parent()</pre>
<ul>- Returns the parented classifier in the SceneTree.</ul>

<pre class="prettyprint">virtual void init()</pre>
<ul>- Called when the class is constructed. Note that this occurs before the start() method is called and before the scene all of the classifier's children have been constructed.</ul>

<pre class="prettyprint">virtual void start()</pre>
<ul>- Called after all of the classifier's children have been constructed and after the classifier has been registered as a valid SceneTree object.</ul>

<pre class="prettyprint">virtual void update(float delta)</pre>
<ul>- Called every frame. This method is called more often than fixed_update(), however is not as stable for jobs such as physics.</ul>

<pre class="prettyprint">virtual void fixed_update(float delta)</pre>
<ul>- Called every physics frame.</ul>

<pre class="prettyprint">virtual void finish()</pre>
<ul>- Called either when the Classifier is deleted, or on message 'engine_shutdown'.</ul>