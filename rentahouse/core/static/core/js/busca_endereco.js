$(document).ready(function() {

    function limpa_formulario_cep() {
        // Limpa valores do formulário de cep.
        $("#id_logradouro").val("");
        $("#id_bairro").val("");
        $("#id_municipio").val("");
        $("#id_uf").val("");
    }

    //Quando o campo cep perde o foco.
    $("#id_cep").blur(function() {

        //Nova variável "cep" somente com dígitos.
        var cep = $(this).val().replace(/\D/g, '');

        //Verifica se campo cep possui valor informado.
        if (cep != "") {

            //Expressão regular para validar o CEP.
            var validacep = /^[0-9]{8}$/;

            //Valida o formato do CEP.
            if(validacep.test(cep)) {

                //Preenche os campos com "..." enquanto consulta webservice.
                $("#id_logradouro").val("...");
                $("#id_bairro").val("...");
                $("#id_municipio").val("...");
                $("#id_uf").val("...");

                //Consulta o webservice viacep.com.br/
                $.getJSON("https://viacep.com.br/ws/"+ cep +"/json/?callback=?", function(dados) {

                    if (!("erro" in dados)) {
                        //Atualiza os campos com os valores da consulta.
                        $("#id_logradouro").val(dados.logradouro);
                        $("#id_bairro").val(dados.bairro);
                        $("#id_municipio").val(dados.localidade);
                        $("#id_uf").val(dados.uf);

                        // Atualiza conteudo da tela
                        $("select").material_select();
                        $("#id_logradouro").focus();
                        $("#id_bairro").focus();
                        $("#id_municipio").focus();
                    } //end if.
                    else {
                        //CEP pesquisado não foi encontrado.
                        limpa_formulario_cep();
                        alert("CEP não encontrado.");
                    }
                });
            } //end if.
            else {
                //cep é inválido.
                limpa_formulario_cep();
                alert("Formato de CEP inválido.");
            }
        } //end if.
        else {
            //cep sem valor, limpa formulário.
            limpa_formulario_cep();
        }
    });
});