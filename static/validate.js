// checks to see if information being passed is valid

(function () {
    // calls the require validation class on index.html
    const forms = document.querySelectorAll('.requires-validation')

    Array.from(forms).forEach(function (form) {

      // looks for on action for submit button
        form.addEventListener('submit', function (event) {

          // checks if not valid
          if (!form.checkValidity()) {
            event.preventDefault()
            event.stopPropagation()
          }
          
          // calls the was verifited class if verified
          form.classList.add('was-validated')
        }, false)
      })
    })()
    