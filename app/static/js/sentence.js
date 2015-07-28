function Sentence(sentence_json, id){
    this.sentence_id = id;
    this.ru_text = sentence_json['ru_text'];
    this.en_text = sentence_json['en_text'];
    this.weight  = sentence_json['weight'];

    this.buildDiv = function(){
        this.divId = "sentence" + this.sentence_id;
        jQuery('<span/>', {
            id: this.divId,
            class: "sentence",
            text: this.ru_text,
            'data-alt_text': this.en_text,
            'data-weight': this.weight,
            'data-istrans': false
        }).appendTo('#reader-div');
    };
}

Sentence.swapLanguage = function(span_id){
    var new_alt_text = $('#' + span_id).text();
    var new_text = $('#' + span_id).data('alt_text');
    $('#' + span_id).data('alt_text', new_alt_text);
    $('#' + span_id).text(new_text);
};