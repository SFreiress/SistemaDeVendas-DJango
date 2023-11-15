$(document).ready(function () {
  $("#telefoneInput").inputmask("(99) 9999-9999");
  $("#celularInput").inputmask("(99) 9 9999-9999");
  $("#cepInput").inputmask("99.999-999");
  $("#cpfInput").inputmask("999.999.999-99");

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
