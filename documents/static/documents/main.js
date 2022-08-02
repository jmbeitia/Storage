$(document).on('click', '#upload', function () {

    beforeSend();

    function beforeSend() {
        $("#staticBackdrop .modal-content").html("");
        $("#staticBackdrop").modal("show");

    }

    fetch('/documents/add_docfile/', {
        headers: {
            'Accept': 'application/json',
            'X-Requested-With': 'XMLHttpRequest',
        },
    })
        .then(response => {
            return response.json()
        })
        .then(data => {
            $("#staticBackdrop .modal-content").html(data.docfile_form);
        })


});


$(document).on("click", ".docfile_submit", function () {

    var formdata = new FormData();

    var docfile = $('#id_docfile')[0].files[0]

    formdata.append('docfile', docfile);

    var csrf = $('input[name="csrfmiddlewaretoken"]').val();

    formdata.append('csrfmiddlewaretoken', csrf);

    var name = $('input[name="name"]').val();

    formdata.append('name', name)

    fetch('/documents/add_docfile/', {
        method: 'POST',
        mode: 'same-origin',
        headers: {
            'Accept': 'application/json',
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': csrf,
        },
        body: formdata
    })
        .then(response => {
            return response.json()
        })
        .then(data => {

            if (!data.form_is_valid) {
                $("#staticBackdrop .modal-body").html("");
                $("#staticBackdrop .modal-body").html(data.docfile_form);
            }

            if (data.form_is_valid) {
                $("#staticBackdrop").modal("hide");
                location.reload();
            }

        })

    return false;

});