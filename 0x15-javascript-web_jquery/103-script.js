$(document).ready(function () {
	$('INPUT#translate_btn').click(fetchTranslation);
    $('INPUT#lang_code').keyup(function (event) {
        if (event.keyCode == 13) {
            fetchTranslation();
        }
    });


    function fetchTranslation() {
        var lang_code = $('INPUT#lang_code').val();
        var url = 'https://fourtonfish.com/hellosalut/?lang=' + lang_code;
        $.get(url, function (data) {
            $('DIV#hello').text(data.hello);
        });
    };
});