$(document).ready(function() {
    /* Inicialização do Seletor */
    $('select').material_select();

    /* Mascarar Telefones */
    var TelefoneMask = function (val) {
        return val.replace(/\D/g, '').length === 11 ? '(00) 00000-0000' : '(00) 0000-00009';
    }

    var spOptions = {
        onKeyPress: function(val, e, field, options) {
            field.mask(TelefoneMask.apply({}, arguments), options);
        }
    };

    $('#id_telefone').mask(TelefoneMask, spOptions);

    /* Mascarar CEP */
    $('#id_cep').mask('00000-000', {reverse: true});

});
