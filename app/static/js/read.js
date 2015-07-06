$(function() {
    $('#read_button').bind('click', function() {
            $.ajax({
                url: $SCRIPT_ROOT + '/read',
                data: $('#full_text').serialize(),
                type: 'POST',
                success: function(response){
                    var json_obj = JSON.parse(response);
                    $.each(json_obj, function(key,value) {
                        var sentence_obj = JSON.parse(value);
                        var sentence = new Sentence(sentence_obj, key);
                        sentence.buildDiv();
                        console.log(sentence_obj['ru_text'] + " : " + sentence_obj['en_text']);
                    });
                },
                error: function(error){
                    console.log(error);
                }
            })
        });
});