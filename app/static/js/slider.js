$(function() {
    $( "#slider" ).slider({
            orientation: "vertical",
            value:0,
            min: 0,
            max: 1000,
            step: 200,
        slide: function( event, ui ) {
            $('#reader-div > span').each(function(index){
                var is_translated = $(this).attr('data-istrans');
                var weight = $(this).data('weight');
                if(is_translated === 'false'){
                    // text isnt translated yet on DOM
                    // see if we should show the translation...
                    if (weight >= 1000 - ui.value){
                        Sentence.swapLanguage($(this).attr('id'));
                        $(this).attr('data-istrans', true);
                    }
                }
                else {
                    // text was already translated
                    // check to see if it should untranslate
                    if(weight < 1000 - ui.value){
                        Sentence.swapLanguage($(this).attr('id'));
                        $(this).attr('data-istrans', false);
                    }
                }
            });
        }
    });
});