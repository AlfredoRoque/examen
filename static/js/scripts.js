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


document.getElementById("close-sidebar").addEventListener("click", function() {
    document.getElementById("tabla").classList.remove("tablaIncomp");
    document.getElementById("tabla").classList.add("tablaComp");
    document.querySelector(".page-wrapper").classList.remove("toggled");
});
document.getElementById("show-sidebar").addEventListener("click", function() {
    document.getElementById("tabla").classList.remove("tablaComp");
    document.getElementById("tabla").classList.add("tablaIncomp");
    document.querySelector(".page-wrapper").classList.add("toggled");
});

$(document).ready(function() {
    $("#tablaE").tablesorter();
});

$('th').click(function() {
    var table = $(this).parents('table').eq(0)
    var rows = table.find('tr:gt(0)').toArray().sort(comparer($(this).index()))
    this.asc = !this.asc
    if (!this.asc) {
        rows = rows.reverse()
    }
    for (var i = 0; i < rows.length; i++) {
        table.append(rows[i])
    }
    setIcon($(this), this.asc);
})

function comparer(index) {
    return function(a, b) {
        var valA = getCellValue(a, index),
            valB = getCellValue(b, index)
        return $.isNumeric(valA) && $.isNumeric(valB) ? valA - valB : valA.localeCompare(valB)
    }
}

function getCellValue(row, index) {
    return $(row).children('td').eq(index).html()
}

function setIcon(element, asc) {
    $("th").each(function(index) {
        $(this).removeClass("sorting");
        $(this).removeClass("asc");
        $(this).removeClass("desc");
    });
    element.addClass("sorting");
    if (asc) element.addClass("asc");
    else element.addClass("desc");
}



addEventListener("load", () => {
    if(document.getElementById("mensaje")!=null){
        if (document.getElementById("mensaje").getAttribute("hidden")) {
            document.getElementById("mensaje").removeAttribute("hidden");
        }
        setTimeout(function() {
            document.getElementById("mensaje").setAttribute("hidden", "true");
        }, 5000)
    }
})