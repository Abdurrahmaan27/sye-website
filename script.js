function performOCR() {
    const imageInput = document.getElementById("image-input");
    const imagePreview = document.getElementById("image-preview");
    const output = document.getElementById("output");
  

    if (imageInput.files && imageInput.files[0]) {
      const reader = new FileReader();
  
      reader.onload = function (e) {
        imagePreview.innerHTML = `<img src="${e.target.result}" alt="Image Preview">`;
        Tesseract.recognize(e.target.result,'eng+hin')
          .then(function (result) {
            output.textContent = result.data.text;
          })
          .catch(function (error) {
            console.error("Error:", error);
          });
      };
  
      reader.readAsDataURL(imageInput.files[0]);
    }
  }
  