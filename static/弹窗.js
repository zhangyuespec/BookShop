var btn = document.getElementById('open_btn');
var div = document.getElementById('background');
var close = document.getElementById('close-button');

btn.onclick = function show() {
	div.style.display = "block";
}

close.onclick = function close() {
	div.style.display = "none";
}

window.onclick = function close(e) {
	if (e.target == div) {
		div.style.display = "none";
	}
}
