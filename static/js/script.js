const texts = ["Python Developer", "Flask Enthusiast", "Web Designer"];
let count = 0, index = 0, currentText = '', letter = '';
(function type(){
  if(count === texts.length) count = 0;
  currentText = texts[count];
  letter = currentText.slice(0, ++index);

  document.querySelector(".typing").textContent = letter;
  if(letter.length === currentText.length){
    count++;
    index = 0;
    setTimeout(type, 2000);
  } else {
    setTimeout(type, 150);
  }
}());
