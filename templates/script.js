function clickedButton() {
	var xhr = new XMLHttpRequest();
  xhr.addEventListener("load", reqListener);
	xhr.open('POST', '/clicked', true);
	xhr.send('The button was clicked!');
}

function signinButton() {
	var xhr = new XMLHttpRequest();
  xhr.addEventListener("load", reqListener);
  xhr.open('GET', '/signin?username=Pete&password=1234', true);
	xhr.send('The button was clicked!');
}

function reqListener () {
  // Write to the browser's debug console
  console.log(this.responseText);

  // Update an element on our web page
  document.getElementById("what_to_do").innerText = this.responseText;
}
