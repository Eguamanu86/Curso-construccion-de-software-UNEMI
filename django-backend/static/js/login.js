// creamos la referencia hacia el formulario HTML
const loginForm = document.querySelector('#id-form-login')

// agregamos escuchador "Submit"
loginForm.addEventListener('submit', async (event) => {
  event.preventDefault()

  // convertimos en formulario html en un objeto FormData
  const formData = new FormData(loginForm)

  const options = {
    method: 'POST',
    credentials: 'same-origin',
    headers: {
      'Accept': 'application/json',
      'X-Requested-With': 'XMLHttpRequest', //Necessary to work with request.is_ajax()
      //'X-CSRFToken': Cookies.get('csrftoken')
    },
    body: formData
  }

  // request/solicitud hacia el servidor Asyncronico
  const response = await fetch('/seguridad/login', options)
  // response.ok = 200
  if (!response.ok) {
    throw response
  }

  const data = await response.json()
  console.log(data)

  if (data.resp) {
    window.location = '/'
  }

})
