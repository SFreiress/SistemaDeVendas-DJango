$(document).ready(function() {
    $('#precoInput').on('input', function() {
        $(this).val(function (index, value) {
            return value.replace(/[^\d.]|(?<=\.\d*)\./g, '');
        });
    });

    $('#qtd_estoqueInput').on('input', function() {
        $(this).val(function (index, value) {
            return value.replace(/\D/g, '');
        });
    });
});