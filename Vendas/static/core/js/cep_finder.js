$("#cepInput").on("keypress", async function (e) {
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
    } catch (error) {
      console.error("Erro na requisição: ", error);
    }
  }
});