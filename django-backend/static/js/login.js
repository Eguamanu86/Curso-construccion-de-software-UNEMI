const loginForm = document.querySelector('#id-form-login')

loginForm.addEventListener('submit', async (event) => {
  event.preventDefault()
  const formData = new FormData(loginForm)

  console.log(formData.get("username"));
  console.log(formData.get("password"));

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

  const response = await fetch('/seguridad/login', options)
  if (!response.ok) {
    throw response
  }
  const data = await response.json()

})
