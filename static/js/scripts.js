pass1 = document.getElementById('id_password1');
pass2 = document.getElementById('id_password2');
form = document.getElementById('miformulario');

if (form != null) {
    form.addEventListener('submit', (e) => {

        if (pass1.value != pass2.value) {
            e.preventDefault();
            document.getElementById("error").classList.add("mostrar");

            return false;
        } else {
            document.getElementById("error").classList.remove("mostrar");

            document.getElementById("ok").classList.remove("ocultar");

            document.getElementById("login").disabled = true;

            setTimeout(function() {
                location.reload();
            }, 3000);

            return true;
        }

    })
}