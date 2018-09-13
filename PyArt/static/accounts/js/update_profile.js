$(document).ready(function () {
    $(':input').attr('readonly','readonly')
    $('#confirm_update').attr('disabled','disabled')
})

function Update() {
    $(':input').removeAttr('readonly')
    $('#confirm_update').removeAttr('disabled')
}