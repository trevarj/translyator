function Sentence(sentence_json, id){
    this.sentence_id = id;
    this.ru_text = sentence_json['ru_text'];
    this.en_text = sentence_json['en_text'];
    this.weight  = sentence_json['weight'];

    this.buildDiv = function(){
        jQuery('<span/>', {
            id: "sentence" + this.sentence_id,
            text: this.ru_text,
            'data-alt_text': this.en_text,
            'data-weight': this.weight
        }).appendTo('body');
    };
}