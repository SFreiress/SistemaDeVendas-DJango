$(document).ready(function () {
  $("#telefoneInput").inputmask("(99) 9999-9999");
  $("#celularInput").inputmask("(99) 9 9999-9999");
  $("#cepInput").inputmask("99 999-999");
  $("#cnpjInput").inputmask("99.999.999/9999-99");

  $("#numeroInput").on("input", function () {
    $(this).val(function (index, value) {
      return value.replace(/\D/g, "");
    });
  });

  $("#emailInput").on("input", function () {
    var email = $(this).val();
    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if (emailRegex.test(email)) {
      $("#emailMessage")
        .text("Endereço de e-mail válido")
        .css("color", "green");
    } else {
      $("#emailMessage")
        .text("Endereço de e-mail inválido")
        .css("color", "red");
    }
  });
});
