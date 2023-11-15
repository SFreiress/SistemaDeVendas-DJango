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

  $("#cepInput").on("keypress", async function (e) {
    console.log("CAIU" + e.which);
    if (e.which === 13) {
      var cep = $(this)
        .val()
        .replace(/[^0-9]/g, "");

      try {
        const request = await fetch(`https://viacep.com.br/ws/${cep}/json/`);
        const data = await request.json();

        $("#enderecoInput").val(data.logradouro);
        $("#bairroInput").val(data.bairro);
        $("#cidadeInput").val(data.localidade);
        $("#ufInput").val(data.uf);
        $("#estadoInput").val(data.uf);

        console.log(data);
      } catch (error) {
        console.error("Erro na requisição:", error);
      }
    }
  });
});
