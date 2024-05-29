function clipboard(short_code) {
  console.log(short_code);
  var copyText = document.getElementById(`url-link${short_code}`);

  copyText.select();
  copyText.setSelectionRange(0, 99999);
  navigator.clipboard
    .writeText(copyText.value)
    .then(function () {
      var copyButton = document.getElementById(`copy-btn${short_code}`);
      copyButton.classList.add('copied');
      copyButton.textContent = 'copied!';

      setTimeout(function () {
        copyButton.classList.remove('copied');
        copyButton.textContent = 'copy';
      }, 2000);
    })
    .catch(function (error) {
      console.error('Failed to copy text: ', error);
    });
}
